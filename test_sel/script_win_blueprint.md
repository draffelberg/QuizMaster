```
# Imports
import logging
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *

# Logger Instanz
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Variablen
url = "https://draffelberg.github.io/QuizMaster/"
anzahlFragen = 0 # to be overwritten
listOfIDs = []

# Driver Instanz
logger.info("Initialisiere Webdriver.. ")

drv = webdriver.Chrome()
drv.get(url)
```
