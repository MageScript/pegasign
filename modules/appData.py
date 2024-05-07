from pathlib import Path


def getAppDataLocalPath():
    return Path.home() / "AppData" / "Local" / "Pegasign"


def addPegasignFolder():
    # Build the full path to the directory in AppData\Local
    pegasignPath = getAppDataLocalPath()

    # Check if the directory exists
    if pegasignPath.exists() and pegasignPath.is_dir():
        print("the directory exists in AppData\\Local")
    else:
        # Create the directory if it doesn't exist
        pegasignPath.mkdir(parents=True, exist_ok=True)
        print("the directory has been created in AppData\\Local")


def addLogFile():
    # Build the full path to the directory in AppData\Local
    lofFilePath = getAppDataLocalPath()

    # Check if pegasign.log exists within the directory
    filePath = lofFilePath / "pegasign.log"
    if filePath.exists() and filePath.is_file():
        print("the file pegasign.log exists in the directory")
    else:
        # Create pegasign.log if it doesn't exist
        with open(filePath, "w") as f:
            f.write("initial content for pegasign.log\n")
        print("the file pegasign.log has been created in the directory")


def addSignatureFolder():

    # Build the full path to the directory in AppData\Local
    signaturePath = getAppDataLocalPath() / "signatures"

    # Check if the directory exists
    if signaturePath.exists() and signaturePath.is_dir():
        print("the directory exists in AppData\\Local")
    else:
        # Create the directory if it doesn't exist
        signaturePath.mkdir(parents=True, exist_ok=True)
        print("the directory has been created in AppData\\Local\\signatures")
    pointsPath = getAppDataLocalPath() / "signatures\\points"
    # Check if the directory exists
    if pointsPath.exists() and pointsPath.is_dir():
        print("the directory exists in AppData\\Local\\signatures")
    else:
        # Create the directory if it doesn't exist
        pointsPath.mkdir(parents=True, exist_ok=True)
        print("the directory has been created in AppData\\Local\\signatures")
    picsPath = getAppDataLocalPath() / "signatures\\pics"
    # Check if the directory exists
    if picsPath.exists() and picsPath.is_dir():
        print("the directory exists in AppData\\Local\\signatures")
    else:
        # Create the directory if it doesn't exist
        picsPath.mkdir(parents=True, exist_ok=True)
        print("the directory has been created in AppData\\Local")


def addAppConfFile():
    confFileContent = """[app.conf]
showgoogle = false
autosign = false
processpid = x
pegasusurl = https://learning.estia.fr/pegasus/index.php
email = <your_email>
password = <your_password>
1sign = false
2sign = false
3sign = false
4sign = false
currentday = Thursday
"""
    # Build the full path to the directory in AppData\Local
    appConfPath = getAppDataLocalPath()

    # Check if pegasign.log exists within the directory
    filePath = appConfPath / "app.conf"
    if filePath.exists() and filePath.is_file():
        print("the file app.conf exists in the directory")
    else:
        # Create pegasign.log if it doesn't exist
        with open(filePath, "w") as f:
            f.write(confFileContent)
        print("the file pegasign.log has been created in the directory")


def appDataCheck():
    addPegasignFolder()
    addLogFile()
    addSignatureFolder()
    addAppConfFile()