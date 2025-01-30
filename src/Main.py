import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import os
import shutil
import gen3ROMModifier
import heartGoldSoulSilverROMModifier
import platinumROMModifier


def backup_file(file_path):
    backup_folder = "backups"
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    file_name = os.path.basename(file_path)
    backup_path = os.path.join(backup_folder, file_name)

    shutil.copy2(file_path, backup_path)
    print(f"Backup of {file_name} created at {backup_path}.")

    return backup_path

def open_file(tab_name):
    file_path = filedialog.askopenfilename(title="Open a file")
    if file_path:
        if tab_name == 'FireRed':
            backup_file(file_path)
            gen3ROMModifier.modify_byte_in_file(file_path, 0x124EA0, 0xA9, 0x90)
            gen3ROMModifier.modify_byte_in_file(file_path, 0x124F6C, 0xA9, 0x90)
            gen3ROMModifier.modify_byte_in_file(file_path, 0x125C74, 0xA9, 0x90)
        elif tab_name == 'LeafGreen':
            backup_file(file_path)
            gen3ROMModifier.modify_byte_in_file(file_path, 0x124E78, 0xA9, 0x90)
            gen3ROMModifier.modify_byte_in_file(file_path, 0x124F44, 0xA9, 0x90)
            gen3ROMModifier.modify_byte_in_file(file_path, 0x125C4C, 0xA9, 0x90)
        elif tab_name == 'Emerald':
            backup_file(file_path)
            gen3ROMModifier.modify_byte_in_file(file_path, 0x1B6EE0, 0xA9, 0x90)
        elif tab_name == 'Platinum':
            backup_file(file_path)
            platinumROMModifier.platinum_infinite_tms(file_path)
        elif tab_name == 'HeartGold/SoulSilver':
            backup_file(file_path)
            heartGoldSoulSilverROMModifier.heartgold_soulsilver_infinite_tms(file_path)
    else:
        messagebox.showinfo("No File", "No file selected")

root = tk.Tk()
root.title("Pokemon Infinite TMs Patcher")

notebook = ttk.Notebook(root)

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)
frame4 = ttk.Frame(notebook)
frame5 = ttk.Frame(notebook)

notebook.add(frame1, text='FireRed')
notebook.add(frame2, text='LeafGreen')
notebook.add(frame3, text='Emerald')
notebook.add(frame4, text='Platinum')
notebook.add(frame5, text='HeartGold/SoulSilver')

notebook.pack(fill="both", expand=True)

button1 = tk.Button(frame1, text="Open FireRed File", command=lambda: open_file('FireRed'))
button1.pack(pady=20)

button2 = tk.Button(frame2, text="Open LeafGreen File", command=lambda: open_file('LeafGreen'))
button2.pack(pady=20)

button3 = tk.Button(frame3, text="Open Emerald File", command=lambda: open_file('Emerald'))
button3.pack(pady=20)

button4 = tk.Button(frame4, text="Open Platinum File", command=lambda: open_file('Platinum'))
button4.pack(pady=20)

button5 = tk.Button(frame5, text="Open HeartGold/SoulSilver File", command=lambda: open_file('HeartGold/SoulSilver'))
button5.pack(pady=20)

root.mainloop()
