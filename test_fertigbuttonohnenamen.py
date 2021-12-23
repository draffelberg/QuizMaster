import logging
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *

# Logging Instanz:

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Variablen

url = "https://draffelberg.github.io/QuizMaster/"
anzahl = 0
listOfIDs = []

# Driver Instanz
drv = webdriver.Chrome()
drv.get(url)

# Wrapper Funktionen
# Zählen fragen und erstellen Antwort IDs

def anzahlFragen():
    try:
        logger.info("Zähle Fragen.. ")
        counted = len(drv.find_elements_by_tag_name("h3"))
        global anzahl
        anzahl = counted
        logger.info("Fragen erflogreich gezählt!")
    except NoSuchElementException:
        logger.warning("Fragen konnten nicht erzählt werden")

def getAnswerID():
    if anzahl >= 1:
        try:
            logger.info("Sammle IDs...")
            for i in range(0, anzahl):
                id = "f{}".format(i+1)
                listOfIDs.append(str(id) + "a")
                listOfIDs.append(str(id) + "b")
                listOfIDs.append(str(id) + "c")
                listOfIDs.append(str(id) + "d")
        except:
            logging.warning("Fehler bei ID Erstellung")

# Testfunktion
# Klicken alle Antworten und auf Fertig ohne Namen einzugeben

def test_clickAnswers():

    anzahlFragen()
    getAnswerID()
    try:
        for i in listOfIDs:
            drv.find_element_by_id(i).click()
            time.sleep(0.1)
            logger.info("Button mit der ID: {} wurde geklickt".format(i))
    except NoSuchElementException:
        logger.warning("")

def test_clickFinish():
    logger.info("Suche und drücke auf 'Fertig'")
    try:
        finishButton = "//*[@id='container']/section/form[2]/input[49]"
        drv.find_element_by_xpath(finishButton).click()
    except:
        logger.warning("Kein 'Fertig'-Button gefunden!")