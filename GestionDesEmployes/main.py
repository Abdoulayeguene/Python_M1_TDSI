# Importer les fonctions du module employe
from employe import ajouter_employe, modifier_employe, supprimer_employe, afficher_employes

# Créer une liste vide pour stocker les employés
liste_employes = []

# Boucle principale du menu
while True:
    print("\n--- Menu de gestion des employés ---")
    print("1. Ajouter un employé")
    print("2. Modifier un employé")
    print("3. Supprimer un employé")
    print("4. Afficher tous les employés")
    print("5. Quitter le programme")

    # Demander le choix de l'utilisateur
    choix = input("Entrez votre choix (1-5) : ").strip()

    if choix == '1':
        # Appeler la fonction pour ajouter un employé
        ajouter_employe(liste_employes)
    elif choix == '2':
        # Appeler la fonction pour modifier un employé
        modifier_employe(liste_employes)
    elif choix == '3':
        # Appeler la fonction pour supprimer un employé
        supprimer_employe(liste_employes)
    elif choix == '4':
        # Appeler la fonction pour afficher tous les employés
        afficher_employes(liste_employes)
    elif choix == '5':
        # Quitter le programme
        print("Au revoir !")
        break
    else:
        # Gérer le cas d'une saisie invalide
        print("Choix invalide. Veuillez entrer un nombre entre 1 et 5.")
