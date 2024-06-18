from os import listdir, utime
from os.path import isfile, join
from datetime import datetime

def parse_file(folder, file):
    Y = file[0:4]
    M = file[4:6]
    D = file[6:8]
    h = file[8:10]
    m = file[10:12]
    s = file[12:14]

    iso_date = f"{Y}-{M}-{D} {h}:{m}:{s}"

    dateandtime = datetime.strptime(iso_date, "%Y-%m-%d %H:%M:%S")

    print(dateandtime)
    
    timestamp = dateandtime.timestamp()

    full_path = join(folder, file)
    utime(full_path, (timestamp, timestamp))

def iterate_folder(folder):
    print(f"\nScanning {folder}")
    for f in listdir(folder):
        print(f"- {f}")
        if isfile(join(folder, f)):
            parse_file(folder, f)
        else:
            iterate_folder(join(folder, f))


path = input("Album's path: ")
iterate_folder(path)
print("\n- Done -")