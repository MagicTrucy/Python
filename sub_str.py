def sub_str(haystack, needle):
    '''sub_str (str * str -> bool) : renvoie True si la chaîne de caractères
    needle se trouve dans la chaîne de caractères haystack'''
    
    # Initialisation
    '''taille_haystack (int) : longueur de la chaîne de caractères haystack'''
    taille_haystack = len(haystack)
    
    '''taille_needle (int) : longueur de la chaîne de caractères needle'''
    taille_needle = len(needle)
    
    # Début du traitement
    for i in range(taille_haystack):
        for j in range(taille_needle):
            if haystack[i] != needle[j]:
                break
            if j == range(taille_needle):
                return True
    return False
    
print(sub_str('mdrlol', 'lol'))