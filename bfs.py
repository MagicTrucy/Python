def parcours(L, depart, arrivee):
    # parcours (list(list(int)) * int * int -> bool)
    # renvoie True s'il existe un chemin entre les sommets depart et arrivee

    # Initialisation
    # explores (list(int)) : contient les sommets déjà explorés
    explores = [depart]

    # a_explorer (list(int)) : contient les sommets à explorer
    a_explorer = [depart]

    # Tant qu'on a des sommets à explorer, on explore et rajoute les sommets
    # voisins à la liste a_explorer
    while len(a_explorer) >= 1:
        # sommet (int) : sommet en cours d'exploration
        sommet = a_explorer.pop(0)
        # On élimine le sommet de la liste des sommets à explorer

        # Si le sommet correspond à celui attendu, on peut renvoyer True
        if sommet == arrivee:
            return True

        # voisins (list(int)) : sommets voisins de sommet
        voisins = L[sommet]

        # Pour chaque voisin trouvé, s'il n'a pas été découvert, on le rajoute
        # dans la liste des sommets explorés et à explorer.
        # S'il a déjà été découvert, on ne fait rien.
        # Ainsi, on évite de boucler indéfiniment dans une boucle dans le graphe.
        for voisin in voisins:
            # Si le sommet voisin n'a jamais été exploré
            if not voisin in explores:
                explores.append(voisin)
                a_explorer.append(voisin)

    # Si après avoir exploré tout les chemins possibles à partir de depart on
    # n'a toujours pas trouvé le sommet arrive, c'est qu'il n'y a pas de chemin
    # entre depart et arrivee.
    return False

l = [[1,3],[0,2],[1],[0],[5],[4]]
dep = 0
arr = 4
print(parcours(l, dep, arr))
