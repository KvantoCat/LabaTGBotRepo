from pathlib import Path
from tkinter import NO
from typing import List

from bot import utils

class Data:
    def __init__(self):
        self.jokes_data_path = utils.get_sulution_dir() / "bot" / "data" / "jokes.txt"
        self.memes_data_path = utils.get_sulution_dir() / "bot" / "data" / "memes"

        self.jokes = []
        self._extensions = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

        self.cat_mem_paths = self.parse_image_paths(self.memes_data_path / "cats")
        self.work_mem_paths = self.parse_image_paths(self.memes_data_path / "work")
        self.it_mem_paths = self.parse_image_paths(self.memes_data_path / "it")

        self.parse_jokes_file()

    def parse_jokes_file(self) -> None:
        self.jokes.clear()
        with open(self.jokes_data_path, "r", encoding="utf-8") as file:
            for line in file:
                new_line = line.strip()
                if new_line != "":
                    self.jokes.append(new_line)

    def parse_image_paths(self, dir_path : Path) -> List[str]:
        paths = []
        for path in dir_path.iterdir():
            if path.is_file() and path.suffix.lower() in self._extensions:
                paths.append(path)

        return paths

bot_data = Data()
