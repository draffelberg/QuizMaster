# Imports:

import time
import logging

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *

# Logger Instanz:

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Variablen

url = "https://draffelberg.github.io/QuizMaster/"
listOfIDs = []
for i in range(0,12):
    listOfIDs.append("f{}".format(i+1))

# Driver Instanz:

logger.info("Intialisiere Webdirver")
drv = webdriver.Chrome()
drv.get(url)

# Testfunktion

def test_enterName():
    logger.info("Suche Namensfeld und sende Namen")
    try:
        nameForm = drv.find_element_by_name("name")
        nameForm.click()
        nameForm.send_keys("Tester")
        logger.info("Name erfolgreich eingegeben")

    except NoSuchElementException:
        logger.warning("Kein Namensfeld gefunden!")

def test_answers():
    
    for i in listOfIDs:
        logger.info("Beantworte Fragen")
        if i == "f1":
            try:
                drv.find_element_by_xpath("//*[@id='container']/section/form[2]/input[4]").click()
            except NoSuchElementException:
                logger.warning("Frage 1 konnte nicht beantwortet werden")

        elif i == "f2":
            try:
                drv.find_element_by_xpath("//*[@id='container']/section/form[2]/input[6]").click()
            except NoSuchElementException:
                logger.warning("Frage 2 konnte nicht beantwortet werden")
        #funktioniert, weil bei 4 Fragen 1 die richtige Antwort ist.
        else:
            try:
                questionID = i
                antwort = drv.find_element_by_name("r{}".format(questionID))
                antwort.click()
            except:
                logger.warning("Antwort {} konnte nicht beantwortet werden".format(questionID))

def test_submit():
    submitbutton = drv.find_element_by_id("submitbtn")
    stateOfSubmitButton = submitbutton.is_enabled()
    assert stateOfSubmitButton == True
    submitbutton.click()
    
def test_checkPoints():
    points = drv.find_element_by_xpath("//*[@id='resultat']/h3/span[1]").text
    assert points == '6'
