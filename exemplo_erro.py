import os
from pathlib import Path

os.mkdir("dest")
original = Path("./original.txt")
original.write_text("config de nvim")
print("teto: ", original.read_text())
Path("./dest/linked.txt").symlink_to(original)
dest_config = Path("~/.config/linked.txt")
dest_config.symlink_to(original)
print(dest_config.read_text())
