---
title: "Files"
draft: false
description: "Essential Linux file operations: encoding conversion, file type detection, ELF analysis, comparison, merging, cleaning, inode inspection, and integrity checking with md5sum for system administrators."
summary: "A handy collection of command‑line utilities for everyday file manipulation, inspection, and verification on Linux systems."
---

Encoding

```bash
iconv -f cp1251 -t utf8
file -bi
```

Determine file type

```bash
file file_name
```

Display file or file system information

```bash
stat <file path|filesystem path>
```

Display ELF-file information

```bash
readelf -a <file path|filesystem path>
```

Show header of file

```bash
cat /usr/bin/python3.9 | hexdump -C | head
```

Compare files

```bash
comm
diff
```

Merge files

```bash
paste
```

Clean file

```bash
truncate -s 0 <file_name>
echo '' > <file_name>
> <file_name>
cat /dev/null > <file_name>
true | tee <file_name>
dd if=/dev/null of=<file_name>
shred <file_name>
shred -zu <file_name>
```

Translate or delete characters

```bash
tr
```

Show inodes

```bash
ls -i <file path>
```

Show file system where file

```bash
df <file path>
```

Print the locate of binary

```bash
type -a command
whereis command
which command
command -v command
```

Show all symbols

```bash
cat -A file_name
```

Find changed files use md5

```bash
find . -type f -exec md5sum {} \; > checklist.chk
md5sum -c checklist.chk
```

Display in hexadecimal

```bash
hexdump -C
xdd
```

Output starting with byte

```bash
tail -c +<number of bytes> <file name>
```

Display the assembler mnemonics for the machine instructions

```bash
objdump -d <file name>
```

## Search in files

```bash
find -name *.c -type f | xargs grep open

grep -R open --include="*.c".
```

## Ldd

Show shared object dependencies

```bash
ldd /path_to_object
```

## TAR

Create archive

```bash
tar -cvpzf archive.tar.gz /forpack
```

Unpack archive

```bash
tar -xzvf archive.tar.gz
tar -xfvj archive.tar.bz2 -C /var/www
```

View archive

```bash
tar -tf archive.tar
```

## TREE

```bash
tree -d -L 2
```

## SED

Replace in all files

```bash
sed -i 's/old_text/new_text/g' *
```

## Grep

Print only matching parts

```bash
grep -Eo "pattern" file | sort | uniq
```

## Cp

Copy with attributes mode, ownership, timestamps

```bash
cp -rp /source /destination
```

Copy with save all parameters

```bash
cp -a /source /destination
```

Backup

```bash
cp <file name>.txt{,.bak}
```

## Shred

Overwrite a file and delete

```bash
shred -zvu -n 10 file_name
```

Overwrite a file

```bash
shred -zv -n 10 file_name
```

Overwrite a partition

```bash
shred -fvz /dev/sdXX
```

## Tail

Terminate tail when process over

```bash
tail -f <file name> --pid=<PID>
```

Wait when file exist

```bash
tail -f <file name> --retry
```