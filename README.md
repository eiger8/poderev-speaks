Всі знають митця [Леся Подервʼянського](https://uk.wikipedia.org/wiki/Лесь_Подерв%27янський). Хтось за його художню діяльність, інші за драматургію. Та найширше він відомий як письменник автор пʼєс із міцним слівцем та добіса влучним гумором. Якось я подумав що було б класно, для підняття настрою, у випадковий момент в навушниках чути випадкову цитату із пʼєс митця. Власне, цей скрипт створений для такої задачі. Він відтворює з певним інтервалом цитату з аудіо файла. Самі цитати знаходяться в директорії `./audio`, перекодовані з YouTube каналу "Подерв'янський — цитати".

Нижче трохи документації щоб краще розуміти що, як і до чого.

# Random Audio Player - poderev-speaks

This script plays random audio files from a specified folder at regular intervals. It supports macOS, Windows 11, and Linux. The script logs the names of the played files to a log file.

## Source of Audio Files

The audio files used by this script are sourced from the [YouTube channel "Подерв'янський — цитати"](https://www.youtube.com/channel/UCz3N3U8VRHOPTkwlFx68jig). Please ensure you have downloaded the audio files into the specified folder.

## Requirements

- Python 3.x
- `afplay` (macOS)
- `aplay` (Linux)
- `powershell` (Windows)

## Configuration
By deafault script will play audio from `./audio` in current working dir
This behaviour can be customized using the following environment variables:

- `RANDOM_AUDIO_PLAYER_FOLDER`: The folder containing the audio files. If not set, the script defaults to using the `audio` folder located in the current working directory.
- `RANDOM_AUDIO_PLAYER_INTERVAL`: The interval in seconds between playing files. If not set, the script defaults to 300 seconds (5 minutes).

EXAMPLE:

```bash
export RANDOM_AUDIO_PLAYER_FOLDER=~/YOUR_AUDIO_FOLDER
export RANDOM_AUDIO_PLAYER_INTERVAL=600
```

## Usage

1. **Clone the repository or download the script:**

    ```bash
    git clone git@github.com:eiger8/poderev-speaks.git
    cd poderev-speaks
    ```

2. **Ensure the audio files are in the specified folder:**

    By default, the script looks for audio files in `./audio`. You can change this by modifying the `RANDOM_AUDIO_PLAYER_FOLDER` variable in the script.

3. **Run the script:**

    ```bash
    python3 poderev-speaks.py
    ```


# Obtain identical functionality utilizing standard BASH. Alternative options.

Execute the random_audio player in the background using the following bash command. To terminate the process, you must manually kill it by its PID, which is provided upon command execution.

```bash
nohup bash -c 'AUDIO_FOLDER=~/path/to-audio; LOG_FILE=~/played_files.log; while true; do file=$(gshuf -e "$AUDIO_FOLDER"/*.* -n 1); echo "$file" >> "$LOG_FILE"; afplay "$file"; sleep 300; done' > /dev/null 2>&1 &
```

Run the random_audio player in the current terminal session. To terminate the process, simply use CTRL+C.

```bash
AUDIO_FOLDER=~/path/to-audio; LOG_FILE=~/played_files.log; while true; do file=$(gshuf -e "$AUDIO_FOLDER"/*.* -n 1); echo "$file" >> "$LOG_FILE"; afplay "$file"; sleep 300; done
```

Please utilize this command if you wish to configure crontab. Be advised that this will disable the "played_files.log" functionality.

```bash
gshuf -e ~/path/to-audio/*.* -n 1 | tr '\n' '\0' | xargs -0 afplay
```