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

## Step 2 — Download Papa Reader

Choose whichever option is easier for you:

---

### Option A — Download as a ZIP file (easiest)

1. Click this link to download: [Download papa-reader.zip](https://github.com/GremlinStyle/papa-reader/archive/refs/heads/master.zip)
2. Open your **Downloads** folder
3. Right-click the file **papa-reader-master.zip** and choose **Extract Here** (or "Extract to this folder")
4. You will now have a folder called **papa-reader-master** in your Downloads

---

### Option B — Using Git (for those who know it)

Open a Terminal and run:

```
git clone https://github.com/GremlinStyle/papa-reader.git
cd papa-reader
```

The folder is now ready — skip to Step 3.

---

## Step 3 — Run the installer

1. Open a **Terminal**
2. Navigate to the Papa Reader folder. If you used Option A, run:

```
cd ~/Downloads/papa-reader-master
```

If you used Option B (git clone), run:

```
cd papa-reader
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
