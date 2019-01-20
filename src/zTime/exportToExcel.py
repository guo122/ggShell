import os
import xlwt
import time

# 定义函数
def formatDouble(a):
    if a < 10:
        return "0" + str(a)
    else:
        return str(a)

def formatDur(a):
    tmpHour = int(int(a) / 3600)
    lastSec = int(int(a) % 3600)
    tmpMin = int(lastSec / 60)
    lastSec = int(int(a) % 60)

    tmpStr = ""
    if tmpHour != 0:
        tmpStr = str(tmpHour) + "小时"
    if tmpMin != 0:
        tmpStr += formatDouble(tmpMin) + "分"
    if lastSec != 0:
        tmpStr += formatDouble(lastSec) + "秒"
    return tmpStr
    
def formatTimePrint(curTime):
    timeStruct = time.localtime(int(curTime))
    tmpStr = str(timeStruct.tm_year) + "/" + str(timeStruct.tm_mon) + "/" + str(timeStruct.tm_mday) + " " + str(timeStruct.tm_hour) + ":" + formatDouble(timeStruct.tm_min) + ":" + formatDouble(timeStruct.tm_sec)
    return tmpStr

# 检测目录是否存在
cachePath = os.getenv("HOME") + "/.zTime/"
if os.path.exists(cachePath):
    lastFile = cachePath + "lastFile"
    dataFile = cachePath + "data"

    list1 = []
    list2 = []

    # 读取记录
    try:
        with open(lastFile) as f:
            for line in f:
                list1.append(line)
        with open(dataFile) as f:
            for line in f:
                list2.append(line)

        # 生成Excel表格
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet("sheet1")
        sheet.write(0, 0, "序号")
        sheet.write(0, 1, "打开时间")
        sheet.write(0, 2, "关闭时间")
        sheet.write(0, 3, "使用时长(秒)")

        sheet.col(1).width = 5120
        sheet.col(2).width = 5120

        i = 0
        lastTime = 0
        
        for x in list2:
            tmpList = x.split(":")

            # 解析数据
            if len(tmpList) == 2:
                # 写入开启时间
                if tmpList[0] == "open":
                    i = i + 1
                    lastTime = int(tmpList[1])
                    sheet.write(i, 0, str(i))
                    sheet.write(i, 1, formatTimePrint(tmpList[1]))
                else:
                    sheet.write(i, 2, formatTimePrint(tmpList[1]))
                    sheet.write(i, 3, formatDur(int(tmpList[1]) - lastTime))

        # 补last
        if len(list1) == 2:
            if list1[1] == "True":
                sheet.write(i, 2, formatTimePrint(list1[0]))
                sheet.write(i, 3, formatDur(int(list1[0]) - lastTime))
                
        wbk.save('output.xls')
        
    except FileNotFoundError:
        print("data error")




