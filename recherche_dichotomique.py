def recherche_dichotomique(tableau, element):
    return _recherche_dichotomique(tableau, element, 0, len(tableau) - 1)

def _recherche_dichotomique(tableau, element, premier, dernier):
    '''recherche_dichotomique (list(object) * object * int * int-> int) :
    renvoie l'indice de l'élément dans le tableau préalablement trié'''
    
    # Initialisation
    '''milieu (int) : indice de la valeur médiane du sous-tableau allant de
    l'indice premier à l'indice dernier'''
    milieu = (premier + dernier) // 2
    
    # Début du traitement
    if element > tableau[milieu]:
        return _recherche_dichotomique(tableau, element, milieu + 1, dernier)
    elif element < tableau[milieu]:
        return _recherche_dichotomique(tableau, element, premier, milieu - 1)
    elif element == tableau[milieu]:
        return milieu
    else:
        return False

    
print(recherche_dichotomique([1,2,3,4,5],3))
    
        