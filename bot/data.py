from pathlib import Path

from bot import utils

class Data:
    def __init__(self):
        self.jokes_data_path = utils.get_sulution_dir() / "bot" / "data" / "jokes.txt"
        self.memes_data_path = utils.get_sulution_dir() / "bot" / "data" / "memes"

        self.jokes = []
        self._extensions = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

        self.cat_mem_paths = []
        self.child_mem_paths = []
        self.work_mem_paths = []

        self.parse_jokes_file()
        self.parse_image_paths(self.memes_data_path / "cats")

    def parse_jokes_file(self):
        self.jokes.clear()
        with open(self.jokes_data_path, "r", encoding="utf-8") as file:
            for line in file:
                new_line = line.strip()
                if new_line != "":
                    self.jokes.append(new_line)

    def parse_image_paths(self, dir_path : Path):
        self.cat_mem_paths.clear()
        for path in dir_path.iterdir():
            if path.is_file() and path.suffix.lower() in self._extensions:
                self.cat_mem_paths.append(path)

bot_data = Data()
