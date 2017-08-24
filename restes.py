def restes(dividendes, diviseur):
    '''restes (list(int) * int -> list(int)) : renvoie les restes de la division
    euclidienne de chaque dividende par le diviseur'''
    
    # Initialisation
    '''restes (list(int)) : restes des divisions euclidiennes'''
    restes = []
    
    # Début du traitement
    for dividende in dividendes:
        reste = dividende % diviseur
        restes.append(reste)
    return restes
    