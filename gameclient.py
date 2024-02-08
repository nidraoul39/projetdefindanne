#impore de bibliothèque

from tkinter import *

#création de fonction

def create_board(canvas):

    square_size = 100
    for row in range(4):
        for col in range(4):
            x1 = col * square_size
            y1 = row * square_size
            x2 = x1 + square_size
            y2 = y1 + square_size
            square = canvas.create_rectangle(x1, y1, x2, y2, fill="white")
            canvas.tag_bind(square, "<Button-1>", lambda event, square=square: square_clicked(square))

def square_clicked(square):
    canvas.itemconfig(square, fill="gray")

root = Tk()
root.title("Tic Tac Toe")

canvas = Canvas(root, width=300, height=300)
canvas.pack()


root.mainloop()


#création de la fenêtre

root = Tk()
root.title("Game")
root.configure(background="beige")
root.geometry("1920x1080")
root.attributes("-fullscreen", True)

# Modification du bouton "Quitter" pour qu'il soit une croix en haut à droite
quitte = Button(root, text="X", command=root.destroy, font=("Arial", 20), bg="red", fg="white")
quitte.pack(side=TOP, anchor=NE, padx=10, pady=10)

# Modification de la position du texte
hello = Label(root, text="Bienvenue sur le puissance 4 choisissez entre les 2 modes de jeux \n en ligne ou hors ligne", bg="beige", fg="black", font=("Arial", 30))
hello.pack(side=TOP, fill=X, padx=10, pady=10)

startonline = Button(root, text="Jouer en ligne", width=25, height=3, bg="white", fg="black", font=("Arial", 20))
startonline.pack(side=TOP, padx=10, pady=10)

startoffline = Button(root, text="Jouer hors ligne",  width=25, height=3, bg="white", fg="black", font=("Arial", 20))
startoffline.pack(side=TOP, padx=10, pady=10)

#écriture de la fenêtre

root.mainloop()