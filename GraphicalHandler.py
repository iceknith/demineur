import tkinter as tk
from case import Case
import gameLogic as gl

jeu_montre=[]

image_drapeau = None
image_case_cachee = None
image_bombe = None
image_bombe_active = None
image_cases_decouvertes = []

firstClick = True
nombreBombe = 0
nombreCases = 0
nombreCasesMax = 0
settings = []

canvas = None
gRoot = None
mouseX = 0
mouseY = 0

gameContinue = True

def mouse_movement(event):
    global mouseX, mouseY, image_cases_decouvertes
    mouseX = event.x
    mouseY = event.y

def left_click(event):
    global canvas, gRoot, settings, firstClick, drapeauDispo, nombreCases, gameContinue, image_bombe, image_bombe_active

    if jeu_montre[mouseY//32][mouseX//32].estDecouverte: return
    
    print("ici")

    if jeu_montre[mouseY//32][mouseX//32].hasDrapeau:
        
        drapeauDispo += 1

        c = jeu_montre[mouseY//32][mouseX//32]

        canvas.delete(c.image)
        c.set_image(canvas.create_image((c.x*32+16, c.y*32+16), image = image_case_cachee))
        c.hasDrapeau = False
        return

    if firstClick:
        firstClick = False
        gl.initialisation(*settings, mouseX//32, mouseY//32)

    affichage = gl.interraction(mouseX//32, mouseY//32)
    
    if affichage:

        for case in affichage:
            
            c = jeu_montre[case.y][case.x]
            
            canvas.delete(c.image)
            c.set_image(canvas.create_image((c.x*32+16, c.y*32+16), image = image_cases_decouvertes[case.nombre]))   

            c.estDecouverte = True
            c.hasDrapeau = False    

        nombreCases += len(affichage)
        
    else:

        for line in gl.jeu_cache:
            for case in line:
                c=jeu_montre[case.y][case.x]
                canvas.delete(c.image)
                if case.isBombe:
                    c.set_image(canvas.create_image((c.x*32+16, c.y*32+16), image = image_bombe))
                else:
                    c.set_image(canvas.create_image((c.x*32+16, c.y*32+16), image = image_cases_decouvertes[case.nombre]))
        case = jeu_montre[mouseY//32][mouseX//32]
        case.set_image(canvas.create_image((case.x*32+16, case.y*32+16), image = image_bombe_active))
        
        gameContinue = False

def right_click(event):
    global mouseX, mouseY, jeu_montre, image_drapeau, drapeauDispo
    
    c = jeu_montre[mouseY//32][mouseX//32]

    if not c.estDecouverte and drapeauDispo > 0:

        drapeauDispo -= 1
        canvas.delete(c.image)
        c.set_image(canvas.create_image((c.x*32+16, c.y*32+16), image = image_drapeau))
        c.hasDrapeau = True

def continuer():
    return gameContinue and nombreCases < nombreCasesMax

def initialisation(longueur, hauteur, nombre_bombe, root):
    global jeu_montre, canvas, gRoot, image_case_decouverte, image_drapeau, image_case_cachee, image_bombe, image_bombe_active, \
        settings, firstClick, drapeauDispo, nombreCases, nombreCasesMax, gameContinue
    
    gRoot=root
    for i in range(0,9):
        image_cases_decouvertes.append(tk.PhotoImage(file=f'images/Decouverte_{i}.png').zoom(2,2))

    image_case_cachee = tk.PhotoImage(file='images/NonDecouverte.png').zoom(2,2)
    image_drapeau = tk.PhotoImage(file='images/Drapeau.png').zoom(2,2)
    image_bombe=tk.PhotoImage(file="images/Bombe.png").zoom(2,2)
    image_bombe_active=tk.PhotoImage(file="images/Bombe_active.png").zoom(2,2)
    
    firstClick = True
    gameContinue = True
    settings = [longueur, hauteur, nombre_bombe]
    drapeauDispo = nombre_bombe
    nombreCases = 0
    nombreCasesMax = longueur*hauteur - nombre_bombe
    
    root.geometry(f'{longueur*32}x{hauteur*32}')

    canvas = tk.Canvas(root, width=longueur*32, height=hauteur*32, bg='white')
    canvas.pack(anchor=tk.CENTER, expand=True)
    
    root.bind("<Motion>",mouse_movement)
    root.bind('<Button-3>', right_click)
    
    jeu_montre = []
    for y in range(hauteur):
        jeu_montre.append([])
        for x in range(longueur):
            
            jeu_montre[-1].append(Case(x, y, image = canvas.create_image((x*32+16, y*32+16), image = image_case_cachee)))
    
if __name__ == "__main__":
    root = tk.Tk()
    root.title('Canvas Demo')
    initialisation(20, 20, 5, root)
    root.mainloop()