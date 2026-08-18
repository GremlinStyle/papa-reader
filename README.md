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

Run it again while it is already reading to **stop the audio immediately**.

For the best experience, set up a keyboard shortcut — one key press to start reading, the same key again to stop. See [docs/Creating a Shortcut.md](docs/Creating%20a%20Shortcut.md).

---

## Requirements

- Linux with a Wayland desktop
- `wl-clipboard` (for reading highlighted text)
- `pipewire` / `pw-play` (for playing audio)
- Python 3

---

## Configuration

You can change the reading speed, the default language, and which languages are downloaded. See the full guide: [docs/Configuration.md](docs/Configuration.md)

**Supported languages:** `de` (German), `en` (English), `es` (Spanish)
