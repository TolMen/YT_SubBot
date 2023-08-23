from siteOpen import *
from GestionMail import mailNewCopy
from GestionMail import mailMessageCopy
from GestionFormulaire import formStageOne
from GestionFormulaire import formStageTwo
from GestionFormulaire import formStageThree
from GestionFormulaire import formStageFour

# Appel la fonction pour ouvrir les sites
openMultipleDrivers()

# Appel la fonction pour compléter l'étape 1 du formulaire (Prénom)
formStageOne.startStageOne()

# Appel la fonction pour compléter l'étape 2 du formulaire (Date Naissance / Genre)
formStageTwo.startStageTwo()

# Appel la fonction pour cliquer sur le bouton qui copie les e-mails
mailNewCopy.copy_mail()

# Appel la fonction pour compléter l'étape 3 du formulaire (E-mail)
formStageThree.startStageThree()


mailMessageCopy.startMailMessageCopy()
formStageFour.startStageFour()
