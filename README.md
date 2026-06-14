# 🗂️ Auto File Organizer

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Ko-fi](https://img.shields.io/badge/Support-Ko--fi-FF5E5B?logo=ko-fi)](https://ko-fi.com/khoirulaziz)

A simple Python script that automatically sorts files in any folder into tidy subfolders — by type, extension, or date. No more messy Downloads folder.

---

## ✨ Features

- **Zero dependencies** — uses Python standard library only
- **Customizable rules** — edit `organizer/rules.py` to add your own file types
- **Dry-run mode** — preview changes before applying them
- **Undo support** — saves a JSON log so you can reverse the sort
- **Cross-platform** — works on Windows, macOS, and Linux

---

## 🚀 Getting Started

```bash
# 1. Clone the repo
git clone https://github.com/khoirdev/auto-file-organizer.git
cd auto-file-organizer

# 2. Preview what will happen (no files are moved)
python main.py ~/Downloads --dry-run

# 3. Organize for real
python main.py ~/Downloads

# 4. Made a mistake? Undo it
python main.py ~/Downloads --undo
```

---

## 📂 How It Works

Files are matched to categories by their extension:

| Category    | Extensions                                      |
|-------------|-------------------------------------------------|
| Images      | `.jpg` `.jpeg` `.png` `.gif` `.webp` `.svg` ... |
| Documents   | `.pdf` `.docx` `.txt` `.xlsx` `.csv` ...        |
| Videos      | `.mp4` `.mov` `.avi` `.mkv` ...                 |
| Music       | `.mp3` `.wav` `.flac` `.aac` ...                |
| Archives    | `.zip` `.tar` `.gz` `.rar` `.7z` ...            |
| Code        | `.py` `.js` `.html` `.css` `.json` ...          |
| Others      | Everything else                                 |

You can fully customize these in `organizer/rules.py`.

---

## 🗺️ Roadmap

- [ ] GUI version with Tkinter
- [ ] Watch mode (auto-sort on file creation)
- [ ] Sort by date (Year/Month subfolders)
- [ ] Config file support (`.organizer.yaml`)

---

## 🧪 Running Tests

```bash
python -m unittest discover tests
```

---

## 🤝 Contributing

Pull requests are welcome! Please open an issue first to discuss what you'd like to change. All experience levels welcome.

---

## ☕ Support

If this project saved you time, consider buying me a coffee!

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/khoirulaziz)

---

## ⚖️ License

MIT © khoirdev
