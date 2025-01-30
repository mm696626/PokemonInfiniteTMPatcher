import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

def open_file(tab_name):
    file_path = filedialog.askopenfilename(title="Open a file")
    if file_path:
        if tab_name == 'FireRed/LeafGreen':
            print("Hello")
        elif tab_name == 'Platinum':
            print("Hi")
        elif tab_name == 'HeartGold/SoulSilver':
            print("Bye")
    else:
        messagebox.showinfo("No File", "No file selected")

root = tk.Tk()
root.title("Pokemon Infinite TMs Patcher")

notebook = ttk.Notebook(root)

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)

notebook.add(frame1, text='FireRed/LeafGreen')
notebook.add(frame2, text='Platinum')
notebook.add(frame3, text='HeartGold/SoulSilver')

notebook.pack(fill="both", expand=True)

button1 = tk.Button(frame1, text="Open FireRed/LeafGreen File", command=lambda: open_file('FireRed/LeafGreen'))
button1.pack(pady=20)

button2 = tk.Button(frame2, text="Open Platinum File", command=lambda: open_file('Platinum'))
button2.pack(pady=20)

button3 = tk.Button(frame3, text="Open HeartGold/SoulSilver File", command=lambda: open_file('HeartGold/SoulSilver'))
button3.pack(pady=20)

root.mainloop()
