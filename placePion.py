def placePion(axeY, axeX, tour, plateau):
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
    if tour %2 == 0:
        pion = "X"
    else:
        pion = "O"
    plateau[axeY][axeX] = pion
    return plateau

def placeBin(axeY, axeX, tour, plateau):
    axeX -= 1
    if axeY == "a":
        axeY = 0
    elif axeY == "b":
        axeY = 1
    elif axeY == "c":
        axeY = 2
    if tour%2 == 0:
        plateau[axeY][axeX] = 1
    else:
        plateau[axeY][axeX] = 2
    return plateau