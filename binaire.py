def binaire(entier):
    '''binaire (int -> list(int)) : renvoie l'écriture en base 2 de entier'''
    #Initialisation
    '''base_2 (list(int)) : contient la représentation en base 2 de entier'''
    base_2 = []
    '''puissances_2 (list(int)) : contient les puissances de 2 successives'''
    puissances_2 = [1]
    '''derniere_puissance (int) : dernière puissance calculée'''
    derniere_puissance = puissances_2[-1]
    '''puissance_en_cours (int) : puissance en cours d'analyse'''
    puissance_en_cours = 0
    
    #Début du traitement
    #On remplit le tableau des puissances de 2
    #Tant que la plus grande puissance de 2 calculée est inférieure à entier,
    #on remplit le tableau
    while derniere_puissance < entier:
        #On double la dernière puissance calculée
        derniere_puissance *= 2
        puissances_2.append(derniere_puissance)
    #À ce stade, puissances_2 contient toutes les puissances nécessaires pour
    #écrire entier en base 2.
    #On parcourt puissances_2 à partir de la plus haute puissance, puis, si
    #cet élément est plus petit que entier, on le soustrait à entier, et on
    #stocke un 1 à son emplacement. Sinon, on stocke 0 et on ne fait rien.
    while puissances_2 != []:
        puissance_en_cours = puissances_2.pop()
        if entier - puissance_en_cours >= 0:
            entier -= puissance_en_cours
            base_2.append(1)
        else:
            base_2.append(0)
    return base_2
    
print(binaire(10))