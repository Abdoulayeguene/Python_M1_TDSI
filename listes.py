#Crée une liste avec ces éléments : ["pomme", "banane", "orange", "kiwi"]
liste = ["pomme", "banane", "orange", "kiwi"]
print("Crée une liste avec ces éléments : ", liste) 
#Ajoute "fraise" à la fin de la liste.
liste.append("fraise")
print("Ajoute fraise à la fin de la liste : ", liste) 
#Supprime "orange"
#liste.remove("orange")
#print("Supprime orange : ", liste)
#Trie la liste par ordre alphabétique.
liste.sort()   
print("Trie la liste par ordre alphabétique : ", liste) 
n = len(liste)
for i in range(n):
    for j in range(0, n - i - 1):
        if liste[j] > liste[j + 1]:  # Comparaison lexicographique
            liste[j], liste[j + 1] = liste[j + 1], liste[j]  # Échange des éléments
# Affiche la liste triée
print(liste)  

#Exercice 2.2 : Boucles et affichage
# Parcours la liste et affiche chaque élément en majuscules. (ne pas utiliser upper())
for i in liste:
    print(i.upper())
# Parcours la liste et affiche chaque élément avec son indice.
for i in range(len(liste)):
    print(i, liste[i])

