terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.74"
}

provider "yandex" {
  token     = var.ya_token
  cloud_id  = var.cloud_id
  folder_id = var.folder_id
  zone      = "ru-central1-b"
}

resource "yandex_iam_service_account" "vmadmin" {
  name        = "vmadmin"
  description = "service account to manage VMs"
}


resource "yandex_resourcemanager_folder_iam_member" "vm-editor-role" {
  folder_id = var.folder_id
  role      = "editor"
  member    = "serviceAccount:${yandex_iam_service_account.vmadmin.id}"
}

resource "yandex_compute_instance_group" "s-group1" {
  name               = "react-vms"
  service_account_id = yandex_iam_service_account.vmadmin.id
  depends_on = [yandex_iam_service_account.vmadmin, yandex_resourcemanager_folder_iam_member.vm-editor-role]
  instance_template {
    name = "nginx-{instance.index}"
    platform_id = "standard-v3"
    resources {
      cores         = 2
      memory        = 1
      core_fraction = 20
    }
    boot_disk {
      initialize_params {
        image_id = "fd82re2tpfl4chaupeuf"
        size     = 10
      }
    }
    network_interface {
      network_id = yandex_vpc_network.s-network-1.id
      subnet_ids = [yandex_vpc_subnet.s-subnet-1.id, yandex_vpc_subnet.s-subnet-2.id]
      nat = true
    }
    metadata = {
      ssh-keys = "ubuntu:${file("<ssh public key path>")}"
    }

  }
  load_balancer {
    target_group_name = "balancer-target-group"
  }
  allocation_policy {
    zones = ["ru-central1-b", "ru-central1-a"]
  }
  deploy_policy {
    max_unavailable = 2
    max_creating    = 2
    max_expansion   = 2
    max_deleting    = 2
  }
  scale_policy {
    fixed_scale {
      size = var.size
    }
  }

}

resource "yandex_compute_instance" "s-vm-1" {
  name = "react-vm-1"
  platform_id = "standard-v3"

  resources {
    cores  = 2
    memory = 1
    core_fraction = 20
  }

  boot_disk {
    initialize_params {
      image_id = "fd82re2tpfl4chaupeuf"
      size     = 10
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.s-subnet-1.id
    nat = true
  }

  scheduling_policy {
    preemptible = true
  }

  metadata = {
    ssh-keys = "ubuntu:${file("<ssh public key path>")}"
  }
}

resource "yandex_vpc_network" "s-network-1" {
  name = "network1"
}

resource "yandex_vpc_subnet" "s-subnet-1" {
  name           = "subnet1"
  zone           = "ru-central1-b"
  network_id     = yandex_vpc_network.s-network-1.id
  v4_cidr_blocks = ["192.168.10.0/24"]
}

resource "yandex_vpc_subnet" "s-subnet-2" {
  name           = "subnet2"
  zone           = "ru-central1-a"
  network_id     = yandex_vpc_network.s-network-1.id
  v4_cidr_blocks = ["192.168.11.0/24"]
}

resource "yandex_lb_network_load_balancer" "s-balancer-1" {
  name = "react-network-load-balancer"

  listener {
    name = "react-listener"
    port = 80
    target_port = var.service_port
    external_address_spec {
      ip_version = "ipv4"
    }
  }

  attached_target_group {
    target_group_id = yandex_compute_instance_group.s-group1.load_balancer.0.target_group_id
    healthcheck {
      name = "http"
      http_options {
        port = var.health_check_port
        path = "/health"
      }
    }
  }
}

resource "null_resource" "command" {
  count = var.size

  connection {
    type = "ssh"
    user = "ubuntu"
    host = element(yandex_compute_instance_group.s-group1.instances[*].network_interface[0].nat_ip_address, count.index)
    private_key = file("<ssh private key path>)
  }

  provisioner "file" {
    source = "<script name>.sh"
    destination = "<script name>.sh"
  }

  provisioner "remote-exec" {
    inline = [
      "chmod +x ~/<script name>.sh",
      "sudo ~/<script name>.sh",
    ]
  }

  provisioner "local-exec" {
    command = "ansible-playbook --key-file <ssh key> -i ${element(yandex_compute_instance_group.s-group1.instances[*].network_interface[0].nat_ip_address, count.index)} <playbook name>"
  }
}

data "terraform_remote_state" "gitlab" {
  backend = "http"

  config = {
    address = var.gitlab_remote_state_address
    username = var.gitlab_username
    password = var.gitlab_access_token
  }
}

variable "size" {
  type = string
  default = 2
}

output "front-internal" {
  value = yandex_compute_instance_group.s-group1.instances.*.network_interface.0.ip_address
}

output "front-external" {
  value = yandex_compute_instance_group.s-group1.instances.*.network_interface.0.nat_ip_address
}

output "backend-internal" {
  value = yandex_compute_instance.s-vm-1.network_interface.0.ip_address
}

output "backend-external" {
  value = yandex_compute_instance.s-vm-1.network_interface.0.nat_ip_address
}

output "balancer-external" {
  value = yandex_lb_network_load_balancer.s-balancer-1.listener
}

variable "ya_token" {
  type = string
}

variable "cloud_id" {
  type = string
}

variable "folder_id" {
  type = string
}

variable "gitlab_remote_state_address" {
  type = string
  description = "Gitlab remote state file address"
}

variable "gitlab_username" {
  type = string
  description = "Gitlab username to query remote state"
}

variable "gitlab_access_token" {
  type = string
  description = "GitLab access token to query remote state"
}