import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from siteOpen import driver2
from VariousInfo import directoryFirstName


# Fonction pour écrire le prénom dans l'étape 1 du formulaire
def editFormName():
    time.sleep(2)
    selector_name = 'firstName'
    formInputName = driver2.find_element(By.ID, selector_name)

    try:
        # Chemin vers la liste des prénoms
        firstNameList = directoryFirstName.listFirstName
        randomFirstName = random.choice(firstNameList)   # Sélectionne un prénom dans la liste
        formInputName.send_keys(randomFirstName)
        print("Le prénom est bien renseigné.")
    except:
        print("L'écriture du prénom a échoué !")


# Fonction pour valider l'étape 1
def nextFormName():
    time.sleep(2)
    button_next = 'VfPpkd-LgbsSe-OWXEXe-dgl2Hf'
    target_next = driver2.find_element(By.CLASS_NAME, button_next)
    try:
        target_next.click()
        print("-----> L'étape du prénom est validé. <-----")
    except:
        print("-----> L'étape du prénom a échoué ! <-----")


# Fonction pour lancer l'étape 1
def startStageOne():
    editFormName()
    nextFormName()
