import tkinter as tk
from tkinter import filedialog


def open_file():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as file:
        text.insert('1.0', file.read())


def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension='.txt')
    with open(file_path, 'w') as file:
        file.write(text.get('1.0', 'end'))


root = tk.Tk()
root.title("Text Editor")

text = tk.Text(root, wrap='word')
text.pack(fill='both', expand=True)

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)

root.mainloop()
