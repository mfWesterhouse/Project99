import time
import os
import shutil
import random

days = 30
path = "C:/Users/Mady Westerhouse/Music/Random"
number_days = days
number_days = time.time()

isExist = os.path.exists(path)

if isExist == True:
    os.walk(path)
else:
    print("File not found")

os.path.join(path, '\Random')

def time():
    ctime = os.stat(path).st_ctime

    if number_days > ctime :
        if os.path.isdir(path) == True:
            os.remove(path)
        else: 
            shutil.rmtree()
    elif number_days == ctime():
        if os.path.isdir(path) == True:
            os.remove(path)
        else:
            shutil.rmtree()
    else:
        print("File not found")
time()
