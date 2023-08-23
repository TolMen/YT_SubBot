import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from siteOpen import driver2
from VariousInfo import directoryDateBirth


# Fonction pour écrire le jour de naissance dans l'étape 2 du formulaire
def editBirthDay():
    time.sleep(4)
    selector_day = 'day'
    formInputDay = driver2.find_element(By.ID, selector_day)
    try:
        numberBirthDay = directoryDateBirth.generateBirthDay()  # Lance la génération du nombre
        formInputDay.send_keys(numberBirthDay)
        print("Le jour est écrit.")
    except:
        print("L'écriture du jour a échoué !")


# Fonction pour sélectionner le mois
def editBirthMonth():
    time.sleep(5)
    # Partie pour ouvrir la liste déroulante
    button_list_month = 'month'
    target_list_month = driver2.find_element(By.ID, button_list_month)
    try:
        target_list_month.click()
        print("La liste des mois est déroulé.")
    except:
        print("La liste des mois ne peut pas être déroulée !")

    time.sleep(3)

    # Partie pour cliquer sur la liste déroulante
    randomNumberMonth = random.randint(1, 12)
    selector_value_month = f'option[value="{randomNumberMonth}"]'
    target_value_month = driver2.find_element(By.CSS_SELECTOR, selector_value_month)
    try:
        target_value_month.click()
        print("Le mois est bien séléctionné")
    except:
        print("Le mois n'a pas pu être séléctionné !")


# Fonction pour écrire l'année de naissance dans l'étape 2 du formulaire
def editBirthYear():
    time.sleep(4)
    selector_year = 'year'
    formInputYear = driver2.find_element(By.ID, selector_year)
    try:
        numberBirthYear = directoryDateBirth.generateBirthYear()  # Lance la génération du nombre
        formInputYear.send_keys(numberBirthYear)
        print("L'année est écrit.")
    except:
        print("L'écriture de l'année a échoué !")


# Fonction pour lancer l'étape 2
def startStageTwo():
    editBirthDay()
    editBirthMonth()
    editBirthYear()