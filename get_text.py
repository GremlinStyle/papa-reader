import subprocess
import shutil
from lingua import LanguageDetectorBuilder

def check_if_wlclipboard_is_present():
    if not shutil.which("wl-paste"):
        print("ERROR")
        print("wl-clipboard is not installed")
        print("Arch Linux: sudo pacman -S wl-clipboard")
        print("Debian/Ubuntu: sudo apt install wl-clipboard")
        return False
    return True

def get_marked_text():
    text = subprocess.check_output(["wl-paste", "-p"],text=True,).strip()
    return text

def get_language_from_text(text):
    detector = LanguageDetectorBuilder.from_all_languages().build()

    language = detector.detect_language_of(text)
    if language is None:
        print("Could not determine language")
        return None
    return language.iso_code_639_1.name.lower()