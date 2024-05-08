# Pegasign

## Overview
Pegasign is a Python tool designed for engineering schools to automate attendance tracking on the Pegasus platform. This tool simplifies the process of verifying student attendance.
## Installation
You have two options for installing Pegasign:

1. **Build from Source:**
   - Clone this repository to your local machine.
   - Navigate to the project directory.
   - Run `python build.py`.
   - The built program will be available in the `dist` directory.

2. **Download Installer:**
   - Visit the [Releases](https://github.com/MageScript/pegasign/releases) section of this repository.
   - Download the latest installer compatible with your Windows operating system.
   - Run the installer and follow the installation instructions.


## Usage
   - Open the app.conf file in %localappdata%\Pegasign
   - Configure the index.php url of pegasus
   - Configure your email and password for login
   - Open pegasign.exe and create a new signature
   - Enable "Activate automated signing"

## Compatibilitys
Pegasign is designed to work with Python 3.11, but it may also function with other versions of Python. 
Only works on Windows.

## Features
- Automatically sign for you (the program can launch at pc startup)
- Create new signatures
- Manually run a signing process

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
