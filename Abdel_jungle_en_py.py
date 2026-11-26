CODE_PIN = "1234"
solde = 500

comptes = {
    "Monnier": {"pin": CODE_PIN, "solde": 500.0}
}

print("===================================")
print("===== DISTRIBUTEUR DE BILLETS =====")
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
solde = comptes[identifiant]["solde"]

PLAFOND_RETRAIT = 300
tentatives = 0
while tentatives < 3:
    code = input("Veuillez saisir votre code PIN:")
    if code == comptes[identifiant]["pin"]:
        print()
        print ("Code bon, veuillez saisir l'action que vous voulez effectuer:")
        break
    else:
        tentatives = tentatives + 1
        restant = 3 - tentatives

    if restant > 0:
        print()
        print (f"Code mauvais, il vous reste {restant} tentative ")
else:
    print("Carte bloquée après 3 codes PIN incorrects.")
    print("Au revoir")
while code == comptes[identifiant]["pin"]:
    print()
    print("-----QUE VOULEZ VOUS FAIRE-----")
    print("-------------TAPEZ-------------")
    print("1-pour voir votre solde")
    print("2-pour retirer de l'argent")
    print("3-pour deposer de l'argent") 
    print("4-pour quitter")
    print("-------------------------------")
    
    choix = input("votre choix:")
    print()
    if choix == "1": 
        print(f"Votre solde est de {solde}€") 
    elif choix == "2":
        montant = float(input("Montant à retirer (en euros) : ")) 
        print()
        if montant<=0:
            print("Erreur : le montant doit être un entier positif.") 
        elif montant > solde:
            print("Retrait refusé : solde insuffisant.")
        elif montant > PLAFOND_RETRAIT:
            print(f"Retrait refusé : le plafond est de {PLAFOND_RETRAIT} € par retrait.")
        else:
            if montant % 10 == 0:
                print(f"Retrait accepté : {montant} €")
                print()
                print("-----------Votre Choix-----------")
                if montant >= 80:
                    print("1-billets de 50€ , 20€ et 10€ " )
                if montant >= 30:
                    print("2-billets de 20€ et 10€")
                print("3-uniquement billets de 10€")
                if montant % 20 == 0:
                    print("4-uniquement des billets de 20€")
                if montant % 50 == 0 :
                    print("5-uniquement de billets de 50€")
                print("-----------De Retrait------------")
                choix_billets = input("Votre choix:")
                if choix_billets == "1":
                    billet_50 = montant // 50
                    if montant % 50 >= 0:
                        if billet_50 > 0:
                            print(f"{billet_50} billets de 50 €")
                    reste1 = montant - billet_50*50
                     
                    if reste1 % 20 >= 0:
                        billet_20 = reste1 // 20 
                        if billet_20 > 0:
                            print(f"{billet_20} billets de 20 €")
                    reste2 = reste1 - billet_20*20
                        
                    if reste2 % 10 >= 0:
                        billet_10 = reste2 // 10 
                        if billet_10 > 0 :
                            print(f"{billet_10} billets de 10 €")
                         
                if choix_billets == "2":
                    billet_20 = montant // 20
                    print(f"{billet_20} billets de 20 €")
                    reste1 = montant - billet_20*20
                    
                    billet_10 = reste1 // 10
                    print(f"{billet_10} billets de 10 €")
                    
                if choix_billets == "3":
                    billet_10 = montant // 10
                    print(f"{billet_10} billets de 10 €")
                    
                if choix_billets == "4":
                    billet_20 = montant // 20
                    print(f"{billet_20} billets de 20 €")
                    
                if choix_billets == "5":
                    billet_50 = montant // 50
                    print(f"{billet_50} billets de 50 €")
            else:            
                print(f"Retrait accepté : {montant} €.")
                billet_50 = montant // 50
                if montant % 50 >= 0:
                    if billet_50 > 0:
                        print(f"{billet_50} billets de 50 €")
                reste = montant - billet_50*50
                reste = round(reste, 2)
                
                if reste % 20 >= 0:
                    billet_20 = reste // 20 
                    if billet_20 > 0:
                        print(f"{billet_20} billets de 20 €")
                reste = reste - billet_20*20
                reste = round(reste, 2)
                
                if reste % 10 >= 0:
                    billet_10 = reste // 10 
                    if billet_10 > 0 :
                        print(f"{billet_10} billets de 10 €")
                reste = reste - billet_10*10
                reste = round(reste, 2)
                
                if reste % 5 >= 0:
                    billet_5 = reste // 5
                    if billet_5 > 0:
                        print(f"{billet_5} billets de 5 €")
                reste = reste - billet_5*5
                reste = round(reste, 2)
                
                if reste % 2 >= 0:
                    piece_2 = reste // 2
                    if piece_2 > 0:
                        print(f"{piece_2} piece de 2 €")
                reste = reste - piece_2*2
                reste = round(reste, 2)
                
                if reste % 1 >= 0:
                    piece_1 = reste // 1
                    if piece_1 > 0:
                        print(f"{piece_1} piece de 1 €")
                reste = reste - piece_1*1
                reste = reste * 100
                piece_0_5 = reste // 50
                if piece_0_5 > 0:
                    print(f"{piece_0_5} piece de 50 centime")
                reste = reste - piece_0_5*50
                reste = round(reste, 2)
                
                piece_0_2 = reste // 20
                if piece_0_2 > 0:
                    print(f"{piece_0_2} piece de 20 centime")
                reste = reste - piece_0_2*20
                reste = round(reste, 2)
                
                piece_0_1 = reste // 10
                if piece_0_1 > 0:
                    print(f"{piece_0_1} piece de 10  centime")
                reste = reste - piece_0_1*10
                reste = round(reste, 2)
                
                piece_0_0_5 = reste // 5
                if piece_0_0_5 > 0:
                    print(f"{piece_0_0_5} piece de 5 centime")
                reste = reste - piece_0_0_5*5
                reste = round(reste, 2)
                
                piece_0_0_2 = reste // 2
                if piece_0_0_2 > 0:
                    print(f"{piece_0_0_2} piece de 2 centime")
                reste2 = reste - piece_0_0_2*2
                reste2 = round(reste2, 2)
                
                if reste2 == 1:
                    piece_0_0_1 = 1.0
                    print(f"{piece_0_0_1} piece de 1 centime")
            solde = solde - montant
            solde = round(solde, 2)
            comptes[identifiant]["solde"] = solde
            print()
            print(f"Votre nouveau solde est de {solde} €.")
            print()
    elif choix == "3":
        montant_depose = float(input("Montant à déposer (en euros) : "))
        if montant_depose <= 0:
            print("Erreur : le montant à déposer doit être un entier positif.")
        else:
            solde = solde + montant_depose
            comptes[identifiant]["solde"] = solde
            print()
            print(f"Dépot accepté : {montant_depose} €")
            print()
            print(f"Votre nouveau solde est de {solde} €.")
            print()
    elif choix == "4":
        print("Au revoir")
        break
    else:
        print ("il y a seulement 4 choix, réessayez")
