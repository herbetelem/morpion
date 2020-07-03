def printMap(plateau):
    for i in range(len(plateau)):
        ligne = ""
        for o in range(len(plateau[i])):
            ligne = ligne + plateau[i][o]
        print(ligne)