import os
import sys
from datetime import date
from shutil import copyfile

if __name__ == "__main__":
    try:
        day = int(sys.argv[1])
    except Exception:
        day = date.today().day

    day_str = f"{day}".zfill(2)

    if os.path.isdir(day):
        sys.exit("day alreddy exists")

    os.makedirs(day_str)
    dest_path_file_name = os.path.join(day_str, "a.py")
    if not os.path.exists(dest_path_file_name):
        copyfile("base.py", dest_path_file_name)
