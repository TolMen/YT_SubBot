import time
from selenium.webdriver.common.by import By
from siteOpen import driver1


# Fonction pour copier l'e-mail temporaire
def copy_mail():
    time.sleep(1)
    button_copy = 'button[data-original-title="Copier l\'email"]'
    target_copy = driver1.find_element(By.CSS_SELECTOR, button_copy)
    try:
        target_copy.click()
        print("L'e-mail est bien copié.")
    except:
        print("La copie de l'e-mail a échoué !")
