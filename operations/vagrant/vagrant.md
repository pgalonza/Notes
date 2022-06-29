# Vagrant

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
