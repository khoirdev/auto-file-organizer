# organizer/rules.py
# Add or edit categories and extensions as you like!

RULES = {
    "Images":     [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".bmp", ".tiff", ".ico"],
    "Documents":  [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".pptx", ".csv", ".md", ".odt"],
    "Videos":     [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv", ".webm"],
    "Music":      [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
    "Archives":   [".zip", ".tar", ".gz", ".rar", ".7z", ".bz2"],
    "Code":       [".py", ".js", ".ts", ".html", ".css", ".json", ".xml", ".sh", ".java", ".cpp", ".c"],
    "Executables":[".exe", ".msi", ".dmg", ".pkg", ".deb", ".apk"],
    "Others":     [],  # Catch-all for unrecognized extensions
}
