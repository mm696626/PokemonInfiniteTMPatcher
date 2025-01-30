import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import os
import shutil
import gen3ROMModifier
import heartGoldSoulSilverROMModifier
import platinumROMModifier
from PIL import Image, ImageTk

# Backup function remains the same
def backup_file(file_path):
    backup_folder = "backups"
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    file_name = os.path.basename(file_path)
    backup_path = os.path.join(backup_folder, file_name)

    shutil.copy2(file_path, backup_path)
    print(f"Backup of {file_name} created at {backup_path}.")

    return backup_path

def open_file(game_name):
    file_path = filedialog.askopenfilename(title=f"Open {game_name} ROM File")
    if file_path:
        if game_name == 'FireRed':
            backup_file(file_path)
            gen3ROMModifier.modify_byte_in_file(file_path, 0x124EA0, 0xA9, 0x90)
            gen3ROMModifier.modify_byte_in_file(file_path, 0x124F6C, 0xA9, 0x90)
            gen3ROMModifier.modify_byte_in_file(file_path, 0x125C74, 0xA9, 0x90)
        elif game_name == 'LeafGreen':
            backup_file(file_path)
            gen3ROMModifier.modify_byte_in_file(file_path, 0x124E78, 0xA9, 0x90)
            gen3ROMModifier.modify_byte_in_file(file_path, 0x124F44, 0xA9, 0x90)
            gen3ROMModifier.modify_byte_in_file(file_path, 0x125C4C, 0xA9, 0x90)
        elif game_name == 'Emerald':
            backup_file(file_path)
            gen3ROMModifier.modify_byte_in_file(file_path, 0x1B6EE0, 0xA9, 0x90)
        elif game_name == 'Platinum':
            backup_file(file_path)
            platinumROMModifier.platinum_infinite_tms(file_path)
        elif game_name == 'HeartGold':
            backup_file(file_path)
            heartGoldSoulSilverROMModifier.heartgold_soulsilver_infinite_tms(file_path)
        elif game_name == 'SoulSilver':
            backup_file(file_path)
            heartGoldSoulSilverROMModifier.heartgold_soulsilver_infinite_tms(file_path)
    else:
        messagebox.showinfo("No File", "No file selected")

root = tk.Tk()
root.title("Pokemon Infinite TMs Patcher")

notebook = ttk.Notebook(root)

frame1 = ttk.Frame(notebook)
notebook.add(frame1, text='Games')

notebook.pack(fill="both", expand=True)

def load_image(image_path, size=(200, 200)):
    try:
        img = Image.open(image_path)
        img = img.resize(size)
        img_tk = ImageTk.PhotoImage(img)
        return img_tk
    except Exception as e:
        print(f"Error loading image {image_path}: {e}")
        return None

fire_red_img = load_image("images/firered.png")
leaf_green_img = load_image("images/leafgreen.png")
emerald_img = load_image("images/emerald.png")
platinum_img = load_image("images/platinum.png")
heart_gold_img = load_image("images/heartgold.png")
soul_silver_img = load_image("images/soulsilver.png")

button1 = tk.Button(frame1, image=fire_red_img, command=lambda: open_file('FireRed'))
button1.grid(row=0, column=0, padx=10, pady=10)

button2 = tk.Button(frame1, image=leaf_green_img, command=lambda: open_file('LeafGreen'))
button2.grid(row=0, column=1, padx=10, pady=10)

button3 = tk.Button(frame1, image=emerald_img, command=lambda: open_file('Emerald'))
button3.grid(row=1, column=0, padx=10, pady=10)

button4 = tk.Button(frame1, image=platinum_img, command=lambda: open_file('Platinum'))
button4.grid(row=1, column=1, padx=10, pady=10)

button5 = tk.Button(frame1, image=heart_gold_img, command=lambda: open_file('HeartGold'))
button5.grid(row=2, column=0, padx=10, pady=10)

button6 = tk.Button(frame1, image=soul_silver_img, command=lambda: open_file('SoulSilver'))
button6.grid(row=2, column=1, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
