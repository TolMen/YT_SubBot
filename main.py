from siteOpen import *
from gestionMail import *
from GestionFormulaire import formStageOne
from GestionFormulaire import formStageTwo

# Appel la fonction pour ouvrir les sites
openMultipleDrivers()

# Appel la fonction pour compléter l'étape 1 du formulaire (Prénom)
formStageOne.startStageOne()

# Appel la fonction pour compléter l'étape 2 du formulaire (Date Naissance / Genre)
formStageTwo.startStageTwo()

# Appel la fonction pour cliquer sur le bouton qui copie les e-mails
copy_mail()
