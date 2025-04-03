---
title: "Files"
draft: false
description: "CLI commands for work with files"
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
