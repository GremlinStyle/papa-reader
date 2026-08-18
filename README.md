# Papa Reader

A simple text-to-speech tool for Linux. Highlight any text on your screen and Papa Reader will read it aloud.

Supports **German**, **English**, and **Spanish** — language is detected automatically.

---

## Installation

See the full step-by-step guide in [docs/Install.md](docs/Install.md).

> **Note:** A simpler single-file installer is coming in a future version.

---

## How to use it

1. **Highlight** any text on your screen (click and drag to select it)
2. Run `bash run.sh` in a Terminal inside the Reader folder
3. The text will be read out loud

That's it. For even easier use, you can set up a keyboard shortcut so you never need to open a Terminal — see [docs/Creating a Shortcut.md](docs/Creating%20a%20Shortcut.md).

---

## Requirements

- Linux with a Wayland desktop
- `wl-clipboard` (for reading highlighted text)
- `pipewire` / `pw-play` (for playing audio)
- Python 3

---

## Changing the default language or speed

Open `config.json` with a text editor. 

- To change the **default language**, find the language you want and add `"primary": true` to it (and remove it from the current primary).
- To change the **reading speed**, adjust the `spoken_speed` number. Higher = faster, lower = slower. `1.0` is normal speed.

**Supported languages:** `de` (German), `en` (English), `es` (Spanish)
