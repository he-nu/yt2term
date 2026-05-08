# yt2term

Stream YouTube videos (or direct video links) as ASCII art directly in the terminal.

![example frame](images/cat_ascii.png)

## Features

- Real-time video to ASCII conversion
- Optional color output
- Adjustable ASCII width
- Optional audio playback via `ffplay`
- Automatic FFmpeg installation prompt when audio is enabled
- ~30 FPS rendering loop

## Requirements

- Python ≥ 3.9
- Tested on Python 3.12

Install dependencies:

```bash
pip install -r requirements.txt
```

## Optional Audio Support

Audio playback uses `ffplay` from FFmpeg.

Audio is completely optional and disabled by default.

If you run with:

```bash
--audio
```

and `ffplay` is not installed, yt2term will prompt you to install FFmpeg automatically.

### Installation Methods

#### Windows

Uses:

```powershell
winget install Gyan.FFmpeg
```

#### macOS

Uses:

```bash
brew install ffmpeg
```

#### Linux

Currently supports:

```bash
sudo apt install -y ffmpeg
```

## Usage

Basic playback:

```bash
python yt2term.py <link>
```

Enable audio:

```bash
python yt2term.py <link> --audio
```

Disable color:

```bash
python yt2term.py <link> --no-color
```

Set ASCII width manually:

```bash
python yt2term.py <link> --width 120
```

Combine options:

```bash
python yt2term.py <link> --audio --width 100 --no-color
```

## Examples

```bash
python yt2term.py "https://www.youtube.com/watch?v=IxX_QHay02M"
```

```bash
python yt2term.py --audio
```

## Notes

- Uses `yt-dlp` to extract direct stream URLs
- Requires internet connection during playback
- Performance depends on terminal speed and CPU
- Audio/video synchronization is approximate
- Audio playback requires FFmpeg

## Exit

Press:

```text
Ctrl+C
```

to stop playback.
