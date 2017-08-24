class File():
    # Implémente la structure de données de file (FIFO (First In First Out))
    
    def __init__(self):
        # donnees (list(object)) : contient les données de la file
        self.donnees = []
        # taille (int) : nombre d'éléments dans la liste
        self.taille = 0
    
    def enfiler(self, element):
        # emfiler (object -> None) : rajoute element au bout de la file
        self.donnees.append(element)
        self.taille += 1
        
    def defiler(self):
        # defiler (None -> object) : retire le premier élément de la file et
        # le renvoie
        # element (object) : premier élément de la file
        element = self.donnees[0]
        del self.donnees[0]
        self.taille -= 1
        return element
        
    def est_vide(self):
        # est_vide (None -> bool) : renvoie True si la file est vide,
        # False sinon
        # S'il n'y a aucun élément dans la file, on renvoie True
        if self.taille == 0:
            return True
        else:
            return False
            
    def cardinal(self):
        # cardinal (None -> int) : renvoie le nombre d'éléments dans la file
        return self.taille
        
    def vider(self):
        # vider (None -> None) : supprime tous les éléments de la liste
        # Si la file est vide, ne rien faire
        if self.taille == 0:
            return None
        for index in range(self.taille - 1, -1 ,-1):
            del self.donnees[index]
        self.taille = 0
        
    def dupliquer(self):
        # dupliquer (None -> None) : duplique l'élément en tête
        # Si la file est vide, indiquer l'erreur et ne rien faire
        if self.taille == 0:
            print('Impossible de dupliquer dans une pile vide')
            return None
        # tete (object) : élément en tête
        tete = self.donnees[0]
        self.donnees.insert(1, tete)
        self.taille += 1
        
    def echanger(self):
        # echanger (None -> None) : échange les 2 éléments en tête
        # S'il y a moins de 2 éléments dans la file, indiquer l'erreur et ne
        # rien faire
        if self.taille < 2:
            print('Impossible d\'échanger dans une file contenant moins de 2 '
                'éléments')
            return None
        self.donnees[0], self.donnees[1] = self.donnees[1], self.donnees[0]
        
    def print(self):
        print(self.donnees)