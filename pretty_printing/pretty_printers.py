import time

for i in range(5, 0, -1):
   print(f"Compte à rebours : {i}", end="\r", flush=True)
   time.sleep(1)
print("Terminé !          ")

val = input("Choisissez une valeur entière entre 0 et 4: ")
print("\033[1A\033[J", end="")
val1 = input("Choisissez une valeur entière entre 5 et 10: ")
print("\033[1A\033[J", end="")   # remonte de 2 lignes et efface jusqu'en bas

print(f"Vous avez choisi d'abord {val}, puis {val1}", end="\r", flush=True)
time.sleep(2)
print("\033[K" + "A bientôt.")   # efface la ligne avant d'écrire

