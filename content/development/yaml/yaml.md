---
title: "YAML"
draft: false
---

Multiline

```yaml
script:
  - |
    echo
        a
        b
        c
```

```yaml
script:
  - >
    echo
        a
        b
        c
```

```yaml
script:  |
    echo
        a
        b
        c
```

Merge

```yml
base: &base
  name: Everyone has same name

foo: &foo
  <<: *base
  age: 10

bar: &bar
  <<: *base
  age: 20
```

Anchors and Aliases

```yaml
invoice:
  billing address: &address1
    name: Santa Clause
    street: Santa Claus Lane
    city: North Pole
  shipping address: *address1
```

```yaml
name1: &name Larry Wall
name2: *name
```
