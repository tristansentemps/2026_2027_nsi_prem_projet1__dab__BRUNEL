print("==============================")
print("      DISTRIBUTEUR DE BILLETS")
print("==============================")

# Code PIN obligatoire
tentatives = 0
pin = 0

# Solde initial du compte
solde = 1000

while pin != 1234 and tentatives < 3:

    pin = int(input("Entrez votre code PIN : "))
    tentatives = tentatives + 1

    if pin != 1234:
        print("Code PIN incorrect.")

        if tentatives < 3:
            print("Il vous reste", 3 - tentatives, "tentative(s).")

        else:
            print("Nombre maximum de tentatives atteint.")
            print("Carte bloquée !")

if pin == 1234:

    print()
    print("Connexion réussie !")

    choix = 0

    # Boucle du menu principal
    while choix != 2:

        print()
        print("==============================")
        print("           MENU")
        print("==============================")
        print("1 - Retirer de l'argent")
        print("2 - Quitter")
        print("3 - Consulter son solde")
        print("4 - Déposer de l'argent")
        print()

        choix = int(input("Choisis une option : "))

        if choix == 1:

            argent = int(input("Montant à retirer : "))

            if argent <= 0:
                print("Montant invalide.")

            elif argent > 300:
                print("Retrait refusé : le plafond est de 300 €.")

            elif argent % 10 != 0:
                print("Le montant doit être un multiple de 10.")

            elif argent > solde:
                print("Retrait refusé : solde insuffisant.")

            else:
                billets100 = argent // 100
                reste = argent % 100

                billets50 = reste // 50
                reste = reste % 50

                billets20 = reste // 20
                reste = reste % 20

                billets10 = reste // 10

                print()
                print("Billets distribués :")

                if billets100 > 0:
                    print(billets100, "billet(s) de 100 €")

                if billets50 > 0:
                    print(billets50, "billet(s) de 50 €")

                if billets20 > 0:
                    print(billets20, "billet(s) de 20 €")

                if billets10 > 0:
                    print(billets10, "billet(s) de 10 €")

                # Mise à jour du solde
                solde = solde - argent

                print()
                print("Retrait effectué avec succès !")
                print("Nouveau solde :", solde, "€")

        elif choix == 2:
            print("Au revoir. Merci de votre visite !")

        elif choix == 3:
            print()
            print("==============================")
            print("       CONSULTATION SOLDE")
            print("==============================")
            print("Votre solde est de :", solde, "€")

        elif choix == 4:

            print()
            print("==============================")
            print("       DEPOT D'ARGENT")
            print("==============================")

            depot = int(input("Montant à déposer : "))

            if depot <= 0:
                print("Montant invalide.")

            elif depot > 5000:
                print("Dépôt refusé : le plafond est de 5000 €.")

            else:
                solde = solde + depot

                print()
                print("Dépôt effectué avec succès !")
                print("Montant déposé :", depot, "€")
                print("Nouveau solde :", solde, "€")

        else:
            print("Choix invalide.")

else:
    print("Accès bloqué. Impossible de continuer.")
