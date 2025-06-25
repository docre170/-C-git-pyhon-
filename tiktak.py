import tkinter

def place_symbol(row,column):
    print("click")

def draw_grid():
    # pour creer des lignes on utilise fonctions
    for column in range(3):
        for row in range(3):
            button = tkinter.Button(
                     root,text="x", font=("Arial",50),
                width=5,height=3,
                command=lambda r=row: place_symbol(row, column)
                )
            button.grid(row=row, column=column)

# stockages
buttons = [
    [0, 0, 0],
    [0, 0, 0 ],
    [0, 0, 0 ]
]



# creer la fenetre du jet
root = tkinter.Tk()

# personalisation de la fenetre
root.title("tiktak")
root.minsize(500,500)
draw_grid()
root.mainloop()