import subprocess
import os

PYTHON_USED_VERSION = "3.11" # works with python 3.11 but you can try with another one


def cmdPrompt(command):
    try:
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        print("An error occurred while running the command.")
        print("Exit code:", e.returncode)


#deps
cmdPrompt("py " + PYTHON_USED_VERSION + " -m pip install -r requirements.txt")



#build exe files
cmdPrompt("rmdir /Q /S dist")

cmdPrompt("py -" + PYTHON_USED_VERSION + " -m nuitka --standalone --enable-plugin=tk-inter --disable-console --windows-icon-from-ico=.\media\pegasign.ico  --output-dir=dist --output-filename=pegasign.exe GUI.py")

cmdPrompt("py -" + PYTHON_USED_VERSION + " -m nuitka --standalone --enable-plugin=tk-inter --disable-console --windows-icon-from-ico=.\media\pegasign.ico  --output-dir=dist --output-filename=autoSignTask.exe autoSignTask.py")

cmdPrompt("py -" + PYTHON_USED_VERSION + " -m nuitka --standalone --enable-plugin=tk-inter --disable-console --windows-icon-from-ico=.\media\pegasign.ico  --output-dir=dist --output-filename=pegasignUpdate.exe pegasignUpdate.py")

cmdPrompt("rmdir /Q /S dist\GUI.build & rmdir /Q /S dist\\autoSignTask.build & xcopy dist\GUI.dist dist /E /H /I /Y & xcopy dist\\autoSignTask.dist dist /E /H /I /Y & rmdir /S /Q dist\GUI.dist & rmdir /S /Q dist\\autoSignTask.dist")

cmdPrompt("rmdir /Q /S dist\pegasignUpdate.build & xcopy dist\pegasignUpdate.dist dist /E /H /I /Y & rmdir /S /Q dist\pegasignUpdate.dist")

cmdPrompt("xcopy media dist\media /s /e /y")

cmdPrompt("copy .\installChromeDriver.bat .\dist\\")


