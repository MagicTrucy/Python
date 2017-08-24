def diviseurs_stricts(entier):
    '''diviseurs_stricts (int -> list(int)) : renvoie la liste des diviseurs
    stricts de entier'''
    
    # Initialisation
    '''jej'''
    diviseurs = []
    
    # Pour chaque nombre de 1 à entier, on teste si le reste de la division
    # de entier par i est nul. S'il l'est, i est un diviseur de entier
    for i in range(1, entier):
        if entier % i == 0:
            diviseurs.append(i)
    return diviseurs