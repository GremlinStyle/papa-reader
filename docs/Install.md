# Installation Guide

> **Coming soon:** A simpler single-file version (.exe / app) is in the works.
> Once it is ready, you will only need to double-click a file to install.
> Until then, please follow the steps below.

---

## What you will need

Before starting, make sure you have:

- A computer running **Linux** with a **Wayland** desktop (most modern Linux desktops use this — if unsure, it is probably fine)
- An internet connection (needed to download voice files the first time)
- About 10–15 minutes

---

## Step 1 — Install system tools

These are small programs the Reader depends on. Open a **Terminal** and copy-paste each line, then press **Enter**.

**On Arch Linux / Manjaro:**
```
sudo pacman -S python wl-clipboard pipewire-audio
```

**On Ubuntu / Debian / Linux Mint:**
```
sudo apt install python3 wl-clipboard pipewire-bin python3-venv
```

**On Fedora:**
```
sudo dnf install python3 wl-clipboard pipewire-utils
```

> When asked for your password, type it and press Enter. The letters will not appear on screen — that is normal.

---

## Step 2 — Download the Reader files

If you received the Reader as a folder (e.g. on a USB drive), copy it somewhere easy to find, like your **Home folder** or your **Desktop**.

If you received a download link, download the file and unzip it to your Desktop.

---

## Step 3 — Run the installer

1. Open a **Terminal**
2. Navigate to the Reader folder. For example, if it is on your Desktop:

```
cd ~/Desktop/papa-reader
```

3. Run the installer:

```
bash install.sh
```

This will set up everything automatically. It may take a minute or two.
When it says **"Installation complete."** you are done.

---

## Step 4 — First launch (voice download)

The first time you run the Reader, it will download the voice files it needs. This only happens once.

```
chmod +x run.sh
bash run.sh
```

> If you see lines like "Starting Download..." — that is normal. Just wait for it to finish.

---

## Make it even easier — keyboard shortcut

Opening a Terminal every time can be inconvenient. You can set up a keyboard shortcut so Papa Reader runs the moment you press a key combination — no Terminal needed. See the guide: [Creating a Shortcut (KDE)](Creating%20a%20Shortcut.md)

---

## You are all set!

From now on, to use the Reader:

1. **Highlight** any text on your screen (click and drag to select it)
2. Open a Terminal in the Reader folder and run:

```
bash run.sh
```

The selected text will be read aloud.

---

## Something went wrong?

| Problem | What to try |
|---|---|
| `wl-clipboard is not installed` | Re-run Step 1 for your Linux version |
| `pw-play is not installed` | Re-run Step 1 for your Linux version |
| `Python 3 is not installed` | Re-run Step 1 for your Linux version |
| `virtual environment not found` | Re-run Step 3 (`bash install.sh`) |
| No sound | Check that your speakers or headphones are connected and the volume is not muted |

If you are still stuck, ask a family member or friend to help, and show them this guide.
