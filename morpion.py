import tkinter as tk


board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
current_player = 1  # Joueur 1 commence

def place_symbol(row, column):
    global current_player, board

    if board[row][column] == 0:  
        board[row][column] = current_player
        buttons[row][column].config(text="X" if current_player == 1 else "O", state=tk.DISABLED)  

        if check_win():
            show_winner()
        elif check_draw():
            show_draw()
        else:
            current_player = 3 - current_player  # Changer de joueur


def check_win():
#  pour le ligne et la colonne
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return True
        if board[0][i] == board[1][i] == board[2][i] != 0:
            return True
        # pour les diagonales
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return True
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return True
    return False

def check_draw():
    for row in board:
        if 0 in row:
            return False
    return True

def show_winner():
    winner = "Joueur 1" if current_player == 2 else "Joueur 2"
    result_label.config(text=f"Le {winner} a gagné !")

def show_draw():
    result_label.config(text="Match nul !")


def disable_all_buttons():
    for row in buttons:
        for btn in row:
            btn.config(state=tk.DISABLED)

def draw_grid():
    global buttons
    buttons = []
    for row in range(3):
        row_buttons = []
        for col in range(3):
            button = tk.Button(root, text="", font=("Arial", 50), width=2, height=1,
                               command=lambda r=row, c=col: place_symbol(r, c))
            button.grid(row=row, column=col)
            row_buttons.append(button)
        buttons.append(row_buttons)


root = tk.Tk()
root.title("Morpion")
root.minsize(500, 500)

result_label = tk.Label(root, text="", font=("Arial", 20))
result_label.grid(row=3, column=0, columnspan=3)

draw_grid()
root.mainloop()
