import os
import sys
from datetime import date
from shutil import copyfile

if __name__ == "__main__":
    try:
        day = sys.argv[1]
    except Exception:
        day = date.today().day
        if day < 10:
            day = f"0{day}"

    if os.path.isdir(day):
        sys.exit("day alreddy exists")

    os.makedirs(day)
    copyfile("base.py", os.path.join(day, "a.py"))
