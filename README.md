# 2026_2027_nsi_prem_projet__dab
# projet de nsi : Abel, Henri et Tristan
Bonjour tt le monde 
print("Bonjour")


print("DISTRIBUTEUR DE BILLETS")

argent = int(input("Montant à retirer : "))

if argent <= 0:
    print("Montant invalide.")
elif argent % 10 != 0:
    print("Le montant doit être un multiple de 10.")
else:
    billets100 = argent // 100
    reste = argent % 100

    billets50 = reste // 50
    reste = reste % 50

    billets20 = reste // 20
    reste = reste % 20

    billets10 = reste // 10

    print("Billets distribués :")

    if billets100 > 0:
        print(billets100, "billet(s) de 100 €")

    if billets50 > 0:
        print(billets50, "billet(s) de 50 €")

    if billets20 > 0:
        print(billets20, "billet(s) de 20 €")

    if billets10 > 0:
        print(billets10, "billet(s) de 10 €")


voila ca normalement ca fonctionne 