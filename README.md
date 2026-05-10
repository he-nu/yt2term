![PyPI version](https://img.shields.io/pypi/v/yt2term)
![Python](https://img.shields.io/pypi/pyversions/yt2term)
![License](https://img.shields.io/github/license/he-nu/yt2term)

![demo](images/oiia.gif)

# yt2term

> Stream YouTube videos (or direct video links) as real-time ASCII art in your terminal.


---

## Entirely impractical. Oddly satisfying.

yt2term turns video into a live terminal experience — frame-by-frame ASCII rendering at ~30 FPS, optionally with audio.

---

<img src="https://img.spacergif.org/spacer.gif" width="1" height="40"/>

## Features

- Real-time video → ASCII conversion  
- Smooth ~30 FPS rendering loop  
- Optional colorized output  
- Adjustable resolution / width scaling  
- Optional audio playback via `ffplay`  
- Automatic FFmpeg detection and guidance  

---

<img src="https://img.spacergif.org/spacer.gif" width="1" height="40"/>

## Installation

### From PyPI (recommended)

```bash
pip install yt2term
```

Run it:

```bash
yt2term
```

---

### Development install

```bash
git clone https://github.com/<your-username>/yt2term.git
cd yt2term

pip install -e .
```

---

### Local install

```bash
pip install .
```

---

<img src="https://img.spacergif.org/spacer.gif" width="1" height="40"/>

## Requirements

- Python ≥ 3.10  
- Tested on Python 3.10–3.12  

---

## Dependencies

Installed automatically:

- `opencv-python`
- `yt-dlp`
- `pillow`
- `asciifyy`

---

<img src="https://img.spacergif.org/spacer.gif" width="1" height="40"/>

## Audio Support

Audio playback uses **FFmpeg (`ffplay`)**.

Disabled by default.

Enable it:

```bash
yt2term <url> --audio
```

If FFmpeg is missing, yt2term will:

- Detect it automatically  
- Explain what’s missing  
- Suggest installation steps  
- Attempt system-package installation (if possible)  

---

<img src="https://img.spacergif.org/spacer.gif" width="1" height="40"/>

## Usage

### Basic playback

```bash
yt2term <youtube-or-video-url>
```

---

### Enable audio

```bash
yt2term <url> --audio
```

---

### Disable color output

```bash
yt2term <url> --no-color
```

---

### Adjust resolution

```bash
yt2term <url> --width 120
```

---

### Combined options

```bash
yt2term <url> --audio --width 100 --no-color
```

---

<img src="https://img.spacergif.org/spacer.gif" width="1" height="40"/>

## Notes

- Streams video via `yt-dlp`
- Requires active internet connection
- Terminal rendering speed affects performance
- Audio/video sync is approximate
- Built for experimentation, not precision playback

---

## Exit

Press:

```text
Ctrl + C
```

to return to reality.

---

<img src="https://img.spacergif.org/spacer.gif" width="1" height="40"/>

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
