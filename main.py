from siteOpen import *
from GestionMail import mailNewCopy
from GestionMail import mailMessageCopy
from GestionFormulaire import formStageOne
from GestionFormulaire import formStageTwo
from GestionFormulaire import formStageThree
from GestionFormulaire import formStageFour
from GestionFormulaire import formStageFive


def startProjetBotYoutube():
    openMultipleDrivers()   # Ouvre les deux pages Internet
    formStageOne.startStageOne()   # Compléte l'étape UN du formulaire (Prénom)
    formStageTwo.startStageTwo()   # Compléte l'étape DEUX du formulaire (Date de naissance & Genre)
    mailNewCopy.copy_mail()   # Copie les E-Mails temporaire
    formStageThree.startStageThree()  # Compléte l'étape TROIS du formulaire (E-Mail)
    mailMessageCopy.startMailMessageCopy()  # Copie et colle le code de confirmation
    formStageFour.startStageFour()  # Compléte l'étape QUATRE du formulaire (Code de confirmation)
    formStageFive.startStageFive()   # Compléte l'étape CINQ du formulaire (Mot de passe)


# Fonction de lancement du projet
if __name__ == "__main__":
    startProjetBotYoutube()
