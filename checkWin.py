def checkWin(plateau, objectif):
    maxCheck = "ko"
    pointer = 0
    #check si la partie est gagné en longueur
    for i in range(len(plateau[0])):
        compteur = 0
        while compteur < len(plateau[pointer]) and plateau[pointer][i] == plateau[pointer][compteur] and plateau[pointer][i] > 0:
            compteur +=1
            if compteur == objectif:
                maxCheck = f"ok {plateau[pointer][i]}"
                return maxCheck
        pointer += 1
    

    #check si la partie est gagné en hauteur
    pointer = 0
    for i in range(len(plateau[0])):
        compteur = 0
        while compteur < len(plateau[pointer]) and plateau[0][i] == plateau[i][pointer] and plateau[i][compteur] > 0:
            compteur +=1
            if compteur == objectif:
                maxCheck = f"ok {plateau[pointer][i]}"
                return maxCheck
        pointer += 1
    





plateauBin = [[1, 0, 1],
              [1, 0, 1],
              [1, 0, 1]]

print(checkWin(plateauBin, 3))