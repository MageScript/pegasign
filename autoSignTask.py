from modules.readSignature import *
import time
from modules.configuration import * 
from modules.getDateTime import * 
import datetime
from modules.randomSelector import *
from win11toast import toast
from modules.signAutoProcess import *
import threading
import pystray
import PIL.Image
import logging
from modules.printAndLog import printAndLog
import logging
from modules.notif import notify
from modules.appData import getAppDataLocalPath


logFilePath = getAppDataLocalPath() / "pegasign.log"
logging.basicConfig(filename=logFilePath, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("autoSignTask.exe starting...")

def sysTrayAppActive():

    try:
        image = PIL.Image.open("media/pegasign.ico")

        # create icon on system tray
        icon = pystray.Icon('Pegasign', icon=image)

        # exit handling
        def exitAction(icon, item):
            icon.stop()  # remove icon from system tray

        # configure the menu
        icon.menu = pystray.Menu(
            pystray.MenuItem('Exit', exitAction)
        )

        # run system tray icon
        icon.run()

    except Exception as e:
        printAndLog(str(e))


def autoSignTask():

    try:

        while(True):

            sign1time1 = datetime.time(8, 31)
            sign1time2 = datetime.time(9, 15)

            sign2time1 = datetime.time(10, 31)
            sign2time2 = datetime.time(11, 15)

            sign3time1 = datetime.time(13, 46)
            sign3time2 = datetime.time(14, 30)

            sign4time1 = datetime.time(15, 46)
            sign4time2 = datetime.time(16, 30)

            if(getConfigFile("app.conf", "currentday") != getDay()):
                changeConfFile("app.conf", "1sign", "false")
                changeConfFile("app.conf", "2sign", "false")
                changeConfFile("app.conf", "3sign", "false")
                changeConfFile("app.conf", "4sign", "false")
                printAndLog("day changed")            

            currentDatetime = datetime.datetime.now().time()

            if(
                (sign1time1 <= currentDatetime <= sign1time2)
                and
                (getDay() != "Saturday" or getDay() != "Sunday")
                and
                (getConfigFile("app.conf", "1sign") == "false")
            ):
                if(signAutoProcess(showGoogle= "true" == getConfigFile("app.conf", "showgoogle"), signaturePath=randomSelector())):
                    changeConfFile("app.conf", "1sign", "true")
                    notify("Signing succed", "The automated signature was successful")
                
                
                
            if(
                (sign2time1 <= currentDatetime <= sign2time2)
                and
                (getDay() != "Saturday" or getDay() != "Sunday")
                and
                (getConfigFile("app.conf", "2sign") == "false")
            ):
                if(signAutoProcess(showGoogle= "true" == getConfigFile("app.conf", "showgoogle"), signaturePath=randomSelector())):
                    changeConfFile("app.conf", "2sign", "true")
                    notify("Signing succed", "The automated signature was successful")
                
                
                
                
                
            if(
                (sign3time1 <= currentDatetime <= sign3time2)
                and
                (getDay() != "Saturday" or getDay() != "Sunday")
                and
                (getConfigFile("app.conf", "3sign") == "false")
            ):
                if(signAutoProcess(showGoogle= "true" == getConfigFile("app.conf", "showgoogle"), signaturePath=randomSelector())):
                    changeConfFile("app.conf", "3sign", "true")
                    notify("Signing succed", "The automated signature was successful")
                
                
                
            if(
                (sign4time1 <= currentDatetime <= sign4time2)
                and
                (getDay() != "Saturday" or getDay() != "Sunday")
                and
                (getConfigFile("app.conf", "4sign") == "false")
            ):
                if(signAutoProcess(showGoogle= "true" == getConfigFile("app.conf", "showgoogle"), signaturePath=randomSelector())):
                    changeConfFile("app.conf", "4sign", "true")
                    notify("Signing succed", "The automated signature was successful")
                    
                    
            changeConfFile("app.conf", "currentday", getDay())

            printAndLog("autoSignTask.exe running...")

            time.sleep(1)

    except Exception as e:
        printAndLog("Error: ", str(e))


signTask = threading.Thread(target=autoSignTask)
sysTray = threading.Thread(target=sysTrayAppActive)

signTask.start()
sysTray.start()

signTask.join()
sysTray.join()