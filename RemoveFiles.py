import time
import os
import shutil

days = 30
path = "\C:\Users\Mady Westerhouse\Music\Random"
seconds = time.time(days)

isExist = os.path.exists(path)

if isExist == true:
    os.walk(path)
else:
    print("Not Found")

os.path.join(path, '\Random')

ctime = os.stat(path).st_ctime
return ctime

if seconds >= ctime:
    if os.path.isdir(path):
        os.remove(path)
    else:
        shutil.rmtree()