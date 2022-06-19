# Network

Check MTU

```bash
ping <ip_address> -4 -M do -s $((1500-28))
ping <ip_address> -6 -M do -s $((1500-48))
```
