def tri_fusion(tableau):
    # list(object) -> list(object)
    # renvoie tableau trié
    # On présume que object implémente une méthode de comparaison à elle-même
    
    # Initialisation
    # taille (int) : nombre d'éléments dans tableau
    taille = len(tableau)
    
    # milieu (int) : index médian du tableau
    milieu = taille // 2
    
    # gauche (list(object)) : moitié gauche du tableau (comportant les éléments
    # de 0 à milieu - 1)
    gauche = []
    
    # droite (list(object)) : moitié droite du tableau (comportant les éléments
    # de milieu à taille)
    droite = []
    
    # Début du traitement
    
    # Si tableau ne comporte qu'un élément, on le renvoie
    if taille == 1:
        return tableau
    
    # Sinon, on le divise en deux, puis on va trier chacune des 2 moitiés, ce
    # qui fait que dans un premier temps, on va sans arrêt diviser, jusqu'à
    # obtenir des tableaux d'un seul élément, puis on va les trier
    # et fusionner successivement
    gauche = tableau[:milieu]
    droite = tableau[milieu:]
    
    # On redivise les tableaux
    gauche = tri_fusion(gauche)
    droite = tri_fusion(droite)
    
    # À ce stade, on aura ou des tableaux à un seul élément, ou des tableaux
    # triés
    return fusion(gauche, droite)
    
def fusion(gauche, droite):
    # list(object) * list(object) -> list(object)
    # renvoie le tableau résultant de la fusion de gauche et droite
    # On présume que gauche et droite sont triés et que object implémente une
    # méthode de comparaison à elle-même
    
    # Initialisation
    # tableau (list(object)) : tableau fusionné
    tableau = []
    
    # taille_gauche (int) : nombre d'éléments dans gauche
    taille_gauche = len(gauche)
    
    # taille_droite (int) : nombre d'éléments dans droite
    taille_droite = len(droite)
    
    # element (int) : élément que l'on va rajouter à tableau
    element = None
    
    # Début du traitement
    # Tant que chaque tableau a au moins 1 élément, on ajoute le plus petit
    # élément situé à l'index 0 au tableau fusionné
    while taille_gauche >= 1 and taille_droite >= 1:
        # Si le premier élément de gauche est plus petit que celui de droite,
        # on le supprime de gauche et on l'ajoute à tableau
        if gauche[0] < droite[0]:
            element = gauche.pop(0)
            tableau.append(element)
            taille_gauche -= 1
        # Sinon, c'est que c'est celui de droite que est plus petit, c'est donc
        # lui que l'on va ajouter au tableau
        else:
            element = droite.pop(0)
            tableau.append(element)
            taille_droite -= 1
    
    # À ce stade, au moins un tableau est vide entre gauche ou droite. Il faut
    # donc ajouter les éléments restants à tableau.
    tableau.extend(gauche)
    tableau.extend(droite)
    
    return tableau
    
power = [4,2,0,1]
print(tri_fusion(power))