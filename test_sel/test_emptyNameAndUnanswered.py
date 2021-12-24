# Imports:
import logging
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *

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

def test_clickAnswers():

    fragenZaehlen()
    getAnswerID()
    logger.info("Klicke Antworten durch.. ")
    for i in listOfIDs:
        if i == "f1":
            continue
        try:
            questionID = i
            antworten = drv.find_elements_by_name("r{}".format(questionID))

            for element in antworten:
                element.click()
                time.sleep(0.1)
        except:
            logger.warning("Antwort {} konnten nicht geklickt werden".format(str(i)))

def test_submit():
    submitbutton = drv.find_element_by_id("submitbtn")
    stateOfSubmitButton = submitbutton.is_enabled()
    assert stateOfSubmitButton == False
    submitbutton.click() 
    