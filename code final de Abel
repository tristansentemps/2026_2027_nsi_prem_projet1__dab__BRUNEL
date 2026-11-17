CODE_PIN = "1234"
solde = 500
PLAFOND_RETRAIT = 300
tentatives = 0
while tentatives<3:
    code = input("Veuillez saisir votre code PIN:")
    if code == CODE_PIN:
        print ("Code bon, veuillez saisir l'action que vous voulez effectuer:")
        break
    else:
        tentatives = tentatives + 1
        restant = 3 - tentatives 


    if restant > 0:
        print (f"Code mauvais, il vous reste {restant} tentative ")
    else:
        print("Carte bloquée après 3 codes PIN incorrects.")
        print("Au revoir")
while code == CODE_PIN:
    print("1-voir votre solde")
    print("2-retirer de l'argent")
    print("3-quitter")
    choix = input("votre choix:")
    if choix == "1":
        print(f"Votre solde est de {solde}€")
    elif choix == "2":
        montant = int(input("Montant à retirer (en euros) : "))
        if montant<=0:
            print("Erreur : le montant doit être un entier positif.")
        elif montant % 10 != 0:
            print("Erreur : le montant doit être un multiple de 10 €.")
        elif montant > solde:
            print("Retrait refusé : solde insuffisant.")
        elif montant > PLAFOND_RETRAIT:
            print(f"Retrait refusé : le plafond est de {PLAFOND_RETRAIT} € par retrait.")
        else:
            solde = solde - montant
            print(f"Retrait accepté : {montant} €.")
            billet_50 = montant // 50
            if montant % 50 >= 0:
                if billet_50 > 0:
                    print(f"{billet_50} billets de 50")
            reste = montant - billet_50*50
            if reste % 20 >= 0:
                billet_20 = reste // 20 
                if billet_20 > 0:
                    print(f"{billet_20} billets de 20")
            reste2 = reste - billet_20*20
            
            if reste2 % 10 >= 0:
                billet_10 = reste2 // 10 
                if billet_10 > 0 :
                    print(f"{billet_10} billets de 10")
            
            print(f"Votre nouveau solde est de {solde} €.")
    elif choix == "3":
        print("Au revoir")
        break
    else:
        print ("il y a seulement 3 choix, réessayez")
