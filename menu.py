from GraphicalHandler import *
import tkinter
from tkinter import messagebox

def init():
    for widget in app.winfo_children():
        widget.destroy()
    initialisation(LARGEUR.get(), HAUTEUR.get(), NB_BOMBES.get(), app)
    app.bind("<Button-1>", left_click_handler)
    
def left_click_handler(event):
    
    if continuer():
        left_click(event)
        
    if not continuer():
        nouvelle_partie = messagebox.askokcancel(title="Recomencer ?", message="La partie est finie,\n voulez-vous recomencer ?")
        if nouvelle_partie:
            app.unbind("<Button-1>")
            for widget in app.winfo_children(): widget.destroy()
            menu()
        else:
            app.quit()
    


def choose_BB():
    NB_BOMBES_MAX.set((LARGEUR.get()*HAUTEUR.get())//3)
    for widget in app.winfo_children(): widget.destroy()
    
    app.geometry("475x500")
    
    titre = tkinter.Label(app,
                      text="Démineur",
                      font=("Courier New",70))
    titre.grid(row=0,column=1,padx=10,pady=10)  
        
    txt_bombes = tkinter.Label(app, text="Nombre de bombes",font=("Courier New",30))
    txt_bombes.grid(row=1,column=1,padx=10,pady=0)
    scale_bombes = tkinter.Scale(app, from_=1, to=NB_BOMBES_MAX.get(),
                                 variable=NB_BOMBES,
                                 orient=tkinter.HORIZONTAL)
    NB_BOMBES.set(NB_BOMBES_MAX.get()/4)
    scale_bombes.grid(row=2,column=1,padx=10,pady=0)

    back_button = tkinter.Button(app,
                             text="Back",
                             width=8, height=1,
                             font=("Courier New",30), background="#FFFF99",
                             activeforeground="#CC9900",activebackground="#FFFF99",
                                 command=menu)
    back_button.grid(row=3,column=1,padx=10,pady=25)
    
    play_button = tkinter.Button(app,
                             text="Play",
                             width=10, height=1,
                             font=("Courier New",40), background="#CCFFDD",
                             activeforeground="#00AA00",activebackground="#CCFFDD",
                                 command=init)
    play_button.grid(row=4,column=1,padx=10,pady=50)
    
def menu():
    
    app.geometry("475x450")
    
    for widget in app.winfo_children(): widget.destroy()
    
    titre = tkinter.Label(app,
                      text="Démineur",
                      font=("Courier New",70))
    titre.grid(row=0,column=1,padx=10,pady=10)            

    txt_largeur = tkinter.Label(app, text="Largeur",font=("Courier New",30))
    txt_largeur.grid(row=1,column=1,padx=10,pady=0)
    scale_largeur = tkinter.Scale(app, from_=4, to=LARGEUR_MAX,
                                 variable=LARGEUR,
                                 orient=tkinter.HORIZONTAL)
    scale_largeur.grid(row=2,column=1,padx=10,pady=0)
    
    txt_hauteur = tkinter.Label(app, text="Hauteur",font=("Courier New",30))
    txt_hauteur.grid(row=3,column=1,padx=10,pady=0)
    scale_hauteur = tkinter.Scale(app, from_=4, to=HAUTEUR_MAX,
                                 variable=HAUTEUR,
                                 orient=tkinter.HORIZONTAL)
    scale_hauteur.grid(row=4,column=1,padx=10,pady=0)

    next_button = tkinter.Button(app,
                             text="Next",
                             width=8, height=1,
                             font=("Courier New",30), background="#FFFF99",
                             activeforeground="#CC9900",activebackground="#FFFF99",
                                 command=choose_BB)
    next_button.grid(row=5,column=1,padx=10,pady=50)

app = tkinter.Tk()
app.title("## -- Démineur -- ##")

LARGEUR_MAX = 20
HAUTEUR_MAX = 20
LARGEUR = tkinter.IntVar()
LARGEUR.set(LARGEUR_MAX//2)
HAUTEUR = tkinter.IntVar()
HAUTEUR.set(HAUTEUR_MAX//2)
NB_BOMBES_MAX = tkinter.IntVar()
NB_BOMBES_MAX.set(int((LARGEUR_MAX*HAUTEUR_MAX)/3))
NB_BOMBES = tkinter.IntVar()
NB_BOMBES.set(NB_BOMBES_MAX.get()//2)

menu()

app.mainloop()