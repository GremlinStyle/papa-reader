import json
from get_text import check_if_wlclipboard_is_present, get_marked_text, get_language_from_text
from piper_run_me import check_if_aplay_is_present,text_to_speech_language
import requests
from pathlib import Path

script_dir=None

def verify_voices():
    global script_dir
    script_dir = Path(__file__).resolve().parent

    with open(script_dir / "config.json") as f:
        config = json.load(f)

    voices_dir = script_dir / "voices"
    voices_dir.mkdir(exist_ok=True)

    for lang, voice in config["languages"].items():
        lang_folder = voices_dir / lang
        lang_folder.mkdir(exist_ok=True)

        onnx_file = lang_folder / voice["file"]
        onnx_json_file = lang_folder / f"{voice['file']}.json"

        if not onnx_file.is_file() and voice["active"]:
            print(f"Missing: {onnx_file}\n\tStarting Download...")
            file_req=requests.get(voice["url"])
            with open(onnx_file,"wb") as f:
                f.write(file_req.content)

        if not onnx_json_file.is_file() and voice["active"]:
            print(f"Missing: {onnx_json_file}\n\tStarting Download...")
            file_req=requests.get(voice["url"]+".json")
            with open(onnx_json_file,"wb") as f:
                f.write(file_req.content)

    
def main():
    global script_dir

    if not check_if_wlclipboard_is_present() and not check_if_aplay_is_present():
        exit(-1)

    with open(f"{script_dir}/config.json","r")as f:
        config = json.load(f)

    default_language = next(
        (
            language
            for language, voice in config["languages"].items()
            if voice.get("primary") is True
        ),
        None,
    )

    text=get_marked_text()
    lang=get_language_from_text(text)

    if lang is None:
        lang=default_language

    text_to_speech_language(f"{script_dir}/voices/{lang}/{config["languages"][lang]["file"]}",text,config["spoken_speed"])

verify_voices()
main()