# yt2term

`yt2term` streams YouTube videos (or direct video links) as real-time ASCII art directly inside your terminal.

## Entirely impractical - Weirdly meaningful

---

![example frame](images/cat_ascii.png)

---

## Features

- Real-time video → ASCII conversion
- ~30 FPS rendering loop
- Optional color rendering
- Adjustable output width
- Optional audio playback via `ffplay`
- Automatic FFmpeg detection

---

## Installation

### Install from PyPI (recommended)

```bash
pip install yt2term
```

This installs the CLI command:

```bash
yt2term
```

---

### Development install

For contributors or local development:

```bash
git clone https://github.com/<your-username>/yt2term.git
cd yt2term

pip install -e .
```

---

### Alternative install

You can also install directly from source:

```bash
pip install .
```

---

## Python Version

- Requires Python ≥ 3.10
- Tested on Python 3.10+ / 3.12

---

## Dependencies

Installed automatically via `pyproject.toml`:

- `opencv-python`
- `yt-dlp`
- `pillow`
- `asciifyy`

---

## Audio Support

Audio playback uses `ffplay` from FFmpeg.

Audio is disabled by default.

Enable it with:

```bash
yt2term <link> --audio
```

If FFmpeg is missing, the application will:

1. Detect it automatically
2. Explain what is missing
3. Prompt installation
4. Attempt installation using the system package manager

---

## Usage

### Basic playback

```bash
yt2term <youtube-or-video-url>
```

### Enable audio

```bash
yt2term <url> --audio
```

### Disable color output

```bash
yt2term <url> --no-color
```

### Set ASCII width

```bash
yt2term <url> --width 120
```

### Combined options

```bash
yt2term <url> --audio --width 100 --no-color
```

---

## Notes

- Uses `yt-dlp` to resolve streaming URLs
- Requires an internet connection during playback
- Performance depends heavily on terminal rendering speed
- Audio/video sync is approximate
- Designed for fun, experimentation, and terminal abuse

---

## Exit

Press `Ctrl+C` to stop playback and return to reality.

---

## Project Structure

```text
yt2term/
├── src/
│   └── yt2term/
│       ├── main.py
│       ├── cli.py
│       ├── video.py
│       ├── audio.py
│       ├── render.py
```

---

## License

MIT
