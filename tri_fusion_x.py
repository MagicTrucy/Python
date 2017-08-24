def tri_fusion(tableau):
    '''tri_fusion (list(object) -> list(object)) : renvoie tableau trié'''
    # Initialisation
    # taille (int) : taille de tableau
    taille = len(tableau)
    
    # moitie (int) : moitié de la taille du tableau
    moitie = taille // 2
    
    # partie_gauche (list(object)) : sous-tableau contenant les moitie premiers
    # éléments de tableau
    partie_gauche = []
    
    # partie_droite (list(object)) : sous-tableau contenant les moitie derniers
    # éléments du tableau
    partie_droite = []
    
    # Début du traitement
    # Si le tableau n'a qu'un élément, alors il est déjà trié
    if taille == 1:
        return tableau
    else:
        partie_gauche = tableau[:moitie]
        partie_droite = tableau[moitie:]
        what = fusion(tri_fusion(partie_gauche), tri_fusion(partie_droite))
        return what
        
def fusion(tableau_gauche, tableau_droit):
    '''fusion (list(object) * list(object) -> list(object)) : renvoie les deux
    listes triées passées en argument fusionnées'''
    # Début du traitement
    # Si un tableau est vide, alors on peut renvoyer l'autre directement
    if tableau_gauche == []:
        return tableau_droit
    if tableau_droit == []:
        return tableau_gauche
    # Si le premier élément du tableau_gauche est plus petit que le premier
    # élément de tableau_droit, on renvoit le premier élément de tableau_gauche
    # puis on rappelle cette fonction
    if tableau_gauche[0] < tableau_droit[0]:
        nouveau_tableau = [tableau_gauche[0]]
        new_fusion = fusion(tableau_gauche[1:], tableau_droit)
        nouveau_tableau.extend(new_fusion)
        return nouveau_tableau
    else:
        new_fusion = fusion(tableau_gauche, tableau_droit[1:])
        nouveau_tableau = [tableau_droit[0]]
        nouveau_tableau.extend(new_fusion)
        return nouveau_tableau
        
a = [2,1]
print(tri_fusion(a))
    