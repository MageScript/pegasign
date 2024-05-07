import os
import re
from modules.appData import getAppDataLocalPath
from modules.printAndLog import printAndLog

def getLastSign():

    dir = getAppDataLocalPath() / "signatures/points"

    signFile = [file for file in os.listdir(dir) if re.match(r'sign\d+\..*', file)]

    if signFile:
        signFile.sort(key=lambda x: int(re.search(r'sign(\d+)\..*', x).group(1)))
        maxNumberFile = signFile[-1]
        
        completeDir = os.path.join(dir, maxNumberFile)
        printAndLog("file with biggest number :" + completeDir)
        
        match = re.search(r'sign(\d+)\.sign', completeDir)

        if match:
            number = match.group(1)
            printAndLog("number :" + number)
            return int(number)
        else:
            printAndLog("any number found")
        
    else:
        printAndLog("no file found with this model 'signN.ext'.")
        return 0
        


