A = [[False,True,False,True],
        [True, False, True, False],
        [False, True, False, True],
        [True, False, True, False]]

# Initialisation
N = 4 # Nombre de pages
l = [[],[],[],[]] # Liste d'adjacence

# Début du traitement
# j : colonne en cours de traitement
for j in range(N):
    # i : ligne en cours de traitement
    for i in range(N):
        if A[i][j]:
            l[j].append(i)

print(l)

