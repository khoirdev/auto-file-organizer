# organizer/sorter.py

import os
import shutil
import json
from pathlib import Path
from datetime import datetime
from organizer.rules import RULES


def get_category(file_path: Path) -> str:
    """Return the category folder name for a given file."""
    ext = file_path.suffix.lower()
    for category, extensions in RULES.items():
        if ext in extensions:
            return category
    return "Others"


def organize(folder: str, dry_run: bool = False) -> dict:
    """
    Organize all files in `folder` into subfolders by type.

    Args:
        folder:  Path to the folder you want to organize.
        dry_run: If True, only print what would happen without moving anything.

    Returns:
        A summary dict with moved files and any errors.
    """
    folder_path = Path(folder).expanduser().resolve()

    if not folder_path.exists():
        raise FileNotFoundError(f"Folder not found: {folder_path}")
    if not folder_path.is_dir():
        raise NotADirectoryError(f"Not a directory: {folder_path}")

    summary = {
        "folder": str(folder_path),
        "dry_run": dry_run,
        "timestamp": datetime.now().isoformat(),
        "moved": [],
        "skipped": [],
        "errors": [],
    }

    files = [f for f in folder_path.iterdir() if f.is_file()]

    if not files:
        print("📂 No files found to organize.")
        return summary

    for file in files:
        category = get_category(file)
        dest_dir = folder_path / category
        dest_file = dest_dir / file.name

        # Avoid overwriting existing files — append a number suffix
        if dest_file.exists():
            stem = file.stem
            suffix = file.suffix
            counter = 1
            while dest_file.exists():
                dest_file = dest_dir / f"{stem}_{counter}{suffix}"
                counter += 1

        if dry_run:
            print(f"  [DRY RUN] Would move: {file.name}  →  {category}/")
            summary["moved"].append({"file": file.name, "to": category})
        else:
            try:
                dest_dir.mkdir(exist_ok=True)
                shutil.move(str(file), str(dest_file))
                print(f"  ✅ Moved: {file.name}  →  {category}/")
                summary["moved"].append({"file": file.name, "to": category, "dest": str(dest_file)})
            except Exception as e:
                print(f"  ❌ Error moving {file.name}: {e}")
                summary["errors"].append({"file": file.name, "error": str(e)})

    return summary


def save_log(summary: dict, folder: str) -> str:
    """Save a JSON log of what was moved so you can undo later."""
    log_path = Path(folder) / ".organizer_log.json"
    with open(log_path, "w") as f:
        json.dump(summary, f, indent=2)
    return str(log_path)


def undo(folder: str) -> None:
    """Reverse the last organize() run using the saved log."""
    log_path = Path(folder).expanduser().resolve() / ".organizer_log.json"

    if not log_path.exists():
        print("⚠️  No undo log found. Run organize() first.")
        return

    with open(log_path) as f:
        summary = json.load(f)

    if summary.get("dry_run"):
        print("⚠️  Last run was a dry run. Nothing to undo.")
        return

    for entry in summary.get("moved", []):
        dest = Path(entry["dest"])
        original = Path(summary["folder"]) / entry["file"]
        if dest.exists():
            shutil.move(str(dest), str(original))
            print(f"  ↩️  Restored: {entry['file']}")
        else:
            print(f"  ⚠️  File not found, skipping: {dest}")

    log_path.unlink()
    print("\n✅ Undo complete!")
