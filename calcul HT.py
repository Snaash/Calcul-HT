import os


#Le prix est à définir par l'utilisateur dans la variable prix, le calcul HT se fait sur la base 20%

def hors_taxe():
    prix = int(input('Entrez un prix: '))
    hors_taxe = 0.2

#Ici on effectue le calcul du produit HT pour ensuite l'afficher

    prix_horstaxe = prix-(prix*hors_taxe)
    print(f"Le prix est de {prix_horstaxe}€ HT")


#Dans cette partie, nous allons fermer ou relancer le script en fonction des besoins

hors_taxe()
while True:
    quit_restart = input("Q pour quitter ou A pour recommencer")
    if quit_restart == "A" or "a":
        print('Ok on relance')
        hors_taxe()
    elif quit_restart == "Q" or "q":
        os.exit(0)