import os
import time
import shutil


# Set working directory
directory = "C:/Users/smrit/Downloads"
os.chdir(directory)

def getDownloads():
    files = filter(os.path.isfile, os.listdir())
    files = [os.path.join(f) for f in files]
    files.sort(key=lambda x: os.path.getmtime(x))
    return files

og = getDownloads()[-1]

while True:
    time.sleep(5)
    new = getDownloads()[-1]
    if (og != new):
        if (new.startswith("M3 tables")):
            os.rename(f"{directory}/{new}", f"{directory}/table.csv")
            os.remove("C:/Users/smrit/PycharmProjects/M3/cities/table.csv")
            shutil.move(f"{directory}/table.csv", f"C:/Users/smrit/PycharmProjects/M3/cities/table.csv")
            print(f"tables.csv has been updated")

