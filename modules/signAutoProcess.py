from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from modules.configuration import getConfigFile
from modules.readSignature import readSignatures
from modules.printAndLog import printAndLog

import time
from win11toast import toast


def signAutoProcess(showGoogle=False, signaturePath=None):
    email = getConfigFile("app.conf", "email")
    passw = getConfigFile("app.conf", "password")

    options = webdriver.ChromeOptions()
    if not showGoogle:
        options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    # options.add_argument(r"--user-data-dir=C:/Users/l.elizalde/AppData/Local/Google/Chrome for Testing/User Data")
    # options.add_argument(r'--profile-directory=Profile 1')
    chromeBin = "C:/Program Files/chrome-win64/chrome.exe"
    options.binary_location = chromeBin

    browser = webdriver.Chrome(options=options)
    pegasusURL = getConfigFile("app.conf", "pegasusURL")
    browser.get(pegasusURL)
    browser.maximize_window()


    def clear_text(element):
                length = len(element.get_attribute('value'))
                element.send_keys(length * Keys.BACKSPACE)
                
    def elementAction(browser, xpath, click=False, fill=False, fillText="", clearText=False, delay=30, elementName="Element"):
        
        try:
            # Wait for the element with the ID of wrapper
            wrapper = WebDriverWait(browser, delay).until(
            EC.presence_of_element_located((By.XPATH, xpath))
            )
            

            printAndLog(f"{elementName} is present in the DOM now")
            ele = browser.find_element(By.XPATH, xpath)
            
            if(click and fill):
                printAndLog("error: click and fill can't be true simultaneously")
                return

            if(fill and fillText == ""):
                printAndLog("warning: fillText is empty")
            
            #click on the element
            if(click):
                ele.click()
            
            #delete the text input that as been automatically generated
            if(clearText):
                clear_text(ele)
            
            #fill the input
            if(fill):
                ele.send_keys(fillText)
        
        
        except TimeoutException:
            printAndLog(f"{elementName} did not show up")
            
        time.sleep(2)


    #click on the login button
    elementAction(browser=browser, xpath="/html/body/div[2]/div/div[3]/div[2]/div/form/button/a",
                click=True, elementName="loginButton")
    #fill the email
    elementAction(browser=browser, xpath="/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]",
                fill=True, clearText=True, fillText=email, elementName="emailInput")
    #click next
    elementAction(browser=browser, xpath="/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div/input",
                click=True, elementName="nextButton")
    #fill password
    elementAction(browser=browser, xpath="/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input",
                fill=True, fillText=passw, clearText=True, elementName="passwordInput")
    #click signin
    elementAction(browser=browser, xpath="/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[5]/div/div/div/div/input",
                click=True, elementName="signinButton")
    #click yes
    elementAction(browser=browser, xpath="/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input",
                click=True, elementName="yesButton")
    #click on Vie Académique
    elementAction(browser=browser, xpath="/html/body/div[1]/div[2]/div[1]/nav/div/div[2]/div[2]/div/div[2]", 
                click=True, elementName="vieAcademique")
    #click on Consulter mes émargements
    elementAction(browser=browser, xpath="/html/body/div[1]/div[2]/div[1]/nav/div/div[2]/div[3]/div/a[2]/div",
                click=True, elementName="mesEmargementsButton")

    time.sleep(2)


    try:
        # Wait for the element with the ID of wrapper
        id = "pegasus_contenu"
        wrapper = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, id))
        )


        iframe = browser.find_element(By.ID, id)
        browser.switch_to.frame(iframe)
        
        for i in range(2, 7):
            printAndLog(f"i={i}")
            xpath = f"/html/body/div[1]/div/div[3]/table/tbody/tr[2]/td[{i}]/div/div"
            emargementCases = browser.find_elements(By.XPATH, xpath)
                
            printAndLog("emarge case is present in the DOM now")
            for case in emargementCases:
                cssProperties = case.get_attribute("style")
                background = cssProperties.split(';')
                if(background[0] == "background-color: rgb(245, 161, 62)"):
                    case.click()
                    
            #DEBUG
            debug = False
            if(i == 4 and debug):
                case.click()
                browser.execute_script("EMARGEABLE = true;") 
                

    except TimeoutException:
        printAndLog("emarge case did not show up")
        
        
    try:
        # Wait for the element with the ID of wrapper
        canvaXpath = "/html/body/div[6]/div[1]/div[2]/div[2]/div[1]/div/table/tbody/tr[1]/td[2]/div/div/canvas"
        wrapper = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, canvaXpath))
        )
        
        canva = browser.find_element(By.XPATH, canvaXpath)
        printAndLog("canve is present in the DOM now")
        signature_coords = readSignatures(signaturePath)
        actions = ActionChains(browser, duration=0)
        printAndLog(str(signature_coords[0][0]) + " " + str(signature_coords[0][1]))
        actions.move_to_element_with_offset(canva, signature_coords[0][0]-85, signature_coords[0][1]-85).click_and_hold()

        
        for prevSign, sign in zip(signature_coords, signature_coords[1:]):
            if prevSign is not None:
                printAndLog(str(sign[0]-prevSign[0]) + str(sign[1]-prevSign[1]))
                actions.move_by_offset(sign[0]-prevSign[0], sign[1]-prevSign[1])
        
        actions.release(canva)
        try:
            actions.perform()
        except Exception as e: 
            printAndLog(e)

    except TimeoutException:
        printAndLog("canva did not show up")
        
    elementAction(browser=browser, xpath="/html/body/div[6]/div[1]/div[2]/div[2]/div[1]/div/div/button[1]", 
                  click=True, elementName="validButton")
    
    browser.quit()
    
    return True

