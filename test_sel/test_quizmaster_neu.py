# Imports:
import logging
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Logger Instanz: 

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Variablen

url = "https://draffelberg.github.io/QuizMaster/"
anzahlFragen = 0 # to be overwritten
listOfIDs = []

# Driver Instanz:

logger.info("Initialisiere Webdriver.. ")
drv = webdriver.Chrome()
drv.get(url)
wait = WebDriverWait(drv, 10)

# Wrapper Funktion

def fragenZaehlen():
    
    logger.info("Zähle Fragen..")

    try:
        counted = len(drv.find_elements_by_tag_name("h3"))
        global anzahlFragen
        anzahlFragen = counted
        logger.info("{} Fragen gefunden".format(str(counted)))

    except NoSuchElementException:
        logger.warning("Keine Fragen gefunden")

def getAnswerID():
    if anzahlFragen > 1:
        try:
            logger.info("Sammle IDs")
            for i in range(0, anzahlFragen):
                id = "f{}".format(i+1)
                listOfIDs.append(str(id))
        except:
            logger.warning("Fehler bei ID Erstellung")

# Testfunktionen

def test_enterName():
    logger.info("Suche Namensfeld und sende Namen")
    nameForm = drv.find_element_by_name("name")
    nameForm.click()
    nameForm.send_keys("Tester")

def test_clickAnswers():

    fragenZaehlen()
    getAnswerID()

    for i in listOfIDs:
        
        questionID = i
        antworten = drv.find_elements_by_name("r{}".format(questionID))

        for element in antworten:
            element.click()
            time.sleep(0.2)

def test_submit():
    submitbutton = drv.find_element_by_id("submitbtn")
    submitbutton.click()