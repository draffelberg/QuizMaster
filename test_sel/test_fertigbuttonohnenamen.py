# Imports:
import logging
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Logger Instanz: 

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Variablen

url = "https://draffelberg.github.io/QuizMaster/"
anzahlFragen = 0 # to be overwritten
listOfIDs = []

# Driver Instanz:
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

s = Service('/var/lib/jenkins/workspace/chromedriver')

logger.info("Initialisiere Webdriver.. ")
drv = webdriver.Chrome(service=s, options=chrome_options)
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
        try:
            questionID = i
            antwort = drv.find_element_by_name("r{}".format(questionID))
            antwort.click()

        except:
            logger.warning("Antwort {} konnten nicht geklickt werden".format(str(i)))

def test_submit():
    submitbutton = drv.find_element_by_id("submitbtn")
    stateOfSubmitButton = submitbutton.is_enabled()
    logger.info("Fertig Button sollte nicht klickbar sein")
    assert stateOfSubmitButton == False
