import random


# Fonction qui génére un nombre entre 1 et 29 pour le jour d'anniversaire
def generateBirthDay():
    return random.randint(1, 29)


# Fonction qui génére une année entre 1975 et 2004 pour l'année d'anniversaire
def generateBirthYear():
    return random.randint(1975, 2004)