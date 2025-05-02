import tkinter as tk
import random

class SimpleTicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.current_player = random.choice(["X", "O"])
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.label = tk.Label(root, text=f"{self.current_player}'s Turn", font=("Arial", 24))
        self.label.pack(pady=10)

        self.frame = tk.Frame(root)
        self.frame.pack()

        for r in range(3):
            for c in range(3):
                btn = tk.Button(self.frame, text="", font=("Arial", 36), width=5, height=2,
                             command=lambda r=r, c=c: self.next_turn(r, c))
                btn.grid(row=r, column=c, padx=5, pady=5)
                self.buttons[r][c] = btn

        self.reset_btn = tk.Button(root, text="Restart Game", font=("Arial", 16), command=self.reset_board)
        self.reset_btn.pack(pady=10)

    def next_turn(self, r, c):
        if self.buttons[r][c]['text'] == "":
            self.buttons[r][c]['text'] = self.current_player

            if self.check_winner():
                self.label.config(text=f"{self.current_player} Wins!")
                self.disable_all()
            elif self.is_tie():
                self.label.config(text="It's a Tie!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.label.config(text=f"{self.current_player}'s Turn")

    def check_winner(self):
        b = self.buttons
        for i in range(3):
            if b[i][0]['text'] == b[i][1]['text'] == b[i][2]['text'] != "":
                return True
            if b[0][i]['text'] == b[1][i]['text'] == b[2][i]['text'] != "":
                return True

        if b[0][0]['text'] == b[1][1]['text'] == b[2][2]['text'] != "":
            return True
        if b[0][2]['text'] == b[1][1]['text'] == b[2][0]['text'] != "":
            return True

        return False

    def is_tie(self):
        return all(self.buttons[r][c]['text'] != "" for r in range(3) for c in range(3))

    def disable_all(self):
        for row in self.buttons:
            for btn in row:
                btn.config(state=tk.DISABLED)

    def reset_board(self):
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(text="", state=tk.NORMAL)
        self.current_player = random.choice(["X", "O"])
        self.label.config(text=f"{self.current_player}'s Turn")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleTicTacToe(root)
    root.mainloop()
