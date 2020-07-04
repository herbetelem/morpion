def checkWin(plateau, objectif):
    maxCheck = 0
    pointer = 0
    #check si la partie est gagné en longueur
    for i in range(len(plateau[0])):
        compteur = 0
        while compteur < len(plateau[pointer]) and plateau[pointer][i] == plateau[pointer][compteur] and plateau[pointer][i] > 0:
            compteur +=1
            if compteur == objectif:
                return plateau[pointer][i]
        pointer += 1

#check si la partie est gagné en hauteur
    
    for i in range(len(plateau[0])):
        compteur = 0
        varprev = 0
        for o in range(len(plateau[0])):
            var = plateau[o][i]
            if var != 0:
                if varprev == 0 or var == varprev:
                    compteur += 1
                    varprev = var
            else:
                compteur = 0
            if compteur == objectif:
                return plateau[o][i]


#check si la partie est gagné en diagonale \
    firstIndex = 0
    compteur = 0
    if plateau[firstIndex][firstIndex] > 0:
        while plateau[firstIndex][firstIndex] == plateau[(firstIndex + compteur)][(firstIndex + compteur)]:
            compteur += 1
            if compteur == objectif:
                return plateau[firstIndex][firstIndex]


#check si la partie est gagné en diagonale /
    lastIndex = 2
    lastIndexY = 0
    compteur = 0
    if plateau[lastIndex][compteur] > 0:
        while plateau[lastIndex][lastIndexY] == plateau[(lastIndex - compteur)][compteur]:
            compteur += 1
            if compteur == objectif:
                return plateau[lastIndex][lastIndexY]
    return maxCheck
