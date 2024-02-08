from tkinter import *

def creer_plateau(canvas):
    global turn
    taille_carre = 100
    for ligne in range(6):
        for col in range(7):
            x1 = col * taille_carre
            y1 = ligne * taille_carre
            x2 = x1 + taille_carre
            y2 = y1 + taille_carre
            carre = canvas.create_rectangle(x1, y1, x2, y2, fill="white")
            canvas.tag_bind(carre, "<Button-1>", lambda event, carre=carre: (carre_clique_player1 if turn == 1 else carre_clique_player2)(carre) )

def carre_clique_player1(carre):
    canvas.itemconfig(carre, fill="blue")
    turn = 1

def carre_clique_player2(carre):
    canvas.itemconfig(carre, fill="red")
    turn = 0


def afficher_page_accueil():
    frame_plateau.pack_forget()
    frame_accueil.pack()

def afficher_plateau():
    frame_accueil.pack_forget()
    frame_plateau.pack()
    creer_plateau(canvas)

turn : int
racine = Tk()
racine.title("Puissance 4")
racine.configure(background="beige")
racine.geometry("1920x1080")
racine.attributes("-fullscreen", True)

quitter = Button(racine, text="X", command=racine.destroy, font=("Arial", 20), bg="red", fg="white")
quitter.pack(side=TOP, anchor=NE, padx=10, pady=10)

# Frame pour la page d'accueil
frame_accueil = Frame(racine, background="beige")
frame_accueil.pack(fill=BOTH, expand=True)

# Frame pour le plateau de jeu
frame_plateau = Frame(racine, background="beige")
canvas = Canvas(frame_plateau, width=600, height=700)
canvas.pack()

# Création des éléments de la page d'accueil

bienvenue = Label(frame_accueil, text="Bienvenue sur le Puissance 4. Choisissez entre les 2 modes de jeux :\n en ligne ou hors ligne", bg="beige", fg="black", font=("Arial", 30))
bienvenue.pack(side=TOP, fill=X, padx=10, pady=10)

jouer_en_ligne = Button(frame_accueil, text="Jouer en ligne", width=25, height=3, bg="white", fg="black", font=("Arial", 20), command=afficher_plateau)
jouer_en_ligne.pack(side=TOP, padx=10, pady=10)

jouer_hors_ligne = Button(frame_accueil, text="Jouer hors ligne", width=25, height=3, bg="white", fg="black", font=("Arial", 20), command=afficher_plateau)
jouer_hors_ligne.pack(side=TOP, padx=10, pady=10)

# Afficher initialement la page d'accueil
afficher_page_accueil()
racine.mainloop()
