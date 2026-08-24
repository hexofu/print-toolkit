
# Print Tools

**Additional useful output features – multi‑colored text (RGB support) and beautiful animated loading with various presets.**

## Features

- 🎨 Multi‑colored text – 8 standard terminal colors
- 🌈 True RGB support – 16 million colors
- 📊 Beautiful animated visual loading – 8 unique presets
- ⚡ Simple and intuitive API
- 🔧 Zero external dependencies

## Installation

```bash
pip install print-tools
```

## Quick Start

```python
from print_tools_lib_pack import printclr, printrgb, visload, RED

printclr("Hello World!", RED)
printrgb("RGB color", 255, 105, 180)
visload(text="Loading: ", end=30, color=GREEN)
```

## Available Styles

| Style | Symbols |
|-------|---------|
| `default` | — |
| `minusplus` | `-` / `+` |
| `zeroone` | `0` / `1` |
| `blocks` | `░` / `█` |
| `circles` | `○` / `●` |
| `squares` | `□` / `■` |
| `hash` | `.` / `#` |
| `lines` | `\` / `/` |

## License

MIT

## Author

Hexofu
