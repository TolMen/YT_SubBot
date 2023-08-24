import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from siteOpen import driver1
from siteOpen import driver2


# Fonction pour ouvrir le message reçu
def selectMail():
    time.sleep(15)
    selector_MessageMail = 'message__body'
    target_MessageMail = driver1.find_element(By.CLASS_NAME, selector_MessageMail)
    try:
        target_MessageMail.click()
        print("Le clic sur le message a eu lieu.")
    except:
        print("Le clic sur le message a échoué !")


# Fonction pour copier le code de confirmation
def copyCodeMail():
    time.sleep(2)
    try:
        selector_CodeMail = 'div[style*="font-size:24px"]'
        target_CodeMail = driver1.find_element(By.CSS_SELECTOR, selector_CodeMail)
        codeText = target_CodeMail.text.strip()
        print("Le code trouvé est :", codeText)
    except:
        print("Aucun code trouvé")
        return None

    # Morceau de fonction pour coller le code de confirmation
    selector_code = 'code'
    formInputCode = driver2.find_element(By.ID, selector_code)

    try:
        formInputCode.send_keys(codeText)
        print("Le code est bien collé.")
    except:
        print("La copie du code a échoué !")


# Fonction pour lancer l'étape de copie/colle du code de confirmation
def startMailMessageCopy():
    selectMail()
    copyCodeMail()
