# This script will grab any of our downloaded google sheets and automatically import them into our Python project so we can more easily collaborate.

# Module imports
import os
import time
import shutil
import getpass


# Set working directory
currentwd = os.getcwd().replace('\\', '/')
directory = f"C:/Users/{getpass.getuser()}/Downloads"
os.chdir(directory)

# Get downloads sorted by modified date
def getDownloads():
    files = filter(os.path.isfile, os.listdir())
    files = [os.path.join(f) for f in files]
    files.sort(key=lambda x: os.path.getmtime(x))
    return files

# Get the name of the latest file
og = getDownloads()[-1]

while True:
    # Wait for 5 seconds to decrease overhead
    time.sleep(5)
    new = getDownloads()[-1]
    # If new file exists
    if (og != new):
        # If the new file starts with M3 tables (the name of our Google sheet)
        if (new.startswith("M3 tables")):
            # Import it into our project
            os.rename(f"{directory}/{new}", f"{directory}/table.csv")
            os.remove(f"{currentwd}/cities/table.csv")
            shutil.move(f"{directory}/table.csv", f"{currentwd}/cities/table.csv")
            print(f"tables.csv has been updated")

