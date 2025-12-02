import os
import subprocess
import tempfile
import shutil

SOUNDFONT_PATH = r'D:\soundfonts\FluidR3_GM.sf2'

OUTPUT_PATH = 'audio'

def render_midi_to_mp3(midi_file, mp3_file, sr=44100):
    if os.path.isfile(mp3_file):
        return
    with tempfile.TemporaryDirectory() as temp_dir:
        # copy the midi file to avoid file name encoding issues
        midi_file_copy = os.path.join(temp_dir, 'temp.mid')
        shutil.copyfile(midi_file, midi_file_copy)
        wav_file = os.path.join(temp_dir, 'temp.wav')

        command = [
            'fluidsynth',
            '-ni',
            '-F',
            wav_file,
            '-r',
            str(sr),
            SOUNDFONT_PATH,
            midi_file_copy
        ]

        subprocess.run(command, check=True)

        # Convert WAV to MP3 using ffmpeg
        command_ffmpeg = [
            r'C:\Program Files\ffmpeg\bin\ffmpeg.exe',
            '-y',  # Overwrite output files without asking
            '-i', wav_file,
            '-codec:a', 'libmp3lame',
            '-b:a', '192k',
            '-filter:a', 'volume=20dB',
            mp3_file
        ]
        subprocess.run(command_ffmpeg, check=True)


def render_all_sheetsage2():
    midi_path = r'../llama_music/temp/transcriptions2'
    for suffix in ['fullband', 'vocal']:
        output_folder = os.path.join(OUTPUT_PATH, 'sheetsage2_V0.2_' + suffix)
        os.makedirs(output_folder, exist_ok=True)
        for file in os.listdir(midi_path):
            if file.endswith(f'_{suffix}.mid'):
                render_midi_to_mp3(os.path.join(midi_path, file), os.path.join(output_folder, file.replace(f'_{suffix}.mid', '.mp3')))

def render_all_sheetsage():
    midi_path = r'../llama_music/temp/sheetsage_demo'
    output_folder = os.path.join(OUTPUT_PATH, 'sheetsage1')
    os.makedirs(output_folder, exist_ok=True)
    for file in os.listdir(midi_path):
        if file.endswith(f'.mp3.mid'):
            render_midi_to_mp3(os.path.join(midi_path, file), os.path.join(output_folder, file.replace(f'.mp3.mid', '.mp3')))

if __name__ == '__main__':
    # render_all_sheetsage()
    render_all_sheetsage2()