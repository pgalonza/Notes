---
title: "Vagrant"
draft: false
description: "Vagrant notes"
---

{{< toc >}}

SSH key

```bash
<vagrant_dir>/.vagrant/machines/<vm_name>/virtualbox/private_key
```

Boxes

```bash
~/.vagrant.d/boxes/
```

Ansible provisioner

```ruby
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "<playbook name>.yml"
  end
```

Sync folder

```ruby
config.vm.synced_folder "<host folder>", "<guest folder>"
```

Create multiple virtual machines

```ruby
Vagrant.configure("2") do |config|

  (1..3).each do |i|
    config.vm.box = "<box_name>"
    config.vm.synced_folder "<src_path>", "<dst_path>", create: true
    config.vm.define "<name>#{i}" do |node| 
      node.vm.hostname = "<host_name>#{i}"
      
      node.vm.network "private_network", ip: "<local_ip>#{i}",
          name: "vboxnet0"
      node.vm.network "public_network", type: "dhcp",
          name: "eno1"

      node.vm.provider "virtualbox" do |vb|
          vb.cpus = 1
          vb.memory = 4096
          vb.gui = false
          vb.name = "<vm_name>#{i}"
    end
  end

  config.vm.provision "shell", inline: <<-SHELL
    dnf update -y
    dnf install epel-release -y
    dnf install vim -y
  SHEL
end
```

```ruby
Vagrant.configure("2") do |config|

  config.vm.box = "<box_name>"

  config.vm.define "vrrp1" do |vrrp1|
    vrrp1.vm.hostname = "<host name>"
    vrrp1.vm.network "private_network", ip: "<local_ip>",
      name: "vboxnet0"
    vrrp1.vm.provider "virtualbox" do |vb1|
      vb1.name = "VRRP1"
    end
  end

  config.vm.define "vrrp2" do |vrrp2|
    vrrp2.vm.hostname = "<host name>"
    vrrp2.vm.network "private_network", ip: "<host ip>",
      name: "vboxnet0"
    vrrp2.vm.provider "virtualbox" do |vb2|
      vb2.name = "VRRP2"
    end
  end

  config.vm.network "public_network", type: "dhcp",
    name: "eno1"

  config.vm.provider "virtualbox" do |vb|
      vb.cpus = 1
      vb.memory = 4096
      vb.gui = false
  end

  config.vm.provision "shell", inline: <<-SHELL
    dnf update -y
    dnf install epel-release -y
    dnf install vim -y
  SHELL
end
```

## Troubleshooting

Vagrant was unable to mount VirtualBox shared folders

``` bash
vagrant plugin install vagrant-vbguest
vagrant vbguest
```

On Guest OS

```bash
sudo mount -t vboxsf -o uid=1000,gid=1000,_netdev <tag_name> <dir_dst> 
```

VBoxClient: error while loading shared libraries

```bash
dnf install libX11-devel libXt-devel libXext-devel libXmu-devel kernel-headers kernel-devel xorg-x11-drivers xorg-x11-utils
```
