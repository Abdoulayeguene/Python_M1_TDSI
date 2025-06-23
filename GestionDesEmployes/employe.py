def ajouter_employe(liste_employes):
    """
    Ajoute un employé à la liste après validation des entrées.
    """
    while True:
        try:
            # Demander le nom de l'employé
            nom = input("Entrez le nom de l'employé : ").strip()
            # Vérifier que le nom n'est pas vide
            if not nom:
                print("Le nom ne doit pas être vide.")
            else:
                print("Le nom est valide.")

            # Demander l'âge de l'employé
            age_str = input("Entrez l'âge de l'employé : ").strip()
            # Convertir l'âge en entier
            age = int(age_str)
            # Vérifier que l'âge est positif
            if age <= 0:
                print("L'âge doit être un entier positif.")
            else:
                print("L'âge est valide.")

            # Demander le poste de l'employé
            poste = input("Entrez le poste de l'em1ployé : ").strip()
            # Vérifier que le poste n'est pas vide
            if not poste:
                print("Le poste ne doit pas être vide.")
                continue

            # Créer un dictionnaire pour l'employé
            employe = {"nom": nom, "age": age, "poste": poste}
            # Ajouter l'employé à la liste
            liste_employes.append(employe)
            # Confirmer l'ajout
            print(f"Employé {nom} ajouté avec succès !")
            # Sortir de la boucle après un ajout réussi
            break
        except ValueError:
            # Gérer le cas où l'âge n'est pas un entier
            print("Veuillez entrer un âge valide (nombre entier positif).")

def modifier_employe(liste_employes):
    """
    Modifie les informations d'un employé existant.
    """
    # Demander le nom de l'employé à modifier
    nom = input("Entrez le nom de l'employé à modifier : ").strip()
    # Chercher l'employé dans la liste
    for employe in liste_employes:
        if employe["nom"].lower() == nom.lower():
            # Afficher les informations actuelles
            print(f"Informations actuelles : Nom = {employe['nom']}, Âge = {employe['age']}, Poste = {employe['poste']}")
            while True:
                try:
                    # Demander le nouveau nom (laisser vide pour ne pas changer)
                    nouveau_nom = input("Nouveau nom (laisser vide pour ne pas changer) : ").strip()
                    if nouveau_nom:
                        employe["nom"] = nouveau_nom
                    # Demander le nouvel âge (laisser vide pour ne pas changer)
                    nouvel_age_str = input("Nouvel âge (laisser vide pour ne pas changer) : ").strip()
                    if nouvel_age_str:
                        nouvel_age = int(nouvel_age_str)
                        if nouvel_age <= 0:
                            print("L'âge doit être un entier positif.")
                            continue
                        employe["age"] = nouvel_age
                    # Demander le nouveau poste (laisser vide pour ne pas changer)
                    nouveau_poste = input("Nouveau poste (laisser vide pour ne pas changer) : ").strip()
                    if nouveau_poste:
                        employe["poste"] = nouveau_poste
                    # Confirmer la modification
                    print("Informations de l'employé modifiées avec succès !")
                    break
                except ValueError:
                    # Gérer le cas où l'âge n'est pas un entier
                    print("Veuillez entrer un âge valide (nombre entier positif) ou laisser vide.")
            return
    # Si l'employé n'est pas trouvé
    print(f"Aucun employé trouvé avec le nom '{nom}'.")

def supprimer_employe(liste_employes):
    """
    Supprime un employé de la liste selon son nom.
    """
    # Demander le nom de l'employé à supprimer
    nom = input("Entrez le nom de l'employé à supprimer : ").strip()
    # Parcourir la liste pour trouver l'employé
    for i, employe in enumerate(liste_employes):
        # Comparer les noms sans tenir compte de la casse
        if employe["nom"].lower() == nom.lower():
            # Afficher les informations de l'employé trouvé
            print(f"Employé trouvé : Nom = {employe['nom']}, Âge = {employe['age']}, Poste = {employe['poste']}")
            # Demander confirmation avant suppression
            confirmation = input("Voulez-vous vraiment supprimer cet employé ? (o/n) : ").strip().lower()
            if confirmation == 'o':
                # Supprimer l'employé de la liste
                del liste_employes[i]
                print(f"Employé {nom} supprimé avec succès !")
            else:
                print("Suppression annulée.")
            return
    # Si l'employé n'est pas trouvé
    print(f"Aucun employé trouvé avec le nom '{nom}'.")

def afficher_employes(liste_employes):
    """
    Affiche tous les employés de la liste avec leurs informations.
    """
    # Vérifier si la liste est vide
    if not liste_employes:
        print("Aucun employé à afficher.")
        return
    # Parcourir la liste des employés
    for i, employe in enumerate(liste_employes, start=1):
        # Afficher les informations de chaque employé
        print(f"Employé {i} :")
        print(f"  Nom   : {employe['nom']}")
        print(f"  Âge   : {employe['age']}")
        print(f"  Poste : {employe['poste']}")
        print("-----------------------------")
