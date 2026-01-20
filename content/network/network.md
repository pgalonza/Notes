---
title: "Network"
date: 2024-08-17T14:24:30+03:00
draft: false
description: "Discover the world of computer networks through our concise notes. From fundamentals to advanced topics, get valuable insights on network optimization, troubleshooting, and security."
aliases:
  - /networks/network/
---

{{< toc >}}

## IPv4

Special Addresses

- [RFC 950](https://www.ietf.org/rfc/rfc950.txt)
- [RFC 943](https://www.ietf.org/rfc/rfc943.txt)
- [RFC 943](https://www.ietf.org/rfc/rfc1878.txt)

IPv4 address = 4 byte = 32 bit
Network mask = 4 byte = 32 bit
255.255.255.0 = /24(the sum of the units in the binary system)

|1st Octet|2nd Octet|3rd Octet|4th Octet|
|:-------:|:-------:|:-------:|:-------:|
|192      |168      |0        |0        |
|255      |255      |255      |0        |
|1byte    |1byte    |1byte    |1byte    |
|11000000 |10101000 |00000000 |00000000 |
|11111111 |11111111 |11111111 |00000000 |

* Network: 192.168.0.0 = 11000000.10101000.00000000.00000000
* Start host: 192.168.0.1 = 11000000.10101000.00000000.00000001
* End host: 192.168.0.254 = 11000000.10101000.00000000.11111110
* Broadcast: 192.168.0.255 = 11000000.10101000.00000000.11111111

Calculating the number of hosts by mask

2^(32 - \<subnet mask\>)


## IPv6

IPv4 address = 16 byte = 128 bit


|1st Hexctet|2nd Hexctet|3rd Hexctet|4th Hexctet|5th Hexctet|6th Hexctet|8th Hexctet|
|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|
|2001       |0db8       |1234       |0000       |0000       |0000       |0000       |
|2byte      |2byte      |2byte      |2byte      |2byte      |2byte      |2byte      |


## MAC

MAC address = 6 byte = 48 bit