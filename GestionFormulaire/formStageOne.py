import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from siteOpen import driver2


# Fonction pour écrire le prénom dans l'étape 1 du formulaire
def editFormName():
    time.sleep(5)
    selector_name = 'firstName'
    formInputName = driver2.find_element(By.ID, selector_name)

    # Liste de 30 prénoms
    listFirstName = [
        "Alice", "Bob", "Claire", "David", "Emma", "Francis", "Grace",
        "Henry", "Isabelle", "Jack", "Kate", "Liam", "Mia", "Noah",
        "Olivia", "Paul", "Quinn", "Ryan", "Sophia", "Thomas", "Uma",
        "Victor", "Willow", "Xander", "Yara", "Zachary", "Ava", "Benjamin",
        "Chloe", "Daniel", "Emily"
    ]

    try:
        randomFirstName = random.choice(listFirstName)   # Sélectionne un prénom dans la liste
        formInputName.send_keys(randomFirstName)
        print("Le prénom est bien renseigné.")
    except:
        print("L'écriture du prénom a échoué !")


# Fonction pour valider l'étape 1
def nextFormName ():
    time.sleep(3)
    try:
        button_next = 'VfPpkd-LgbsSe-OWXEXe-dgl2Hf'
        target_next = driver2.find_element(By.CLASS_NAME, button_next)
        print("Element trouvé")
    except:
        print("Element introuvable")
    try:
        target_next.click()
        print("L'étape du prénom est validé.")
    except:
        print("L'étape du prénom a échoué !")


# Fonction pour lancer l'étape 1
def startStageOne():
    editFormName()
    nextFormName()