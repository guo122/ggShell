import os
import time

# cache目录
cachePath = os.getenv("HOME") + "/.zTime/"
if not os.path.exists(cachePath):
    os.makedirs(cachePath)
lastFile = cachePath + "lastFile"
dataFile = cachePath + "data"

# 初始化变量
isOpened = False
i = 0

# 补last
try:
    list1 = []
    with open(lastFile) as f:
        for line in f:
            list1.append(line)

    if len(list1) == 2:
        if list1[1] == "True":
            with open(dataFile, "a") as f:
                f.write("close:" + list1[0])
except FileNotFoundError:
    print("init")
        
while True:
    # 获得word开启状态
    f = os.popen("tasklist | findstr WINWORD")
    isRun = f.read() != ''

    if not isOpened and isRun:
        with open(dataFile, "a") as f:
            f.write("open:" + str(int(time.time())) + "\n")
        isOpened = True

    if isOpened and not isRun:
        i = i + 1
        with open(dataFile, "a") as f:
            f.write("close:" + str(int(time.time())) + "\n")
        isOpened = False

    with open(lastFile, "w") as f:
        f.write(str(int(time.time())) + "\n")
        f.write(str(isRun))
    
    time.sleep(1)
