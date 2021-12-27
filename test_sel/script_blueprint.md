# Blueprint für Testskripts
---
### Bitte benutzen, wenn Testskripts hochgeladen werden
- Namenskonvention: **test_'Testfunktion'.py**
- Beachte, dass diese Testskripts wahrscheinlich nicht auf Windows laufen (zum Testen auf Windows, gerne die Importe und Variablen wie gewohnt benutzen)

```
# Imports
import logging
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


# Logger Instanz
logger = logging.getLogger()
logger.setLevel(logging.INFO)


# Variablen
url = "https://draffelberg.github.io/QuizMaster/"
anzahlFragen = 0 # to be overwritten
listOfIDs = []


# Driver Insatanz
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

s = Service('/var/lib/jenkins/workspace/chromedriver')

logger.info("Initialisiere Webdriver.. ")

drv = webdriver.Chrome(service=s, options=chrome_options)
drv.get(url)
```
