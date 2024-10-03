import os
import random
import time
import subprocess
import platform

# For debugging purposes, declaring RANDOM_AUDIO_PLAYER_FOLDER
# os.environ['RANDOM_AUDIO_PLAYER_FOLDER'] = os.path.expanduser('~/Downloads/mp3')

# Configuration
default_folder = os.path.join(os.getcwd(), 'audio')
audio_folder = os.getenv('RANDOM_AUDIO_PLAYER_FOLDER', default_folder)
played_files_log = 'played_files.txt'
default_interval = 300  # 5 minutes in seconds
interval = os.getenv('RANDOM_AUDIO_PLAYER_INTERVAL', default_interval)

# Get list of audio files
audio_files = [f for f in os.listdir(audio_folder) if f.endswith(('.mp3', '.wav'))]

while True:
    # Pick a random file
    file_to_play = random.choice(audio_files)
    file_path = os.path.join(audio_folder, file_to_play)

    # Determine the OS and set the appropriate player command
    system = platform.system().lower()
    if system == 'darwin':  # macOS
        player_command = ['afplay', file_path]
    elif system == 'linux':  # Linux
        player_command = ['aplay', file_path]
    elif system == 'windows':  # Windows
        player_command = ['powershell', '-c', f'(New-Object Media.SoundPlayer "{file_path}").PlaySync();']
    else:
        raise EnvironmentError("Unsupported OS")

    # Play the file
    subprocess.run(player_command)

    # Log the played file
    with open(played_files_log, 'a') as f:
        f.write(file_to_play + '\n')

    # Wait for the interval
    time.sleep(interval)
