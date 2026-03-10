---
title: "GoLang"
draft: false
aliases:
  - /development/go/go/
description: "Concise Go (Golang) notes covering syntax, iota enums, debugging tips, and best practices for efficient Go development."
summary: "A handy reference for Go developers, featuring code snippets and essential techniques to streamline your Go programming workflow."
---

Enum iota

```golang
const (
    c0 = iota
    c1 = iota
    c2
)
```

View hiden symbols

```golang
fmt.Printf("%#v")
```
