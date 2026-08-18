import json
from get_text import check_if_wlclipboard_is_present, get_marked_text, get_language_from_text
from piper_run_me import check_if_aplay_is_present,text_to_speech_language

def main():
    if not check_if_wlclipboard_is_present() and not check_if_aplay_is_present():
        exit(-1)

    with open("config.json","r")as f:
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

    text_to_speech_language(f"voices/{lang}/{config["languages"][lang]["file"]}",text,config["spoken_speed"])

main()