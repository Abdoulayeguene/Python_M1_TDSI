#3. Dictionnaires : Création et Modification

#Crée un dictionnaire contenant ces informations :
personne = {"nom":"Alice", "age":25, "ville":"Paris"}

#Affiche l'âge de la personne.
print(personne["age"])

#Modifie l'âge d'Alice pour 26 ans.
personne["age"]=26
print(f"l'age de la personne est: {personne["age"]}")

#Ajoute une nouvelle clé "profession" avec la valeur "Ingénieur".
personne["profession"]="Ingénieur"
print(f"la profession de la personne est: {personne["profession"]}")

#Supprime la clé "ville".
print(personne)
del(personne["ville"])
print(personne)

#Affiche toutes les clés du dictionnaire.
print(personne.keys())

#Affiche toutes les valeurs du dictionnaire.
print(personne.values())

#Affiche toutes les clés et valeurs du dictionnaire.
print(personne.items())

#Vérifie si la clé "age" existe dans le dictionnaire.
print("age" in personne)

#Vérifie si la clé "ville" existe dans le dictionnaire.
print("ville" in personne)
#afficcer chaque cles avec sa valeur
for keys, value  in personne.items():
    print(f"{keys} : {value}")

#Exercice 3.2 : Dictionnaires et boucles
# Parcours le dictionnaire et affiche chaque clé et valeur.
for i in personne:
    print(f"{i} : {personne[i]}")


