import tkinter


def set_tile(row, column):
    global current_player

    if game_over:
        return

    if board[row][column]["text"] != "":
        return

    board[row][column]["text"] = current_player

    if current_player == playerO:
        current_player = playerX
    else:
        current_player = playerO

    label["text"] = current_player + "'s turn"

    check_winner()


def check_winner():
    global turns, game_over
    turns += 1

    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
                and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"] +
                         " is the winner!", foreground=color_blue)
            for column in range(3):
                board[row][column].config(
                    foreground=color_blue, background=color_pink)
            game_over = True
            return

    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
                and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"] +
                         " is the winner!", foreground=color_blue)
            for row in range(3):
                board[row][column].config(
                    foreground=color_blue, background=color_pink)
            game_over = True
            return

    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
            and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"] +
                     " is the winner!", foreground=color_blue)
        for i in range(3):
            board[i][i].config(foreground=color_blue, background=color_pink)
        game_over = True
        return

    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
            and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"] +
                     " is the winner!", foreground=color_blue)
        board[0][2].config(foreground=color_blue, background=color_pink)
        board[1][1].config(foreground=color_blue, background=color_pink)
        board[2][0].config(foreground=color_blue, background=color_pink)
        game_over = True
        return

    if turns == 9:
        game_over = True
        label.config(text="It's a tie!", foreground=color_blue)


def new_game():
    global turns, game_over

    turns = 0
    game_over = False

    label.config(text=current_player + "'s turn", foreground="white")

    for row in range(3):
        for column in range(3):
            board[row][column].config(
                text="", foreground=color_brown, background=color_pink)


playerX = "X"
playerO = "O"
current_player = playerX
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

color_yellow = "#E0BB74"
color_brown = "#8F6B58"
color_pink = "#e4abcc"
color_gray = "#d2d2d2"
color_blue = "#4a7ba6"

turns = 0
game_over = False

window = tkinter.Tk()
window.title("TIc Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window, background=color_pink)
label = tkinter.Label(frame, text=current_player + "'s turn", font=("Consolas", 20), background=color_pink,
                      foreground="white")

label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"),
                                            background=color_pink, foreground=color_brown, width=4, height=1,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column)

button = tkinter.Button(frame, text="restart", font=("Consolas", 20), background=color_pink,
                        foreground="white", command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()
