#import library
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
driver = webdriver.Chrome()

# variables
url = "https://draffelberg.github.io/QuizMaster/"

def selectAnswer():
    for i in range(1,13):
        correctAnswer = [4,6,9,15,20,21,28,29,35,40,41,46]
        xpathValue = '//*[@id="container"]/section/form[2]/input[{}]'.format(correctAnswer[i-1])
        optionValue= driver.find_element_by_xpath(xpathValue)
        optionValue.click()
        time.sleep(1)


def test_PlayCorrect():
    logger.info("Programm beginn ...")
    logger.info("QuizMaster web page aufrufen: ")
    driver.get(url)
    logger.info("username eingeben")
    inputName= driver.find_element_by_name(name="name")
    inputName.send_keys("Tester")
    time.sleep(2)
    logger.info("Alle Fragen richtig antworten.")
    selectAnswer()
    logger.info("click on Fertig")
    fertig =driver.find_element_by_id("submitbtn")
    fertig.click()
    logger.info("Check Infos")
    result = driver.find_element_by_xpath('//*[@id="resultat"]/h3')
    if "Tester, du hast 12 von 12 Punkten erzielt" in result.text:
        logger.info("pass")
    time.sleep(5)
    driver.quit()