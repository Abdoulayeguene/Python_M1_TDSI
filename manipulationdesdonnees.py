#4 Manipulation des Données
# #Demande à l’utilisateur d’entrer son nom.
nom = input("Entrez votre nom: ")
# #Demande à l’utilisateur d’entrer son prénom.
prenom = input("Entrez votre prénom: ")
# #Affiche le nom et le prénom.
print(f"Bonjour {nom} {prenom}")

#Affiche le nom en majuscules et en minuscules. (Sans utiliser upper ni lower)
print(nom.upper())
print(nom.lower())
dictionnaires_alphabet = {"a": "A", "b": "B", "c": "C", "d": "D", "e": "E", "f": "F", "g": "G", "h": "H", "i": "I", "j": "J", "k": "K", "l": "L", "m": "M", "n": "N", "o": "O", "p": "P", "q": "Q", "r": "R", "s": "S", "t": "T", "u": "U", "v": "V", "w": "W", "x": "X", "y": "Y", "z": "Z"}
# Majuscules
nom_maj = ""
for lettre in nom.lower():
    if lettre in dictionnaires_alphabet:
        nom_maj += dictionnaires_alphabet[lettre]
    else:
        nom_maj += lettre
print(f"nom maj {nom_maj}")

# Minuscules
nom_min = ""
for lettre in nom.upper():
    if lettre in dictionnaires_alphabet.values():
        for k, v in dictionnaires_alphabet.items():
            if v == lettre:
                nom_min += k
    else:
        nom_min += lettre
print(f"nom min {nom_min}")
    
#Affiche la longueur du nom.
print(len(nom))
#Étant donné la liste suivante :
nombres = [10, 23, 45, 66, 75, 90, 101]
#Affiche le nombre de valeurs dans la liste.
print(len(nombres))
#Affiche la valeur maximale de la liste.
print(max(nombres))
#Affiche la valeur minimale de la liste.
print(min(nombres))
#Crée une nouvelle liste contenant uniquement les nombres pairs.
for nombres_pairs in nombres:
    if nombres_pairs % 2 == 0:
        print(nombres_pairs)

#Crée une nouvelle liste contenant uniquement les nombres impairs.
nombres_impairs = [i for i in nombres if i % 2 != 0]
print(nombres_impairs)
