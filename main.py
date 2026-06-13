#!/usr/bin/env python3
# main.py — CLI entry point for Auto File Organizer

import argparse
import sys
from organizer.sorter import organize, undo, save_log


def main():
    parser = argparse.ArgumentParser(
        prog="auto-file-organizer",
        description="🗂️  Automatically organize files in a folder by type.",
    )
    parser.add_argument(
        "folder",
        help="Path to the folder you want to organize (e.g. ~/Downloads)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview what would happen without moving any files",
    )
    parser.add_argument(
        "--undo",
        action="store_true",
        help="Reverse the last organize run",
    )
    parser.add_argument(
        "--no-log",
        action="store_true",
        help="Skip saving the undo log",
    )

    args = parser.parse_args()

    # ── UNDO MODE ──
    if args.undo:
        print(f"\n↩️  Undoing last organize in: {args.folder}\n")
        undo(args.folder)
        return

    # ── ORGANIZE MODE ──
    mode = "DRY RUN — no files will be moved" if args.dry_run else "Organizing files..."
    print(f"\n🗂️  Auto File Organizer")
    print(f"📁 Folder : {args.folder}")
    print(f"⚙️  Mode   : {mode}\n")

    try:
        summary = organize(args.folder, dry_run=args.dry_run)
    except (FileNotFoundError, NotADirectoryError) as e:
        print(f"\n❌ {e}")
        sys.exit(1)

    total = len(summary["moved"])
    errors = len(summary["errors"])

    print(f"\n{'─' * 40}")
    print(f"✅ Done!  {total} file(s) {'would be ' if args.dry_run else ''}moved.", end="")
    if errors:
        print(f"  ⚠️  {errors} error(s).")
    else:
        print()

    if not args.dry_run and not args.no_log and total > 0:
        log_path = save_log(summary, args.folder)
        print(f"📋 Undo log saved → {log_path}")
        print(f"   (run with --undo to reverse)\n")


if __name__ == "__main__":
    main()
