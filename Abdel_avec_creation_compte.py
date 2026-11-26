import random

CODE_PIN = "1234"
PLAFOND_RETRAIT = 1000

comptes = {
    "Monnier": {"pin": CODE_PIN, "solde": 500.0}
}

print("===================================")
print("====== DISTRIBUTEUR DE BILLETS =====")
print("===================================")

reponse = input("Possédez-vous déjà un compte bancaire ? (0=Oui / 1=Non) : ")

if reponse == "1":
    creation = input("Souhaitez-vous créer un compte ? (0=Oui / 1=Non) : ")

    if creation == "0":
        identifiant = input("Veuillez définir un identifiant de compte : ")

        while identifiant in comptes:
            print("Cet identifiant existe déjà. Veuillez en choisir un autre.")
            identifiant = input("Nouvel identifiant : ")

        nouveau_pin = input("Veuillez définir un code PIN : ")
        comptes[identifiant] = {"pin": nouveau_pin, "solde": 500.0}
        print("Votre compte a été créé avec succès.")

    elif creation == "1":
        print("Merci de votre visite. Au revoir.")
        quit()
    else:
        print("Choix incorrect. Au revoir.")
        quit()

elif reponse != "0":
    print("Choix incorrect. Au revoir.")
    quit()

identifiant = input("Entrez votre identifiant de compte : ")

if identifiant not in comptes:
    print("Votre identifiant ne figure pas dans notre base de données. Au revoir.")
    quit()

tentatives = 0
code_correct = False

while tentatives < 3 and code_correct == False:
    code = input("Veuillez saisir votre code PIN : ")

    if code == comptes[identifiant]["pin"]:
        code_correct = True
        print("Code bon. Connexion effectuée avec succès.")
    else:
        tentatives = tentatives + 1
        restant = 3 - tentatives

        if restant > 0:
            print(f"Code incorrect, il vous reste {restant} tentative(s).")
        else:
            print("Carte bloquée après 3 codes PIN incorrects.")
            print("Au revoir.")

if code_correct == True:
    solde = comptes[identifiant]["solde"]

    while True:
        print("\n----------- MENU -----------")
        print("1- Voir votre solde")
        print("2- Retirer de l'argent")
        print("3- Déposer de l'argent")
        print("4- Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            print(f"Votre solde est de {solde:.2f} €")

        elif choix == "2":
            montant = float(input("Montant à retirer (en euros) : "))

            if montant <= 0:
                print("Erreur : le montant doit être positif.")
            elif montant > solde:
                print("Retrait refusé : solde insuffisant.")
            elif montant > PLAFOND_RETRAIT:
                print(f"Retrait refusé : le plafond est de {PLAFOND_RETRAIT} € par retrait.")
            else:
                solde = solde - montant
                print(f"Retrait accepté : {montant:.2f} €")

                reste = round(montant * 100)
                valeurs = [
                    (10000, "billet(s) de 100 €"),
                    (5000, "billet(s) de 50 €"),
                    (2000, "billet(s) de 20 €"),
                    (1000, "billet(s) de 10 €"),
                    (500, "billet(s) de 5 €"),
                    (200, "pièce(s) de 2 €"),
                    (100, "pièce(s) de 1 €"),
                    (50, "pièce(s) de 50 centimes"),
                    (20, "pièce(s) de 20 centimes"),
                    (10, "pièce(s) de 10 centimes"),
                    (5, "pièce(s) de 5 centimes"),
                    (2, "pièce(s) de 2 centimes"),
                    (1, "pièce(s) de 1 centime")
                ]

                for valeur, nom in valeurs:
                    nombre = reste // valeur
                    if nombre > 0:
                        print(f"{nombre} {nom}")
                    reste = reste % valeur

                print(f"Votre nouveau solde est de {solde:.2f} €.")

        elif choix == "3":
            montant_depose = float(input("Montant à déposer (en euros) : "))

            if montant_depose <= 0:
                print("Erreur : le montant à déposer doit être positif.")
            else:
                solde = solde + montant_depose
                print(f"Dépôt accepté : {montant_depose:.2f} €")
                print(f"Votre nouveau solde est de {solde:.2f} €.")

        elif choix == "4":
            print("Au revoir.")
            break

        else:
            print("Choix invalide, veuillez choisir entre 1 et 4.")

    comptes[identifiant]["solde"] = solde
