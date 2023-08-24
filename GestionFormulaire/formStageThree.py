import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from siteOpen import driver2


# Fonction pour écrire l'e-mail dans l'étape 3 du formulaire
def editFormMail():
    time.sleep(1)
    selector_mail = 'identifierId'
    formInputMail = driver2.find_element(By.ID, selector_mail)

    try:
        formInputMail.send_keys(Keys.CONTROL, 'v')
        print("L'e-mail est bien collé.")
    except:
        print("La copie de l'e-mail a échoué !")


# Fonction pour valider l'étape 3
def nextFormMail():
    time.sleep(1)
    button_next_mail = 'VfPpkd-vQzf8d'
    target_next_StageThree = driver2.find_element(By.CLASS_NAME, button_next_mail)
    try:
        target_next_StageThree.click()
        print("-----> L'étape de l'e-mail est validé. <-----")
    except:
        print("-----> L'étape de l'e-mail a échoué ! <-----")


# Fonction pour lancer l'étape 3
def startStageThree():
    editFormMail()
    nextFormMail()
