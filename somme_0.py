
import random
argent = random.randint(-500, 1694)
print("Bonjour. Possedez-vous déjà un compte bancaire?(0=Oui/1=Non)" )
pin = int(input("Entrez votre PIN :"))
while pin != 6732:
    print("PIN incorrect. Veuillez reessayer.")
    pin = int(input("Entrez votre PIN :"))
print(f"Vous avez {argent}€ sur votre compte.")
answer = int(input("Voulez vous retirer de l'argent ?(0=Oui/1=Non):"))
if answer==0:
    argent_a_retirer=int(input("Combien d'argent voulez vous retirer?"))
    if argent_a_retirer<=0 or argent_a_retirer > argent:
        print("Montant incorrect")
        argent_a_retirer=int(input("Combien d'argent voulez vous retirer?"))
    elif argent_a_retirer>=1000:
        print("Montant superieur au plafond. Le plafond est de 1000€.")
        argent_a_retirer=int(input("Combien d'argent voulez vous retirer?"))
    elif argent_a_retirer%1 !=0:
        print("Ce distributeur ne delivre que des billets. Veuillez choisir un montant multiple du nombre 5.")
        argent_a_retirer=int(input("Combien d'argent voulez vous retirer?"))
    else:
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

        coin1 = reste//2


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
        print("Merci de vortre visite. Au revoir.")
elif answer==1:
    print("Au revoir.")
else:
    print("Veuillez choisir entre 0 et 1")
    answer = int(input("Voulez vous retirer de l'argent ?(0/1):"))
