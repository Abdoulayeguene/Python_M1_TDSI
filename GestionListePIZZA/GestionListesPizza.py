def gestion_pizzas():
    # Création de la liste vide
    pizza_list = []
    
    print("\nBienvenue dans le gestionnaire de pizzas!")
    print("Entrez les noms des pizzas (appuyez sur Entrée pour terminer)")
    
    while True:
        # Demande de saisie d'une pizza
        pizza = input("\nEntrez le nom d'une pizza: ").strip()
        
        # Vérification si l'utilisateur veut quitter
        if not pizza:
            break
            
        # Vérification si la pizza existe déjà (sans tenir compte de la casse)
        if any(p.lower() == pizza.lower() for p in pizza_list):
            print("ERREUR !!! La pizza saisie existe déjà.")
            continue
            
        # Ajout de la pizza à la liste
        pizza_list.append(pizza)
    
    # Affichage des résultats
    print("\n" + "="*50)
    print(f"Nombre total de pizzas: {len(pizza_list)}")
    
    if not pizza_list:
        print("La liste des pizzas est vide.")
    else:
        # Affichage du titre centré
        print(f"\n{'Liste des ' + str(len(pizza_list)) + ' pizzas':^50}")
        print("-"*50)
        
        # Affichage de la liste complète
        for pizza in pizza_list:
            print(f"- {pizza}")
            
        # Affichage de la première et dernière pizza
        print("\nPremière pizza:", pizza_list[0])
        print("Dernière pizza:", pizza_list[-1])
        
        # Affichage des trois premiers éléments
        print("\nLes trois premières pizzas:")
        for i, pizza in enumerate(pizza_list[:3], 1):
            print(f"{i}. {pizza}")

if __name__ == "__main__":
    gestion_pizzas()
