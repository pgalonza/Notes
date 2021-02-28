# Development

# Tools, Programs and Libraries

* **postman** - the Collaboration Platform for API Development.

## New line representation

Character encoding|Abbreviation|hex value|dec value|Escape sequence
------------------|------------|---------|---------|---------------
ASCII             |LF          |0A       |10       |\n
ASCII             |CR LF       |0D 0A    |13 10    |\r\n
ASCII             |CR          |0D       |13       |\r
ASCII             |RS          |1E       |30       |
ASCII             |LF CR       |0A 0D    |10 13    |\n\r
ATASCII           |            |9B       |155      |
EBCDIC            |NL          |15       |21       |\025

## ANSI

* \033[0-7m - effects
* \033[30-37m - text colors
* \033[40-47m - background colors

## VKontakte

Get  user token
* _https://vk.com/dev/permissions_

```
https://oauth.vk.com/authorize?client_id=<application_id>&scope=<permissions>&response_type=token
```
