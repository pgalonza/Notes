---
title: "Lutris"
draft: false
---

Create play file

```yaml
name: "<Name of game>"
game_slug: <name in low case and separate with "-">
runner: <runner (wine)>
version: "<Game version(GOG,Steam).>"
files:
- setupfile: N/A:Select the game's setup file
game:
  exe: <path to game exe file>
  prefix: $GAMEDIR
installer:
- task:
    name: create_prefix
    prefix: $GAMEDIR
- task:
    app: <name of dll to install>
    name: winetricks
    prefix: $GAMEDIR
    silent: true
- task:
    args: <args of installer>
    description: <Game description>
    executable: setupfile
    name: wineexec
    prefix: $GAMEDIR
system:
  env:
    <variable name>: <variable value>
  pulse_latency: false
wine:
  Desktop: true
```
