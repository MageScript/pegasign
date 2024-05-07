import signal
import subprocess as sp
from modules.signAutoProcess import *
import tkinter as tk
from modules.createSignature import *
from modules.getLastSign import * 
from modules.configuration import *
from modules.randomSelector import *
from modules.runAtStartup import *
import os
import logging
from modules.printAndLog import printAndLog
from modules.appData import *
from modules.processesCheck import checkProcessExists


#check if appData\Local is properly set
appDataCheck()
logFilePath = getAppDataLocalPath() / "pegasign.log"
logging.basicConfig(filename=logFilePath, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("pegasign.exe starting...")

#check if update daemon is properly set
pegasignUpdateProcess = "pegasignUpdate.exe"
if(checkProcessExists(pegasignUpdateProcess) != True):
    try:
        extProc = sp.Popen([pegasignUpdateProcess]) 
        printAndLog("opening " + pegasignUpdateProcess)
    except Exception as e:
        printAndLog(str(e))


def toggleShowGoogle(check):
    try:
        if(check == True):
            changeConfFile("app.conf", "showgoogle", "true")
            printAndLog("enabling showgoogle in app.conf")
        else:
            changeConfFile("app.conf", "showgoogle", "false")
            printAndLog("disabling showgoogle in app.conf")
    except Exception as e:
        printAndLog(str(e)) 

def toggleAutoSign(check):
    try:
        if(check == True):
            extProc = sp.Popen(['autoSignTask.exe']) 
            printAndLog("opening autoSignTask.exe and adding at startup")
            changeConfFile("app.conf", "autosign", "true")
            changeConfFile("app.conf", "processpid", f"{extProc.pid}")
            scriptPath = os.path.realpath(__file__)
            currentPath = os.path.dirname(scriptPath)
            changeDirPlusPath = "cmd.exe /c cd /d \"" + currentPath + "\" && start \"\" \"autoSignTask.exe\""
            addToStartup(changeDirPlusPath, "Pegasign")

        else:
            changeConfFile("app.conf", "autosign", "false")
            pid = getConfigFile("app.conf", "processpid")
            os.kill(int(pid), signal.SIGILL)
            removeFromStartup("Pegasign")
            printAndLog("killing autoSignTask.exe and removing from startup")

    except Exception as e:
        printAndLog(str(e))

def GUIStartup():

    try: 
        # tkinter window
        window = tk.Tk()
        window.title("Pegasign")

        width = 350
        height = 350
        window.geometry(f"{width}x{height}")

        # window updating
        window.update_idletasks()

        # get screen size
        width_screen = window.winfo_screenwidth()
        hauteur_screen = window.winfo_screenheight()

        # add ico to window
        iconPath = "media/pegasign.ico"
        window.iconbitmap(iconPath)

        # center the window
        x = (width_screen - width) // 2
        y = (hauteur_screen - height) // 2
        window.geometry(f"{width}x{height}+{x}+{y}")

        # add components
        label = tk.Label(window, text="configure the signing")
        label.pack()

        button = tk.Button(window, text="create new signature", command=lambda: createSignature(f"sign{getLastSign()+1}", window))
        button.pack()

        signManually = tk.Button(window, text="run signing", 
                            command=lambda: signAutoProcess(showGoogle= "true" == getConfigFile("app.conf", "showgoogle"), signaturePath=randomSelector()))
        signManually.pack()

        checkboxState = tk.BooleanVar()
        chekcbox = tk.Checkbutton(window, text="show navigator", variable=checkboxState,
                                    command= lambda: toggleShowGoogle(checkboxState.get()))
        chekcbox.pack()

        enableAutoSign = tk.BooleanVar()
        enableAutoEmarge = tk.Checkbutton(window, text="Activate automated signing", variable=enableAutoSign,
                                    command= lambda: toggleAutoSign(enableAutoSign.get()))
        enableAutoEmarge.pack()

        if(getConfigFile("app.conf", "showgoogle") == "true"):
            checkboxState.set(True)
        elif(getConfigFile("app.conf", "showgoogle") == "false"):
            checkboxState.set(False)
        else: 
            checkboxState.set(False)
            changeConfFile("app.conf", "showgoogle", "false")
            
        if(getConfigFile("app.conf", "autosign") == "true"):
            enableAutoSign.set(True)
        elif(getConfigFile("app.conf", "autosign") == "false"):
            enableAutoSign.set(False)
        else: 
            enableAutoSign.set(False)
            changeConfFile("app.conf", "showgoogle", "false")
    except Exception as e:
        printAndLog(str(e))
            
    try:        
        window.mainloop()
    except Exception as e:
        printAndLog(str(e))

GUIStartup()

