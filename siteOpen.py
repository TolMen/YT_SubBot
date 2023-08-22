import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# Fonction pour ouvrir Chrome Driver
def startChromeDriver(incognito=False):
    chrome_options = webdriver.ChromeOptions()
    if incognito:
        chrome_options.add_argument("--incognito")
    chromedriver_path = 'chromedriver.exe'
    service = webdriver.chrome.service.Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


# Fonction pour ouvrir un site
def openWebsite(driver, url):
    driver.get(url)


# Fonction pour la position des drivers
def positionWindow(driver, x, y):
    driver.set_window_position(x, y)


# Fonction pour la taille des drivers
def resizeWindow(driver, width, height):
    driver.set_window_size(width, height)


# Fonction qui gére le driver 1
def openDriverOne(driver1):
    try:
        # Ouvre le premier site dans le premier driver
        openWebsite(driver1, 'https://temp-mail.io/fr')
        print("L'ouverture du site d'e-mail est un succès.")
        positionWindow(driver1, 0, 0)
        resizeWindow(driver1, 760, 1000)
        print("Le site d'e-mail est cadré.")
    except:
        print("Une erreur s'est produite sur le site d'e-mail !")


# Fonction qui gére le driver 2
def openDriverTwo(driver2):
    try:
        # Ouvre le deuxième site dans un deuxième driver
        openWebsite(driver2, 'https://urlz.fr/ni8X')
        print("L'ouverture de la page d'inscription est un succès.")
        positionWindow(driver2, 750, 0)
        resizeWindow(driver2, 750, 1000)
        print("La page d'inscription est cadré.")
    except:
        print("Une erreur s'est produite sur le site d'inscription !")


# Fonction pour démarrer l'ouverture des sites
def openMultipleDrivers():
    openDriverTwo(driver2)
    time.sleep(2)
    openDriverOne(driver1)


# Déclenche les 2 drivers
driver1 = startChromeDriver(incognito=False)  # Navigation normal
time.sleep(2)
driver2 = startChromeDriver(incognito=True)   # Navigation privé
