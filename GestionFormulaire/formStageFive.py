import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from siteOpen import driver2
from VariousInfo import directoryPassword


# Fonction pour écrire le mot de passe dans l'étape 5 du formulaire
def editFormPassword():
    time.sleep(2)
    selector_password = '[name="Passwd"]'
    formInputPassword = driver2.find_element(By.CSS_SELECTOR, selector_password)
    try:
        # Chemin vers la liste des mots de passe
        passwordList = directoryPassword.listPassword
        randomPassword = random.choice(passwordList)   # Sélectionne un MDP dans la liste
        formInputPassword.send_keys(randomPassword)
        print("Le mot de passe est bien renseigné.")
    except:
        print("L'écriture du mot de passe a échoué !")

    time.sleep(2)
    selector_passwordAgain = '[name=PasswdAgain]'
    formInputPasswordAgain = driver2.find_element(By.CSS_SELECTOR, selector_passwordAgain)
    try:
        formInputPasswordAgain.send_keys(randomPassword)
        print("La confirmation du mot de passe est réussi.")
    except:
        print("Echec de la confirmation du mot de passe !")


# Fonction pour valider l'étape 5
def nextFormPassword():
    time.sleep(2)
    button_next_password = 'VfPpkd-LgbsSe-OWXEXe-dgl2Hf'
    target_next_StageFive = driver2.find_element(By.CLASS_NAME, button_next_password)
    try:
        target_next_StageFive.click()
        print("-----> L'étape du mot de passe est validé. <-----")
    except:
        print("-----> L'étape du mot de passe a échoué ! <-----")


# Fonction pour lancer l'étape 5
def startStageFive():
    editFormPassword()
    nextFormPassword()
