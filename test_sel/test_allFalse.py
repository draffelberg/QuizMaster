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
listOfIDs = []
for i in range(0,12):
    listOfIDs.append("f{}".format(i+1))
# Driver Instanz:

logger.info("Initialisiere Webdriver.. ")
drv = webdriver.Chrome()
drv.get(url)
wait = WebDriverWait(drv, 10)

def test_enterName():
    logger.info("Suche Namensfeld und sende Namen")
    try:
        nameForm = drv.find_element_by_name("name")
        nameForm.click()
        nameForm.send_keys("Tester")
    except:
        logger.warning("Fehler bei der Namenseingabe")

def test_clickAnswers():

    logger.info("Klicke Antworten durch.. ")
    for i in listOfIDs:
        if i == "f3":
            drv.find_element_by_xpath("//*[@id='container']/section/form[2]/input[10]").click()
        
        elif i == "f6":
            drv.find_element_by_xpath("//*[@id='container']/section/form[2]/input[22]").click()

        elif i == "f7":
            drv.find_element_by_xpath("//*[@id='container']/section/form[2]/input[26]").click()

        elif i == "f8":
            drv.find_element_by_xpath("//*[@id='container']/section/form[2]/input[30]").click()

        elif i == "f11":
            drv.find_element_by_xpath("//*[@id='container']/section/form[2]/input[42]").click()

        else:
            try:
                questionID = i
                antworten = drv.find_element_by_name("r{}".format(questionID))
                antworten.click()

            except:
                logger.warning("Antwort {} konnten nicht geklickt werden".format(str(i)))

def test_submit():
    logger.info("Suche Fertig Button..")
    submitbutton = drv.find_element_by_id("submitbtn")
    try:
        submitbutton.click()
        logger.info("Fertig Button geklickt")
    except:
        logger.warning("Fertig Button nicht klickbar")

