from bot import utils

class Data:
    JOKES_DATA_PATH = utils.get_sulution_dir() / "bot" / "data" / "jokes.txt"

    def __init__(self):
        self.jokes_data = []

    def parse_jokes_file(self):
        self.jokes_data.clear()
        with open(self.JOKES_DATA_PATH, "r", encoding="utf-8") as file:
            for line in file:
                new_line = line.strip()
                if new_line != "":
                    self.jokes_data.append(new_line)

bot_data = Data()