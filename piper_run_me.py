from piper import PiperVoice, SynthesisConfig
import wave, subprocess, os
import shutil

def check_if_aplay_is_present():
    if not shutil.which("aplay"):
        print("ERROR")
        print("aplay is not installed")
        print("Arch Linux: sudo pacman -S alsa-utils")
        print("Debian/Ubuntu: sudo apt install alsa-utils")
        return False
    return True

def text_to_speech_language(language_onnx_file,text_to_speech,speed=1.5):
        test_file_name="/tmp/temp_file.wav"
        voice = PiperVoice.load(language_onnx_file)

        syn_config = SynthesisConfig(
            length_scale=speed,
        )

        with wave.open(test_file_name, "wb") as wav_file:
            voice.synthesize_wav(text_to_speech, wav_file,syn_config=syn_config)

        subprocess.run(["aplay", test_file_name], check=True)
        os.remove(test_file_name)