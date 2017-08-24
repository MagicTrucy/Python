# Donnée : l la liste d'adjacence
l = [[1,3],[0,2],[1],[0]]

# Initialisation

# N : nombre de pages
N = 4
# A : tableau d'adjacence
A = [[False for x in range(N)] for y in range(N)]

# Début du traitement
# index_page : l'index en cours dans la liste
for index_page in range(len(l)):
    # index_lien : l'index en cours dans la liste à la position l[index_page]
    for index_lien in range(len(l[index_page])):
        # page_pointee (int) : page pointee par le lien numéro index_lien
        # de la page numéro index_page
        page_pointee = l[index_page][index_lien]
        A[page_pointee][index_page] = True

print(A)
