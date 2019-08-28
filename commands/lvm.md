# Physical volumes

###### View information about pv
```
pvs
```

###### Initialize physical volume
```
pvcreate /dev/sda
```

###### Move extents from one physical volume to another
report progress and only the extents belonging to the named LV
```
pvmove -i 10 -n /dev/pv_name /dev/sda /dev/sdb
```

###### Resize physical volume
```
pvresize /dev/sda
```
# Volume groups

###### View information about vg
```
vgs
```

###### Add physical volumes to a volume group
```
vgextend fg_name /dev/sda
```

###### Display volume group information
```
vgdisplay vg_name -v
```

###### Remove physical volume
```
vgreduce fg_name /dev/sda
```

###### Create a volume group
```
vgcreate vg_name /dev/sda
```

# Logical volumes

###### Create a logical volume
```
lvcreate -l 100%FREE -n lv_name vg_name
```

###### View information about lv
```
lvs
lvs -a -o+devices
```

###### Add space to a logical volume
```
lvextend -l +50%FREE /dev/vg_name/lv_name
lvextend -l +100%FREE /dev/vg_name/lv_name
```
