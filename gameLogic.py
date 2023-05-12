from case import Case
from random import randrange

jeu_cache = []

def affiche_jeu_cache():
    for l in jeu_cache:
        print(*[str(c) for c in l])

def initialisation(longueur : int, hauteur : int, nombre_de_bombe : int, safeX : int, safeY : int) -> None:
    global jeu_cache
    
    jeu_cache = []
    
    for y in range(hauteur):
        jeu_cache.append([])
        for x in range(longueur):
            jeu_cache[-1].append(Case(x,y))
            
    for i in range(nombre_de_bombe):
        
        x = randrange(0,longueur)
        y = randrange(0,hauteur)
        
        while jeu_cache[y][x].isBombe or (-1 <= safeX - x <= 1  and -1 <= safeY - y <= 1):

            x = randrange(0,longueur)
            y = randrange(0,hauteur)

            
        jeu_cache[y][x].isBombe = True
        
        for x1 in [-1,0,1]:
            if x+x1 >= 0 and x+x1 < longueur:
            
                for y1 in [-1,0,1]:
                    if y+y1 >= 0 and y+y1 < hauteur:
                    
                        jeu_cache[y+y1][x+x1].nombre += 1
    
def interraction(x : int, y : int):
    
    global jeu_cache
    
    assert x >= 0 and x < len(jeu_cache[0]), "X position out of bounds"
    assert y >= 0 and y < len(jeu_cache), "Y position out of bounds"

    if jeu_cache[y][x].isBombe:
        return False
    
    listeCases = []
    listeCasesAExplorer = [(x,y)]
    
    while len(listeCasesAExplorer) > 0:
        posX, posY = listeCasesAExplorer.pop()
        
        
        listeCases.append(jeu_cache[posY][posX])
        
        if jeu_cache[posY][posX].nombre == 0:
            
            for posX2 in [posX-1,posX,posX+1]:
                for posY2 in [posY-1,posY,posY+1]:
                    
                    if  0 <= posX2 < len(jeu_cache[0]) and 0 <= posY2 < len(jeu_cache) \
                        and not (jeu_cache[posY2][posX2] in listeCases or (posX2,posY2) in listeCasesAExplorer):
                        
                        listeCasesAExplorer.append((posX2, posY2))
                    
    return listeCases
    
    
if __name__ == "__main__":
    initialisation(10,10,20, 5, 5)
    affiche_jeu_cache()
    l = interraction(5,5)
    
    for c in l:
        jeu_cache[c.y][c.x].hasDrapeau = True
    
    print("######")
    affiche_jeu_cache()