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

    compteur = 0
    varprev = 0
    for i in range(len(plateau[0])):
        for o in range(len(plateau[0])):
            var = plateau[o][i]
            if var != 0:
                if varprev == 0 or var == varprev:
                    compteur += 1
                    varprev = var
            else:
                compteur = 0
            if compteur == objectif:
                return f"ok {plateau[o][i]}"
    


plateauBin = [[1, 1, 1],
              [2, 1, 2],
              [2, 1, 2]]

print(checkWin(plateauBin, 3))