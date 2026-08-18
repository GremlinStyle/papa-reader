# Configuration

All settings are stored in the file `config.json`, which lives in the Papa Reader folder. You can open it with any text editor (e.g. right-click → Open with Text Editor).

---

## Reading speed — `spoken_speed`

Controls how fast the text is read aloud.

```json
"spoken_speed": 1.2
```

| Value | Effect |
|---|---|
| `0.8` | Faster than normal |
| `1.0` | Normal speed |
| `1.5` | Slower |
| `2.0` | Twice as slow |

Lower the number to go faster, increase it to go slower.

---

## Languages — `languages`

Each language has its own entry. Here is what each field means:

```json
"de": {
    "file": "de_DE-thorsten-medium.onnx",
    "url": "https://...",
    "active": true,
    "primary": true
}
```

| Field | What it does |
|---|---|
| `file` | The name of the voice file used for this language |
| `url` | Where the voice file is downloaded from (do not change) |
| `active` | Set to `true` to download and use this language, `false` to skip it |
| `primary` | Marks this as the fallback language when the text language cannot be detected |

### Disabling a language

If you only ever read text in one language and want to skip downloading the others, set `"active": false` for the languages you do not need:

```json
"en": {
    "file": "en_GB-alan-medium.onnx",
    "url": "...",
    "active": false
}
```

> Voice files that are already downloaded will not be re-downloaded, but they will not be used if `active` is `false`.

### Changing the default (fallback) language

The language marked `"primary": true` is used when Papa Reader cannot automatically detect the language of the highlighted text.

**Important:** Only one language should have `"primary": true` at a time. If you change it, make sure to remove `"primary": true` from the old one first.

**Example — switching the default from German to English:**

Before:
```json
"de": { ..., "primary": true },
"en": { ... }
```

After:
```json
"de": { ... },
"en": { ..., "primary": true }
```

### Adding more languages

You can add any language from the [Piper voices library](https://huggingface.co/rhasspy/piper-voices/tree/main). Each language uses one voice.

1. Browse to the link above and find a language you want to add
2. Click into its folder until you see a file ending in `.onnx` — pick one voice for that language
3. Click the file, then copy the URL from your browser's address bar — but replace `/blob/` with `/resolve/` in the URL
4. Add a new entry to `config.json` following this pattern:

```json
"fr": {
    "file": "fr_FR-upmc-medium.onnx",
    "url": "https://huggingface.co/rhasspy/piper-voices/resolve/main/fr/fr_FR/upmc/medium/fr_FR-upmc-medium.onnx",
    "active": true
}
```

The two-letter key (`"fr"`, `"de"`, `"en"`, etc.) must match the language's ISO code — this is how Papa Reader knows which voice to use when it detects the language of your text.

The voice file will be downloaded automatically the next time you run Papa Reader.

---

## Full example

```json
{
  "languages": {
    "de": {
      "file": "de_DE-thorsten-medium.onnx",
      "url": "https://huggingface.co/rhasspy/piper-voices/resolve/main/de/de_DE/thorsten/medium/de_DE-thorsten-medium.onnx",
      "active": true,
      "primary": true
    },
    "en": {
      "file": "en_GB-alan-medium.onnx",
      "url": "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_GB/alan/medium/en_GB-alan-medium.onnx",
      "active": true
    },
    "es": {
      "file": "es_ES-davefx-medium.onnx",
      "url": "https://huggingface.co/rhasspy/piper-voices/resolve/main/es/es_ES/davefx/medium/es_ES-davefx-medium.onnx",
      "active": true
    }
  },
  "spoken_speed": 1.2
}
```
