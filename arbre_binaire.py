class Noeud:
    '''Noeud d'un arbre binaire'''
    
    def __init__(self, valeur=None):
        '''Créé un nœud avec une valeur (None par défaut)'''
        # valeur (object) : valeur a stocker dans le nœud. On présume que valeur
        # implémente une méthode pour être comparée à elle-même
        self.valeur = valeur
        
        # gauche (noeud) : référence vers le noeud-fils à gauche
        self.gauche = None
        
        # droite (noeud) : référence vers le noeud-fils à droite
        self.droite = None
        
        # parent (noeud) : référence vers le noeud-parent
        self.parent = None
        
    def assigner_droite(self, noeud):
        '''Assigne un fils droit au noeud'''
        self.droite = noeud
        noeud.parent = self
        
    def assigner_gauche(self, noeud):
        '''Assigne un fils gauche au noeud'''
        self.gauche = noeud
        noeud.parent = self
        
    def parcours_prefixe(self):
        '''Affiche le parcours préfixe à partir de cette instance de noeud'''
        print(self.valeur)
        if self.gauche != None:
            self.gauche.parcours_prefixe()
        if self.droite != None:
            self.droite.parcours_prefixe()
            
    def parcours_infixe(self):
        '''Affiche le parcours infixe à partir de cette instance de noeud'''
        if self.gauche != None:
            self.gauche.parcours_infixe()
        print(self.valeur)
        if self.droite != None:
            self.droite.parcours_infixe()
            
    def parcours_suffixe(self):
        '''Affiche le parcours suffixe à partir de cette instance de noeud'''
        if self.gauche != None:
            self.gauche.parcours_suffixe()
        if self.droite != None:
            self.droite.parcours_suffixe()
        print(self.valeur)
        
    def parcours_profondeur(self):
        '''Affiche le parcours en profondeur à partir de cette instance de noeud'''
        # Initialisation
        # a_visiter (list(noeud)) : contient la pile des noeuds à visiter
        a_visiter = []
        
        # noeud_en_cours (noeud) : noeud_en_cours d'exploration
        noeud_en_cours = None
        
        # On ajoute la racine (cette instance) au sommet de la pile 
        a_visiter.append(self)
        
        # Début du traitement
        # Tant qu'on a au moins un noeud à explorer, on l'explore
        while a_visiter != []:
            noeud_en_cours = a_visiter.pop()
            print(noeud_en_cours.valeur)
            # On ajoute les fils de noeud_en_cours à la pile
            if noeud_en_cours.gauche != None:
                a_visiter.append(noeud_en_cours.gauche)
            if noeud_en_cours.droite != None:
                a_visiter.append(noeud_en_cours.droite)
                
    def parcours_largeur(self):
        '''Affiche le parcours en profondeur à partir de cette instance de noeud'''
        # Initialisation
        # a_visiter (list(noeud)) : contient la file des noeuds à visiter
        a_visiter = []
        
        # noeud_en_cours (noeud) : noeud_en_cours d'exploration
        noeud_en_cours = None
        
        # On ajoute la racine (cette instance) au bout de la pile 
        a_visiter.append(self)
        
        # Début du traitement
        # Tant qu'on a au moins un noeud à explorer, on l'explore
        while a_visiter != []:
            noeud_en_cours = a_visiter.pop(0)
            print(noeud_en_cours.valeur)
            # On ajoute les fils de noeud_en_cours à la pile
            if noeud_en_cours.gauche != None:
                a_visiter.append(noeud_en_cours.gauche)
            if noeud_en_cours.droite != None:
                a_visiter.append(noeud_en_cours.droite)
                
    def rotation_droite(self):
        '''Tourne l'arbre à droite depuis ce noeud'''
        # Initialisation
        # pivot (noeud) : nouvelle racine
        pivot = self.gauche
        self.gauche = pivot.droite
        pivot.droite = self
        self = pivot
        
    def rotation_gauche(self):
        '''Tourne l'arbre à gauche depuis ce noeud'''
        # Initialisation
        # pivot (noeud) : nouvelle racine
        pivot = self.droite
        self.droite = pivot.gauche
        pivot.gauche = self
        self = pivot