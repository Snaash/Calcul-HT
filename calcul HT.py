def hors_taxe():
    prix = int(input('Entrez un prix: '))
    hors_taxe = 0.2

    prix_horstaxe = prix-(prix*hors_taxe)
    print(f"Le prix est de {prix_horstaxe}€ HT")


hors_taxe()
while True:
    quit_restart = input("Q pour quitter ou A pour recommencer")
    if quit_restart == "A" or "a":
        print('Ok on relance')
        hors_taxe()
    elif quit_restart == "Q" or "q":
        break
