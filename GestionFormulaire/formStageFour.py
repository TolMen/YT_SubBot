import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from siteOpen import driver2

# Le morceau de fonction pour coller le code est dans le
# fichier mailMessageCopy.py dans la fonction copyCodeMail


# Fonction pour valider l'étape 4
def nextFormCode():
    time.sleep(1)
    button_next_code = 'VfPpkd-vQzf8d'
    target_next_StageFour = driver2.find_element(By.CLASS_NAME, button_next_code)
    try:
        target_next_StageFour.click()
        print("-----> L'étape du code est validé. <-----")
    except:
        print("-----> L'étape du code a échoué ! <-----")


# Fonction pour lancer l'étape 4
def startStageFour():
    nextFormCode()
