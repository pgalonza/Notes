---
title: TMUX
draft: false
description: "CLI commands for TMUX"
---

Run

```bash
tmux attach || tmux new -s session1
```

```bash
Ctrl+b c — создать окошко;
Ctrl+b 0...9 — перейти в такое-то окошко;
Ctrl+b p — перейти в предыдущее окошко;
Ctrl+b n — перейти в следующее окошко;
Ctrl+b l — перейти в предыдущее активное окошко (из которого вы переключились в текущее);
Ctrl+b & — закрыть окошко (а можно просто набрать exit в терминале).

Ctrl+b % — разделить текущую панель на две, по вертикали;
Ctrl+b " — разделить текущую панель на две, по горизонтали (это кавычка, которая около Enter, а не Shift+2);
Ctrl+b →←↑↓ — переходить между панелями;
Ctrl+b x — закрыть панель (а можно просто набрать exit в терминале).
```

Parallel execution of commands

```bash
tmux set synchronize-panes on
```
