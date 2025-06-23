# Dictionnaire pour stocker les informations des personnes
personnes = {}

def ajouter_personne():
    """Ajoute une nouvelle personne au dictionnaire"""
    while True:
        nom = input("Entrez le nom de la personne : ")
        
        # Vérifier si la personne existe déjà (insensible à la casse)
        nom_lower = nom.lower()
        nom_existe = any(existing_nom.lower() == nom_lower for existing_nom in personnes.keys())
        
        if nom_existe:
            print("Erreur : Cette personne existe déjà dans le système (même nom, majuscules/minuscules ignorées).")
            continue
        
        # Si le nom n'existe pas, on sort de la boucle
        break
    
    # Demander les autres informations
    age = input("Entrez l'âge : ")
    adresse = input("Entrez l'adresse : ")
    email = input("Entrez l'email : ")
    telephone = input("Entrez le numéro de téléphone : ")
    
    # Stocker les informations dans le dictionnaire
    personnes[nom] = {
        "âge": age,
        "adresse": adresse,
        "email": email,
        "téléphone": telephone
    }
    print(f"La personne {nom} a été ajoutée avec succès.")

def modifier_personne():
    """Modifie les informations d'une personne existante"""
    nom = input("Entrez le nom de la personne à modifier : ")
    
    if nom not in personnes:
        print("Erreur : Cette personne n'existe pas dans le système.")
        return
    
    print(f"\nModification des informations pour {nom}")
    print("Laissez vide pour conserver la valeur actuelle.")
    
    # Demander les nouvelles informations
    age = input(f"Nouvel âge [{personnes[nom]['âge']}] : ") or personnes[nom]['âge']
    adresse = input(f"Nouvelle adresse [{personnes[nom]['adresse']}] : ") or personnes[nom]['adresse']
    email = input(f"Nouvel email [{personnes[nom]['email']}] : ") or personnes[nom]['email']
    telephone = input(f"Nouveau téléphone [{personnes[nom]['téléphone']}] : ") or personnes[nom]['téléphone']
    
    # Mettre à jour les informations
    personnes[nom] = {
        "âge": age,
        "adresse": adresse,
        "email": email,
        "téléphone": telephone
    }
    print(f"Les informations de {nom} ont été mises à jour avec succès.")

def supprimer_personne():
    """Supprime une personne du dictionnaire"""
    nom = input("Entrez le nom de la personne à supprimer : ")
    
    if nom not in personnes:
        print("Erreur : Cette personne n'existe pas dans le système.")
        return
    
    del personnes[nom]
    print(f"La personne {nom} a été supprimée avec succès.")

def afficher_personne():
    """Affiche les informations d'une personne spécifique"""
    nom = input("Entrez le nom de la personne à afficher : ")
    
    if nom not in personnes:
        print("Erreur : Cette personne n'existe pas dans le système.")
        return
    
    print(f"\nInformations de {nom}:")
    for cle, valeur in personnes[nom].items():
        print(f"{cle.capitalize()}: {valeur}")

def afficher_toutes_personnes():
    """Affiche les informations de toutes les personnes"""
    if not personnes:
        print("Aucune personne n'est enregistrée dans le système.")
        return
    
    print("\nListe de toutes les personnes :")
    for nom, infos in personnes.items():
        print(f"\n{nom}:")
        for cle, valeur in infos.items():
            print(f"  {cle.capitalize()}: {valeur}")

def menu():
    """Affiche le menu principal et gère les choix de l'utilisateur"""
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Ajouter une nouvelle personne")
        print("2. Modifier une personne existante")
        print("3. Supprimer une personne")
        print("4. Afficher les informations d'une personne")
        print("5. Afficher toutes les personnes")
        print("6. Quitter")
        
        choix = input("\nEntrez votre choix (1-6) : ")
        
        if choix == "1":
            ajouter_personne()
        elif choix == "2":
            modifier_personne()
        elif choix == "3":
            supprimer_personne()
        elif choix == "4":
            afficher_personne()
        elif choix == "5":
            afficher_toutes_personnes()
        elif choix == "6":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    menu()
