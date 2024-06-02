import tkinter as tk
from random import choice

class ColorButtonGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Button Game")

        self.colors = ["Yellow", "Blue", "Green", "Red"]
        self.buttons = []
        self.correct_colors = [choice(self.colors) for _ in range(5)]

        self.create_widgets()

    def create_widgets(self):
        for i in range(5):
            button = tk.Button(self.root, text="", width=10, height=3, command=lambda i=i: self.change_color(i))
            button.grid(row=0, column=i, padx=10, pady=10)
            self.buttons.append(button)

        self.check_button = tk.Button(self.root, text="Check", width=10, height=3, command=self.check_colors)
        self.check_button.grid(row=1, column=2, pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.result_label.grid(row=2, columnspan=5, pady=10)

    def change_color(self, index):
        current_color = self.buttons[index].cget("bg")
        next_color = self.colors[(self.colors.index(current_color) + 1) % len(self.colors)] if current_color in self.colors else self.colors[0]
        self.buttons[index].configure(bg=next_color)

    def check_colors(self):
        correct_count = 0
        for button, correct_color in zip(self.buttons, self.correct_colors):
            if button.cget("bg") == correct_color:
                correct_count += 1
        self.result_label.config(text=f"Correct colors in correct places: {correct_count}")

if __name__ == "__main__":
    root = tk.Tk()
    game = ColorButtonGame(root)
    root.mainloop()
