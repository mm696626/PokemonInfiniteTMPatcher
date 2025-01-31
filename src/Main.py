import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import hashlib
import os
import shutil

import gen3ROMModifier
import heartGoldSoulSilverROMModifier
import platinumROMModifier


EXPECTED_MD5 = {
    'FireRed': ['e26ee0d44e809351c8ce2d73c7400cdd'],
    'LeafGreen': ['612ca9473451fa42b51d1711031ed5f6'],
    'Emerald': ['605b89b67018abcea91e693a4dd25be3'],
    'Platinum': ['d66ad7a2a0068b5d46e0781ca4953ae9', 'ab828b0d13f09469a71460a34d0de51b'],
    'HeartGold': ['258cea3a62ac0d6eb04b5a0fd764d788'],
    'SoulSilver': ['8a6c8888bed9e1dce952f840351b73f2']
}

EXPECTED_SIZE = {
    'FireRed': 16777216,
    'LeafGreen': 16777216,
    'Emerald': 16777216,
    'Platinum': 134217728,
    'HeartGold': 134217728,
    'SoulSilver': 134217728
}


def calculate_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def check_rom_validity(file_path, game_name):
    file_size = os.path.getsize(file_path)
    expected_size = EXPECTED_SIZE.get(game_name)

    if file_size != expected_size:
        messagebox.showerror("Invalid ROM", f"Invalid file size for {game_name}. Expected size: {expected_size} bytes.")
        return False

    md5_hash = calculate_md5(file_path)
    expected_md5_list = EXPECTED_MD5.get(game_name)

    if game_name == 'FireRed' and md5_hash == '51901a6e40661b3914aa333c802e24e8':
        messagebox.showerror("Unsupported ROM", "The USA Rev 1 FireRed ROM is not supported.")
        return False

    if game_name == 'LeafGreen' and md5_hash == '9d33a02159e018d09073e700e1fd10fd':
        messagebox.showerror("Unsupported ROM", "The USA Rev 1 LeafGreen ROM is not supported.")
        return False

    if md5_hash not in expected_md5_list:
        messagebox.showerror("Invalid ROM", f"Invalid MD5 for {game_name}. Expected MD5: {expected_md5_list}.")
        return False

    return True

def copy_file(file_path, save_path):
    file_name = os.path.basename(file_path)
    shutil.copy2(file_path, save_path)
    print(f"Copy of {file_name} created at {save_path}.")

def open_file(game_name):
    if game_name in ['FireRed', 'LeafGreen', 'Emerald']:
        filetypes = [("GBA Files", "*.gba")]
    elif game_name in ['HeartGold', 'SoulSilver', 'Platinum']:
        filetypes = [("DS Files", "*.nds")]
    else:
        filetypes = [("All Files", "*.*")]

    file_path = filedialog.askopenfilename(
        title=f"Open {game_name} ROM File",
        filetypes=filetypes
    )

    if file_path:
        if not check_rom_validity(file_path, game_name):
            return

        save_path = filedialog.asksaveasfilename(
            title=f"Save Modified {game_name} ROM File",
            defaultextension=".gba" if game_name in ['FireRed', 'LeafGreen', 'Emerald'] else ".nds",
            filetypes=filetypes
        )

        copy_file(file_path, save_path)

        if game_name == 'FireRed':
            gen3ROMModifier.modify_byte_in_file(save_path, 0x124EA0, 0xA9, 0x90)
            gen3ROMModifier.modify_byte_in_file(save_path, 0x124F6C, 0xA9, 0x90)
            gen3ROMModifier.modify_byte_in_file(save_path, 0x125C74, 0xA9, 0x90)
        elif game_name == 'LeafGreen':
            gen3ROMModifier.modify_byte_in_file(save_path, 0x124E78, 0xA9, 0x90)
            gen3ROMModifier.modify_byte_in_file(save_path, 0x124F44, 0xA9, 0x90)
            gen3ROMModifier.modify_byte_in_file(save_path, 0x125C4C, 0xA9, 0x90)
        elif game_name == 'Emerald':
            gen3ROMModifier.modify_byte_in_file(save_path, 0x1B6EE0, 0xA9, 0x90)
        elif game_name == 'Platinum':
            platinumROMModifier.platinum_infinite_tms(save_path)
        elif game_name == 'HeartGold':
            heartGoldSoulSilverROMModifier.heartgold_soulsilver_infinite_tms(save_path)
        elif game_name == 'SoulSilver':
            heartGoldSoulSilverROMModifier.heartgold_soulsilver_infinite_tms(save_path)

        messagebox.showinfo("Done", f"Patching for {game_name} is complete!")
    else:
        pass

root = tk.Tk()
root.title("Pokemon Infinite TMs Patcher")

frame1 = tk.Frame(root)
frame1.pack(padx=10, pady=10)

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

root.mainloop()
