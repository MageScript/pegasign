import configparser
from modules.appData import getAppDataLocalPath

def changeConfFile(sections, attribute, value):
    dir = getAppDataLocalPath() / "app.conf"
    config = configparser.ConfigParser()
    config.read(dir)
    config[sections][attribute] = value
    with open(dir, 'w') as configfile:
        config.write(configfile)
    
def getConfigFile(sections, attribute):
    dir = getAppDataLocalPath() / "app.conf"
    config = configparser.ConfigParser()
    config.read(dir)
    return config[sections][attribute]