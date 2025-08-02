# Linux Command Assistant

Ask natural-language questions about Linux terminal usage and get the exact command.

## Install

```bash
git clone https://github.com/yourname/linux-command-assistant
cd linux-command-assistant
pip install .
```

## Use

```bash
linux-help ask "How do I check disk usage?"
```

Output:
```
df -h
```

## Build

```
uv build
```

## Install

Use pipx

```
pipx install dist/linux_command_assistant-0.1.0-py3-none-any.whl
```

## Run

Create an alias for `ask`

```
alias ask='function _ask() { ~/.local/bin/linux-help ask "$*"; }; _ask'
```
