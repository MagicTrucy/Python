class Pile():
    # Implémente la structure de données de pile (LIFO (Last In First Out))
    # L'élément en index 0 est le plus bas de la pile
    
    def __init__(self):
        # donnees (list(object)) : contient les données de la pile
        self.donnees = []
        # taille (int) : nombre d'éléments dans la liste
        self.taille = 0
    
    def empiler(self, element):
        # empiler (object -> None) : rajoute element au sommet de la pile
        self.donnees.append(element)
        self.taille += 1
        
    def depiler(self):
        # depiler (None -> object) : retire l'élément au sommet de la pile et
        # le renvoie
        # element (object) : élément au sommet de la pile
        # on prend le taille-1-ième élément car le premier élément a pour index
        # 0
        element = self.donnees[self.taille - 1]
        del self.donnees[self.taille - 1]
        self.taille -= 1
        return element
        
    def est_vide(self):
        # est_vide (None -> bool) : renvoie True si la pile est vide,
        # False sinon
        # S'il n'y a aucun élément dans la pile, on renvoie True
        if self.taille == 0:
            return True
        else:
            return False
            
    def cardinal(self):
        # cardinal (None -> int) : renvoie le nombre d'éléments dans la pile
        return self.taille
        
    def vider(self):
        # vider (None -> list(object) : dépile tous les éléments de la liste
        # Si la pile est vide, ne rien faire
        depile = []
        while self.donnees != []:
            depile.append(self.depiler())
        self.taille = 0
        return depile
        
    def dupliquer(self):
        # dupliquer (None -> None) : duplique l'élément en tête
        # Si la pile est vide, indiquer l'erreur et ne rien faire
        if self.taille == 0:
            print('Impossible de dupliquer dans une pile vide')
            return None
        # tete (object) : élément en tête
        tete = self.donnees[self.taille - 1]
        self.donnees.append(tete)
        self.taille += 1
        
    def echanger(self):
        # echanger (None -> None) : échange les 2 éléments en tête
        # S'il y a moins de 2 éléments dans la pile, indiquer l'erreur et ne
        # rien faire
        if self.taille < 2:
            print('Impossible d\'échanger dans une pile contenant moins de 2 '
                'éléments')
            return None
        # index_tete (int) : index de l'élément en tête
        index_tete = self.taille - 1
        # index_avant_tete (int) : index de l'élément avant celui en tête
        index_avant_tete = self.taille - 2
        self.donnees[index_tete], self.donnees[index_avant_tete] = self.donnees[index_avant_tete], self.donnees[index_tete]
        
    def print(self):
        print(self.donnees)