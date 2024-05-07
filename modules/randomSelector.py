import os
import random
from modules.appData import getAppDataLocalPath
from modules.printAndLog import printAndLog

def randomSelector():
    dir = getAppDataLocalPath() / "signatures/points"

    signFile = [file for file in os.listdir(dir) if file.startswith("sign")]

    if signFile:
        chosenFile = random.choice(signFile)
        completeDir = os.path.join(dir, chosenFile)
        printAndLog("chosen file :" + completeDir)
    else:
        printAndLog("no .sign file found")

    return completeDir