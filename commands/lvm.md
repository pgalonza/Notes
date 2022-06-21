# Lvm

## Physical volumes

View information about pv

```bash
pvs
```

Initialize physical volume

```bash
pvcreate /dev/sda
```

Move extents from one physical volume to another
report progress and only the extents belonging to the named LV

```bash
pvmove -i 10 -n /dev/pv_name /dev/sda /dev/sdb
```

Resize physical volume

```bash
pvresize /dev/sda
```

## Volume groups

View information about vg

```bash
vgs
```

Add physical volumes to a volume group

```bash
vgextend fg_name /dev/sda
```

Display volume group information

```bash
vgdisplay vg_name -v
```

Remove physical volume

```bash
vgreduce fg_name /dev/sda
```

Create a volume group

```bash
vgcreate vg_name /dev/sda
```

## Logical volumes

Create a logical volume

```bash
lvcreate -l 100%FREE -n lv_name vg_name
```

View information about lv

```bash
lvs
lvs -a -o+devices
```

Add space to a logical volume

```bash
lvextend -l +50%FREE /dev/vg_name/lv_name
lvextend -l +100%FREE /dev/vg_name/lv_name
```
