# YAML

Multiline
```
script:
  - |
    echo
        a
        b
        c
```
```
script:
  - >
    echo
        a
        b
        c
```

Merge
```
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
```
---
invoice:
  billing address: &address1
    name: Santa Clause
    street: Santa Claus Lane
    city: North Pole
  shipping address: *address1
You can also use it for scalars:

---
name1: &name Larry Wall
name2: *name
```
