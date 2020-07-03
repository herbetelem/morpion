def checkPion(axeY, axeX, plateau):
    if axeX == 1:
        axeX = 2
    elif axeX == 2:
        axeX = 4
    elif axeX == 3:
        axeX = 6
    if axeY == "a":
        axeY = 1
    elif axeY == "b":
        axeY = 2
    elif axeY == "c":
        axeY = 3
    if plateau[axeY][axeX] == ".":
        return "ok"
    else: 
        return "ko"