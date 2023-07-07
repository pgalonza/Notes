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

Display file or file system status

```bash
stat <file path|filesystem path>
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
df file path>
```
