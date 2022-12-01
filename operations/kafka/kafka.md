# Kafka

* File system: XFS
* Mount option: noatime
* vm.swappinness: 1
* vm.dirty_background_ratio: <10
* vm.dirty_ratio: >20
* net.core.wmem_default: 2097152
* net.core.rmem_default: 2097152
* net.ipv4.tcp_wmem: 4096 65536 2048000
* net.ipv4.tcp_rmem: 4096 65536 2048000
* net.core.wmem_max: > net.ipv4.tcp_wmem
* net.core.rmem_max: > net.ipv4.tcp_rmem
* net.ipv4.tcp_window_scaling: 1
* net.ipv4.tcp_max_syn_backlog: > 1024
* net.core.netdev_max_backlog: > 1000
