import tkinter as tk
from tkinter import messagebox, ttk
import random
import time

# Translation dictionary
translations = {
    "en": {
        "incomplete": "Please fill all cells!",
        "congratulations": "Congratulations! You solved it correctly.",
        "check_solution": "Check Solution",
        "new_game": "New Game",
        "language": "Language"
    },
    "ru": {
        "incomplete": "Пожалуйста, заполните все ячейки!",
        "congratulations": "Поздравляем! Вы правильно решили задачу.",
        "check_solution": "Проверить решение",
        "new_game": "Новая игра",
        "language": "Язык"
    },
    "vi": {
        "incomplete": "Vui lòng điền vào tất cả các ô!",
        "congratulations": "Chúc mừng! Bạn đã giải đúng.",
        "check_solution": "Kiểm tra giải pháp",
        "new_game": "Trò chơi mới",
        "language": "Ngôn ngữ"
    }
}

current_language = "en"

def translate(key):
    return translations[current_language].get(key, key)

def generate_puzzle():
    board = [[0] * 9 for _ in range(9)]
    for _ in range(20):
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        if board[row][col] == 0 and is_valid(board, row, col, num):
            board[row][col] = num
    return board

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def validate_board():
    for row in range(9):
        for col in range(9):
            num = entries[row][col].get()
            if num == "":
                messagebox.showinfo(translate("incomplete"), translate("incomplete"))
                return
            num = int(num)
            if not is_valid(grid, row, col, num):
                highlight_invalid_cells()
                return
    messagebox.showinfo(translate("congratulations"), translate("congratulations"))

def highlight_invalid_cells():
    invalid_cells = []
    for row in range(9):
        for col in range(9):
            num = entries[row][col].get()
            if num != "" and int(num) != grid[row][col] and not is_valid(grid, row, col, int(num)):
                invalid_cells.append(entries[row][col])
    for _ in range(3):
        for cell in invalid_cells:
            cell.config(bg="red")
        root.update()
        time.sleep(0.3)
        for cell in invalid_cells:
            cell.config(bg="white")
        root.update()
        time.sleep(0.3)

def load_puzzle():
    for row in range(9):
        for col in range(9):
            entry = entries[row][col]
            entry.config(state="normal") 
            entry.delete(0, tk.END)  
            entry.config(bg="white") 

            num = grid[row][col]
            if num != 0:  
                entry.insert(0, str(num))  
                entry.config(state="disabled", bg="#E0E0E0") 
            else:
                entry.config(state="normal", bg="white")

def new_game():
    global grid
    grid = generate_puzzle()
    load_puzzle()

def change_language(event):
    global current_language
    current_language = language_var.get()
    update_ui()

def update_ui():
    validate_button.config(text=translate("check_solution"))
    new_game_button.config(text=translate("new_game"))
    language_label.config(text=translate("language"))

root = tk.Tk()
root.title("Sudoku Game")

# Language selection
language_label = tk.Label(root, text=translate("language"))
language_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

language_var = tk.StringVar(value=current_language)
language_menu = ttk.Combobox(root, textvariable=language_var, values=list(translations.keys()))
language_menu.grid(row=0, column=1, padx=5, pady=5, sticky="w")
language_menu.bind("<<ComboboxSelected>>", change_language)

# Sudoku grid
entries = [[None for _ in range(9)] for _ in range(9)]
frame = tk.Frame(root)
frame.grid(row=1, column=0, columnspan=10, padx=10, pady=10)
for row in range(9):
    for col in range(9):
        e = tk.Entry(frame, width=2, font=('Arial', 18), justify='center')
        e.grid(row=row, column=col, padx=5, pady=5)
        entries[row][col] = e

grid = generate_puzzle()
load_puzzle()

# Buttons
validate_button = tk.Button(root, text=translate("check_solution"), command=validate_board)
validate_button.grid(row=2, column=0, columnspan=2, sticky="we", padx=5, pady=5)

new_game_button = tk.Button(root, text=translate("new_game"), command=new_game)
new_game_button.grid(row=2, column=2, columnspan=8, sticky="we", padx=5, pady=5)

root.mainloop()