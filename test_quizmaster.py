import logging 
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *

# Logging Instanz: 

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Variablen: 

anzahl = 0
listOfIDs = []
url = "https://draffelberg.github.io/QuizMaster/"

# Driver Instanz: 

logger.info("Intialisiere Webdriver..")
drv = webdriver.Chrome()
drv.get(url)

# Wrapper Funktionen
# Zählen die Fragen anhand von <h3>'s
# ID der Antwort wird erstellt. Format: f<Nummer der Frage><a-d>

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

# Testmethoden
# Gibt 'Rick' als Namen ein
# Klickt alle gefundenen Antworten an [s. anzahlFragen() und getAnswerID()]
# Klickt auf Fertig

def test_enterName():
    
    logger.info("Suche Namensfeld..")

    try:
        nameForm = "//*[@id='container']/section/form[1]/input"
        logger.info("Namensfeld gefunden, sende Eingabe.. ")
        drv.find_element_by_xpath(nameForm).send_keys("Rick")

    except:
        logger.warning("Kein Namensfeld gefunden!")

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