def tri_selection(tableau):
    '''tri_selection (list(object) -> list(object)): trie un tableau'''
    # Initialisation
    '''taille (int) : taille du tableau'''
    taille = len(tableau)
    
    # Début du traitement
    # Pour chaque élément tableau[i] du tableau
    for i in range(taille):
        # Pour chaque j allant de l'élément actuel tableau[i] jusqu'à la fin du
        # tableau, on vérifie si c'est le plus petit
        for j in range(i, taille):
            if tableau[j] < tableau[i]:
                tableau[i], tableau[j] = tableau[j], tableau[i]
    return tableau
    
print(tri_selection([3,2,1,4,8,4,10,9,8,32,91]))