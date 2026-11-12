 
import random
import sys
print("===================================")
print("===================================")
print("======DISTRIBUTEUR DE BILLETS======")
print("===================================")
print("===================================")
sentence = ""
argent = random.randint(0, 4753)
answer=int(input("Bonjour. Possedez-vous déjà un compte bancaire?(0=Oui/1=Non) : "))
if answer==0:
    familyname = str(input("Entrez votre identifiant de compte : "))

    if familyname == "Monnier":
        argent = -993
        sentence = "Vous êtes a decouvert et ne pouvez donc pas retirer d'argent.\nOn se revoit en fin de mois."
        pin = int(input("Entrez votre PIN : "))
        while pin != 6732:
            print("PIN incorrect. Veuillez reessayer.")
            pin = int(input("Entrez votre PIN : "))
            
    else:
        print("Votre identifiant ne figure pas dans notre base de données. Au revoir")
        sys.exit()
elif answer==1:
    
    answer=int(input("Souhaitez-vous créer un compte?(0=Oui/1=Non) : "))
    if answer == 0:
        account_name = input("Veuillez definir un identifiant de compte : ")
        account_pin = int(input("Veuillez definir un mot de passe : "))
        print("Votre compte à ete créé avec succès. Saisissez votre identifiant et mot de passe pour vous y connecter.")
        familyname = str(input("Entrez votre identifiant de compte : "))
        
        if familyname == account_name:
            pin = int(input("Entrez votre PIN : "))
            while pin != account_pin:
                print("PIN incorrect. Veuillez reessayer.")
                pin = int(input("Entrez votre PIN : "))
        else:
            print("Votre identifiant ne figure pas dans notre base de données.")
            answer=int(input("Souhaitez-vous créer un compte?(0=Oui/1=Non) : "))
    elif answer ==1:
        print("Merci de votre visite. Au revoir.")
        sys.exit()
    else:
        print("Veuillez choisir un nombre entre 0 (Oui) et 1 (Non). ")
        answer=int(input("Souhaitez-vous créer un compte?(0=Oui/1=Non) : "))
        


else:
    print("Au revoir.")
    sys.exit()
print("Connection effectuée avec succès")
print(f"Vous avez {argent}€ sur votre compte.{sentence}")
if argent <0:
    sys.exit()
answer = int(input("Le plafond s'eleve à 999€. Voulez vous retirer de l'argent ?(0=Oui/1=Non) : "))
if answer == 0:
    while True:
        argent_a_retirer = int(input("Combien d'argent voulez-vous retirer ? : "))

        if argent_a_retirer <= 0 or argent_a_retirer > argent:
            print("Montant incorrect.")

        elif argent_a_retirer > 999:
            print("Montant supérieur au plafond. Le plafond est de 999€.")

        else:
            break
elif answer==1:
    print("Au revoir.")
else:
    print("Veuillez choisir entre 0 et 1")
    answer = int(input("Voulez vous retirer de l'argent ?(0/1) : "))
    
bill100 = argent_a_retirer//100
reste = argent_a_retirer%100

bill50 = reste//50
reste = reste%50

bill20 = reste//20
reste = reste%20

bill10 = reste//10
reste = reste%10

bill5 = reste//5 
reste = reste%5

coin2 = reste//2
reste = reste%2

coin1 = reste//1


print("Billet(s) distribué(s) : ")
if bill100 > 0:
    print(bill100, "billet(s) de 100 €")
if bill50 > 0:
    print(bill50, "billet(s) de 50 €")
if bill20 > 0:
    print(bill20, "billet(s) de 20 €")
if bill10 > 0:
    print(bill10, "billet(s) de 10 €")
if bill5 > 0:
    print(bill5, "billet(s) de 5€")
if coin2 > 0:
    print(coin2, "pièce(s) de 2€")
if coin1 > 0:
    print(coin1, "pièce(s) de 1€")
print("Merci de vortre visite. ")
print(f"Il reste {argent-argent_a_retirer}€ sur votre compte. Au revoir.")