# Kernel
## Make and build
Configure
```
make menuconfig
```

Make kernel all targets
```
make -j(<NUMBER_OF_CORES> + 1) all
```

Make modules
```
make modules_install
```

Make headers
```
make headers_install
```

Install kernel
```
make install
```
