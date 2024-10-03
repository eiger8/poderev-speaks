# Random Audio Player

This script plays random audio files from a specified folder at regular intervals. It supports macOS, Windows 11, and Linux. The script logs the names of the played files to a log file.

## Requirements

- Python 3.x
- `afplay` (macOS)
- `aplay` (Linux)
- `powershell` (Windows)

## Configuration

- `audio_folder`: The folder containing the audio files. This is set to `~/Downloads/YouTube/mp3` by default.
- `played_files_log`: The file where the names of the played files will be logged. This is set to `played_files.txt` by default.
- `interval`: The interval in seconds between playing files. This is set to 300 seconds (5 minutes) by default.

## Usage

1. **Clone the repository or download the script:**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Ensure the audio files are in the specified folder:**

    By default, the script looks for audio files in `~/Downloads/YouTube/mp3`. You can change this by modifying the `audio_folder` variable in the script.

3. **Run the script:**

    ```bash
    python3 random_audio_player.py
    ```

## Example

Here is an example of how to run the script:

```bash
python3 random_audio_player.py
```

# Obtain identical functionality utilizing standard BASH. Alternative options.

Execute the random_audio player in the background using the following bash command. To terminate the process, you must manually kill it by its PID, which is provided upon command execution.

```bash
nohup bash -c 'AUDIO_FOLDER=~/Downloads/YouTube; LOG_FILE=~/played_files.log; while true; do file=$(gshuf -e "$AUDIO_FOLDER"/*.* -n 1); echo "$file" >> "$LOG_FILE"; afplay "$file"; sleep 300; done' > /dev/null 2>&1 &
```

Run the random_audio player in the current terminal session. To terminate the process, simply use CTRL+C.

```bash
AUDIO_FOLDER=~/Downloads/YouTube; LOG_FILE=~/played_files.log; while true; do file=$(gshuf -e "$AUDIO_FOLDER"/*.* -n 1); echo "$file" >> "$LOG_FILE"; afplay "$file"; sleep 300; done
```

Please utilize this command if you wish to configure crontab. Be advised that this will disable the "played_files.log" functionality.

```bash
gshuf -e ~/Downloads/YouTube/*.* -n 1 | tr '\n' '\0' | xargs -0 afplay
```