# tests/test_sorter.py

import unittest
import tempfile
from pathlib import Path
from organizer.sorter import organize, get_category


class TestGetCategory(unittest.TestCase):

    def test_image(self):
        self.assertEqual(get_category(Path("photo.jpg")), "Images")

    def test_document(self):
        self.assertEqual(get_category(Path("report.pdf")), "Documents")

    def test_video(self):
        self.assertEqual(get_category(Path("clip.mp4")), "Videos")

    def test_unknown(self):
        self.assertEqual(get_category(Path("weird.xyz")), "Others")

    def test_case_insensitive(self):
        self.assertEqual(get_category(Path("PHOTO.JPG")), "Images")


class TestOrganize(unittest.TestCase):

    def setUp(self):
        # Create a temporary folder with dummy files
        self.tmp = tempfile.mkdtemp()
        for name in ["photo.jpg", "report.pdf", "song.mp3", "video.mp4", "unknown.xyz"]:
            Path(self.tmp, name).write_text("dummy content")

    def test_dry_run_moves_nothing(self):
        summary = organize(self.tmp, dry_run=True)
        # Files should still be in root folder
        remaining = list(Path(self.tmp).glob("*.jpg"))
        self.assertEqual(len(remaining), 1)
        self.assertEqual(len(summary["moved"]), 5)

    def test_organize_moves_files(self):
        summary = organize(self.tmp, dry_run=False)
        self.assertEqual(len(summary["moved"]), 5)
        self.assertTrue((Path(self.tmp) / "Images" / "photo.jpg").exists())
        self.assertTrue((Path(self.tmp) / "Documents" / "report.pdf").exists())
        self.assertTrue((Path(self.tmp) / "Music" / "song.mp3").exists())
        self.assertTrue((Path(self.tmp) / "Others" / "unknown.xyz").exists())

    def test_nonexistent_folder(self):
        with self.assertRaises(FileNotFoundError):
            organize("/this/does/not/exist")


if __name__ == "__main__":
    unittest.main()
