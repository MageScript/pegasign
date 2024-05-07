import winreg
from modules.printAndLog import printAndLog

def addToStartup(exe_path, name):
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_ALL_ACCESS)
    try:
        winreg.SetValueEx(key, name, 0, winreg.REG_SZ, exe_path)
        printAndLog(f"successfully added {name} to startup")
    except Exception as e:
        printAndLog(f"error adding {name} to startup: {e}")

def removeFromStartup(name):
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_ALL_ACCESS)
    try:
        winreg.DeleteValue(key, name)
        printAndLog(f"successfully removed {name} from startup")
    except Exception as e:
        printAndLog(f"error removing {name} from startup: {e}")