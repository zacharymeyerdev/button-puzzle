import tkinter as tk
from random import choice

class ColorButtonGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Button Game")

        self.max_buttons = 25
        self.max_colors = 25

        self.color_palette = ["Yellow", "Blue", "Green", "Red", "Cyan", "Magenta", "Orange", "Purple", "Pink", "Brown",
                              "Black", "White", "Gray", "Violet", "Indigo", "Chartreuse", "Teal", "Maroon", "Navy", 
                              "Olive", "Lime", "Coral", "Gold", "Silver", "Beige"]

        self.setup_initial_widgets()

    def setup_initial_widgets(self):
        self.label_buttons = tk.Label(self.root, text="Number of buttons (1-25):")
        self.label_buttons.grid(row=0, column=0, padx=10, pady=10)
        self.entry_buttons = tk.Entry(self.root)
        self.entry_buttons.grid(row=0, column=1, padx=10, pady=10)

        self.label_colors = tk.Label(self.root, text="Number of colors (1-25):")
        self.label_colors.grid(row=1, column=0, padx=10, pady=10)
        self.entry_colors = tk.Entry(self.root)
        self.entry_colors.grid(row=1, column=1, padx=10, pady=10)

        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.start_button.grid(row=2, columnspan=2, pady=10)

    def start_game(self):
        try:
            self.num_buttons = min(max(int(self.entry_buttons.get()), 1), self.max_buttons)
            self.num_colors = min(max(int(self.entry_colors.get()), 1), self.max_colors)
        except ValueError:
            self.num_buttons = 5
            self.num_colors = 4

        self.colors = self.color_palette[:self.num_colors]
        self.correct_colors = [choice(self.colors) for _ in range(self.num_buttons)]

        self.clear_initial_widgets()
        self.create_widgets()

    def clear_initial_widgets(self):
        self.label_buttons.destroy()
        self.entry_buttons.destroy()
        self.label_colors.destroy()
        self.entry_colors.destroy()
        self.start_button.destroy()

    def create_widgets(self):
        self.buttons = []
        for i in range(self.num_buttons):
            button = tk.Button(self.root, text="", width=10, height=3, bg=self.colors[0], command=lambda i=i: self.change_color(i))
            button.grid(row=i//5, column=i%5, padx=10, pady=10)  # Adjust layout to handle up to 25 buttons
            self.buttons.append(button)

        self.check_button = tk.Button(self.root, text="Check", width=10, height=3, command=self.check_colors)
        self.check_button.grid(row=(self.num_buttons // 5) + 1, column=2, pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.result_label.grid(row=(self.num_buttons // 5) + 2, columnspan=5, pady=10)

    def change_color(self, index):
        current_color = self.buttons[index].cget("bg")
        next_color = self.colors[(self.colors.index(current_color) + 1) % len(self.colors)] if current_color in self.colors else self.colors[0]
        self.buttons[index].configure(bg=next_color)

    def check_colors(self):
        correct_count = 0
        guessed_colors = []
        for button, correct_color in zip(self.buttons, self.correct_colors):
            guessed_color = button.cget("bg")
            guessed_colors.append(guessed_color)
            if guessed_color == correct_color:
                correct_count += 1
        print(f"Guessed colors in order: {guessed_colors}. Number of correct guesses: {correct_count}")
        self.result_label.config(text=f"Correct colors in correct places: {correct_count}")

if __name__ == "__main__":
    root = tk.Tk()
    game = ColorButtonGame(root)
    root.mainloop()
