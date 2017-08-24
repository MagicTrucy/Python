import sys

# Initialisation

# fichier (file) : pointeur vers le fichier passé en argument
fichier = open(sys.argv[1])

# commentaire (int) : nombre de lignes de commentaire
commentaire = 0

# total (int) : nombre de lignes total
total = 0

# ratio (float) : rapport entre le nombre de lignes de commentaire et le nombre
# de lignes total
ratio = 0

# ligne_sans_blanc (str) : ligne sans caractères blancs (espaces, …)
ligne_sans_blanc = ''

# taille_ligne (int) : taille d'une ligne
taille_ligne = 0

# Début du traitement
# Pour chaque ligne dans le fichier, incrémenter total, et incrémenter
# commentaire si la ligne commence par un #
# ligne (str) : ligne en train d'être parcourue
for ligne in fichier:
    # On retire les caractères blancs
    ligne_sans_blanc = ligne.lstrip()
    taille_ligne = len(ligne_sans_blanc)
    # Si la ligne est vide, on la passe
    if taille_ligne > 0:
        # Si le premier caractère est un #, on incrémente commentaire
        if ligne_sans_blanc[0] == '#':
            commentaire += 1
        # Dans tous les cas, on incrémente total
        total += 1

# On calcule le pourcentage de lignes de commentaires par rapport au nombre de
# ligne total
ratio = commentaire / total
ratio *= 100

# On affiche les résultats
print('Nombre de lignes de commentaire : {}'.format(commentaire))
print('Nombre de lignes total : {}'.format(total))
print('Pourcentage de lignes de commentaire : {0:.2f}%'.format(ratio))
    