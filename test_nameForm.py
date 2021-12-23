import logging
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *

# Logging Instanz: 

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Variablen 

anzahl = 0
listOfIDs = []
url = "https://draffelberg.github.io/QuizMaster/"
nameFormXPath = "//*[@id='container']/section/form[1]/input"

# Driver Instanz: 

logger.info("Intialisiere Webdriver..")
drv = webdriver.Chrome()
drv.get(url)

def test_Namensfeld():

    logger.info("Finde Namensfeld")
    try:
        nameForm = drv.find_element_by_xpath(nameFormXPath)
        logger.info("Namensfeld gefunden")
    except NoSuchElementException:
        logger.warning("Kein Namensfeld gefunden")
    
    logger.info("Sende einfachen String an Namensfeld: ")
    try:
        nameForm.click()
        nameForm.clear()
        nameForm.send_keys("Test")
        logger.info("Einfacher String wurde eingegeben")
        time.sleep(0.5)
    except:
        logger.warning("Irgendwas läuft mächtig schief")

    logger.info("Sende Zahlenfolge an Namensfeld: ")
    try:
        nameForm.click()
        nameForm.clear()
        nameForm.send_keys("123456789")
        logger.info("Zahlenfolge erfolgreich eingegeben")
        time.sleep(0.5)
    except:
        logger.warning("Zahlenfolge kann nicht eingegeben werden")

    logger.info("Sende Space an Namensfeld")
    try:
        nameForm.click()
        nameForm.clear()
        nameForm.send_keys(" ")
        logger.info("Space funktioniert")
        time.sleep(0.5)
    except:
        logger.warning("HALT STOP")

    logger.info("Sende String + Newline an Namensfeld: ")
    try:
        nameForm.click()
        nameForm.clear()
        nameForm.send_keys("Test \n")
        time.sleep(0.5)
    except:
        logger.warning("Newline kann nicht eingegeben werden")
