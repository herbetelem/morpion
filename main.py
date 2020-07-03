import variables
import printPlat as pPlat
import debutJeu as dJeu
import checkPion
import placePion
import os
clear = lambda: os.system('cls')





def main():
    init = dJeu.debutJeu()
    variables.joueurA = init[0]
    variables.joueurB = init[1]
    
    while variables.statutParti == "ok":
        if variables.tour > 0:
            clear()

        print(variables.plateauBin)
        pPlat.printMap(variables.plateau)
        
        if variables.tour %2 == 0:
            print(f"{variables.joueurA} c'est a ton tour")
        else:
            print(f"{variables.joueurB} c'est a ton tour")
        axeY = str(input("veuillez choisir la ligne ou mettre votre pion (entre a et c) : "))
        while axeY != "a" and axeY != "b" and axeY != "c":
            axeY = str(input("entre a et c : "))
        axeX = int(input("veuillez choisir la colonne ou mettre votre pion (entre 1 et 3) : "))
        while axeX > 3 or axeX < 1:
            axeX = int(input("entre 1 et 3 : "))
        while checkPion.checkPion(axeY, axeX, variables.plateau) == "ko":
            print("cette case est deja prise")
            axeY = str(input("veuillez choisir la ligne ou mettre votre pion (entre a et c) : "))
            while axeY != "a" and axeY != "b" and axeY != "c":
                axeY = str(input("entre a et c : "))
            axeX = int(input("veuillez choisir la colonne ou mettre votre pion (entre 1 et 3) : "))
            while axeX > 3 or axeX < 1:
                axeX = int(input("entre 1 et 3 : "))
        variables.plateau = placePion.placePion(axeY, axeX, variables.tour, variables.plateau)
        variables.plateauBin = placePion.placeBin(axeY, axeX, variables.tour, variables.plateauBin)
        
        variables.tour += 1




if __name__ == "__main__":
    main()