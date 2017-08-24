def tri_rapide(tableau):
    '''tri_rapide (list(object) -> list(object)) : renvoie le tableau trié'''
    
    # Si le tableau est vide ou ne contient qu'un seul élément, il est trié
    if len(tableau) == 1 or len(tableau) == 0:
        return tableau
    # Sinon
    else:
        # On choisit arbitrairement un pivot
        '''pivot(int) : valeur à laquelle on va comparer les éléments du tableau'''
        pivot = tableau[0]
        '''place(int) : index de la valeur à remplacer si on trouve un élément
        plus petit que pivot'''
        place = 0
        # On parcourt le tableau
        for j in range(len(tableau)-1):
            if tableau[j+1] < pivot:
                tableau[j+1],tableau[place+1] = tableau[place+1], tableau[j+1]
                place += 1
        tableau[0],tableau[place] = tableau[place],tableau[0]
        first_part = tri_rapide(tableau[:place])
        second_part = tri_rapide(tableau[place+1:])
        first_part.append(tableau[place])
        return first_part + second_part
        
alist = [54,26,93,17,77,31,44,55,20]
tri_rapide(alist)
print(alist)