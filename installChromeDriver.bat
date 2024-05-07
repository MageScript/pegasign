@echo off

set "zip=C:\Program Files\7-Zip"
if not exist "%zip%\*" (
    curl -o 7zip.exe curl -o 7zip.exe https://www.7-zip.org/a/7z2404-x64.exe
	7zip.exe /S
	del 7zip.exe
)

taskkill /IM chrome.exe /F

curl.exe -o "C:\Program Files\chrome-win64.zip" "https://storage.googleapis.com/chrome-for-testing-public/124.0.6367.91/win64/chrome-win64.zip"
 
set "zipFile=C:\Program Files\chrome-win64.zip"
set "extractFolder=C:\Program Files"
set "chromeDriverDest=C:\Program Files\chrome-win64"
set "dezip=C:\Program Files\7-Zip\7z.exe"
 
echo %7zip%
 
if exist "%chromeDriverDest%\*" (
    rmdir /s /q "%chromeDriverDest%"
    "%dezip%" x -o"%extractFolder%" "%zipFile%"
) else (
    "%dezip%" x -o"%extractFolder%" "%zipFile%"
)
 
del "%zipFile%"
