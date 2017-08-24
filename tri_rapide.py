def partitionner(tableau, premier_index, dernier_index, pivot):
    '''partitionner (list(object) * int * int * int -> int) : place les valeurs
    inférieures à tableau[pivot] à gauche du tableau (à partir de premier_index)
    Renvoie la position du pivot à la fin du traitement.'''
    
    # Initialisation
    
    # On place le pivot à une place arbitraire (ici, la fin du tableau)
    tableau[pivot], tableau[dernier_index] = tableau[dernier_index], tableau[pivot]
    
    '''place (int) : index du prochain emplacement où mettre une valeur
    inférieure à tableau[dernier_index]'''
    place = premier_index + 1
    # Pour chaque index dans le sous-tableau entre premier_index et
    # dernier_index inclus
    for i in range(premier_index, dernier_index + 1):
        # Si l'élément que l'on est en train de parcourir est plus petit que
        # tableau[dernier_index] (le pivot donc), on le met à l'index place
        if tableau[i] <= tableau[dernier_index]:
            tableau[i], tableau[place] = tableau[place], tableau[i]
            place += 1
    # Une fois qu'on a parcouru le sous-tableau, on a donc tous les éléments
    # dans des indexes inférieurs à place qui sont inférieurs au pivot. On peut
    # donc placer le pivot juste après eux.
    # On effectue cette opération seulement si elle est faisable
    if place <= dernier_index:
        tableau[dernier_index], tableau[place] = tableau[place], tableau[dernier_index]
    return place

def tri_rapide(tableau, premier_index, dernier_index):
    '''tri_rapide (list(object) * int * int -> None : trie
    effectivement le tableau en le partitionnant autour d'un pivot, puis en
    appelant tri_rapide sur chacune des sous-parties à gauche et à droite du
    pivot du tableau'''
    
    # Initialisation
    
    '''pivot (int) : index du pivot choisi. Ici il est choisi arbitrairement.'''
    pivot = premier_index
    
    # Début du traitement
    # On s'assure que les arguments sont corrects
    if premier_index < dernier_index:
        pivot = partitionner(tableau, premier_index, dernier_index, pivot)
        tri_rapide(tableau, premier_index, pivot - 1)
        tri_rapide(tableau, pivot + 1, dernier_index)

def tri_rapide_initialisation(tableau):
    '''tri_rapide_initialisation(list(object) -> list(object)): renvoie le
    tableau trié. Cette fonction n'est qu'une fonction d'initialisation qui va
    faire appel aux vraies fonctions de traitement avec les arguments corrects'''
    
    # Initialisation
    
    '''premier_index(int): premier index du tableau'''
    premier_index = 0
    '''dernier_index(int): dernier index du tableau'''
    dernier_index = len(tableau) - 1
    
    # Traitement
    return tri_rapide(tableau, premier_index, dernier_index)
    
    
lel = [5,4,3,2,1]
print(tri_rapide_initialisation(lel))