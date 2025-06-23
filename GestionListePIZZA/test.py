
# Créer une liste vide pour stocker les employés
def ajouter_pizza(liste_pizzas):
    """
    Ajoute une pizza à la liste après validation des entrées.
    """
    while True:
        try:
            # Demander le nom de la pizza
            nom = input("Entrez le nom de la pizza : ").strip()
            # Vérifier que le nom n'est pas vide    
            if not nom:
                print("Le nom ne doit pas être vide.")
            else:
                print("Le nom est valide.")

            # Demander le prix de la pizza
            prix_str = input("Entrez le prix de la pizza : ").strip()
            # Convertir le prix en nombre flottant
            prix = float(prix_str)
            # Vérifier que le prix est positif
            if prix <= 0:
                print("Le prix doit être un nombre positif.")
            else:
                print("Le prix est valide.")

            # Demander la catégorie de la pizza
            categorie = input("Entrez la catégorie de la pizza : ").strip()
            # Vérifier que la catégorie n'est pas vide
            if not categorie:
                print("La catégorie ne doit pas être vide.")
            else:
                print("La catégorie est valide.")

            # Créer un dictionnaire pour la pizza
            pizza = {"nom": nom, "prix": prix, "categorie": categorie}
            # Ajouter la pizza à la liste
            liste_pizzas.append(pizza)
            # Confirmer l'ajout
            print(f"Pizza {nom} ajoutée avec succès !")
            # Sortir de la boucle après un ajout réussi
            break
        except ValueError:
            # Gérer le cas où le prix n'est pas un nombre flottant
            print("Veuillez entrer un prix valide (nombre flottant positif).")
