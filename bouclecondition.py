#Boucles et Conditions
#• Demande à l’utilisateur d’entrer un nombre entier n.
n = int(input("Entrez un nombre entier: "))
#• Calcule et affiche la somme des 10nombres pairs de 1 à n.
somme = 0
for i in range(1, n+1):
    if i % 2 == 0:
        somme += i
print(f"La somme des nombres pairs de 1 à {n} est {somme}")
#• Génère un nombre aléatoire entre 1 et 20. (Utilise random.randint(1, 20))
import random
nombre_aleatoire = random.randint(1, 20)
#• Demande à l’utilisateur de deviner ce nombre.
devine = int(input("Devinez le nombre aléatoire: "))
#• Affiche "Trop grand" ou "Trop petit" jusqu'à ce qu'il trouve la bonne réponse.
while devine != nombre_aleatoire:
    if devine > nombre_aleatoire:
        print("Trop grand")
    else:
        print("Trop petit")
    devine = int(input("Devinez le nombre aléatoire: "))
print("Bravo, vous avez trouvé le nombre aléatoire!")
