import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk
import hashlib
import os
import shutil

import romByteModifier
import heartGoldSoulSilverROMModifier
import platinumROMModifier
import gamecubeISOModifier


EXPECTED_MD5 = {
    'FireRed': ['e26ee0d44e809351c8ce2d73c7400cdd', '51901a6e40661b3914aa333c802e24e8'],
    'LeafGreen': ['612ca9473451fa42b51d1711031ed5f6', '9d33a02159e018d09073e700e1fd10fd'],
    'Emerald': ['605b89b67018abcea91e693a4dd25be3'],
    'Platinum': ['d66ad7a2a0068b5d46e0781ca4953ae9', 'ab828b0d13f09469a71460a34d0de51b'],
    'HeartGold': ['258cea3a62ac0d6eb04b5a0fd764d788'],
    'SoulSilver': ['8a6c8888bed9e1dce952f840351b73f2'],
    'Colosseum': ['e3f389dc5662b9f941769e370195ec90'],
    'XD': ['3bc1671806cf763a8712a5d398f62ad3']
}

EXPECTED_SIZE = {
    'FireRed': 16777216,
    'LeafGreen': 16777216,
    'Emerald': 16777216,
    'Platinum': 134217728,
    'HeartGold': 134217728,
    'SoulSilver': 134217728,
    'Colosseum': 1459978240,
    'XD': 1459978240
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

    if md5_hash not in expected_md5_list:
        messagebox.showerror("Invalid ROM", f"Invalid MD5 for {game_name}. Expected MD5: {expected_md5_list}.")
        return False

    return True

def copy_file(file_path, save_path):
    shutil.copy2(file_path, save_path)

def open_file(game_name):
    if game_name in ['FireRed', 'LeafGreen', 'Emerald']:
        filetypes = [("GBA Files", "*.gba")]
    elif game_name in ['HeartGold', 'SoulSilver', 'Platinum']:
        filetypes = [("DS Files", "*.nds")]
    elif game_name in ['Colosseum', 'XD']:
        filetypes = [("GameCube ISO Files", "*.iso")]
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
            defaultextension=".iso" if game_name in ['Colosseum', 'XD'] else ".gba" if game_name in ['FireRed', 'LeafGreen', 'Emerald'] else ".nds",
            filetypes=filetypes
        )

        if not save_path:
            return

        copy_file(file_path, save_path)
        md5_hash = calculate_md5(file_path)

        if game_name == 'FireRed' and md5_hash == '51901a6e40661b3914aa333c802e24e8':
            romByteModifier.apply_ips_patch(file_path, save_path, "patches/firered_downgrade.ips")
            patched_md5_hash = calculate_md5(save_path)
            if not patched_md5_hash == 'e26ee0d44e809351c8ce2d73c7400cdd':
                messagebox.showinfo("ROM Downgrade Failed", ":(")
                return

        if game_name == 'LeafGreen' and md5_hash == '9d33a02159e018d09073e700e1fd10fd':
            romByteModifier.apply_ips_patch(file_path, save_path, "patches/leafgreen_downgrade.ips")
            patched_md5_hash = calculate_md5(save_path)
            if not patched_md5_hash == '612ca9473451fa42b51d1711031ed5f6':
                messagebox.showinfo("ROM Downgrade Failed", ":(")
                return

        if game_name == 'Colosseum' or game_name == 'XD':
            dolString = "start.dol"
            gamecubeISOModifier.read_gamecube(file_path, dolString.encode("ascii"), "clean.dol")
            copy_file("clean.dol", "modified.dol")

        show_patch_options(game_name, save_path)
    else:
        pass


def show_patch_options(game_name, save_path):
    def apply_patches():
        if game_name == 'FireRed':
            if infinite_tms.get():
                romByteModifier.modify_byte_in_file(save_path, 0x124EA0, 0xA9, 0x90)
                romByteModifier.modify_byte_in_file(save_path, 0x124F6C, 0xA9, 0x90)
                romByteModifier.modify_byte_in_file(save_path, 0x125C74, 0xA9, 0x90)
            if running_shoes.get():
                romByteModifier.modify_byte_in_file(save_path, 0x0BD494, 0x08, 0x00)
            if national_dex_evos.get():
                romByteModifier.modify_byte_in_file(save_path, 0x0CE91A, 0x97, 0x00)
                romByteModifier.modify_byte_in_file(save_path, 0x0CE91B, 0x28, 0x00)
                romByteModifier.modify_byte_in_file(save_path, 0x0CE91C, 0x14, 0x14)
                romByteModifier.modify_byte_in_file(save_path, 0x0CE91D, 0xDD, 0xE0)

        elif game_name == 'LeafGreen':
            if infinite_tms.get():
                romByteModifier.modify_byte_in_file(save_path, 0x124E78, 0xA9, 0x90)
                romByteModifier.modify_byte_in_file(save_path, 0x124F44, 0xA9, 0x90)
                romByteModifier.modify_byte_in_file(save_path, 0x125C4C, 0xA9, 0x90)
            if running_shoes.get():
                romByteModifier.modify_byte_in_file(save_path, 0x0BD468, 0x08, 0x00)
            if national_dex_evos.get():
                romByteModifier.modify_byte_in_file(save_path, 0x0CE8EE, 0x97, 0x00)
                romByteModifier.modify_byte_in_file(save_path, 0x0CE8EF, 0x28, 0x00)
                romByteModifier.modify_byte_in_file(save_path, 0x0CE8F0, 0x14, 0x14)
                romByteModifier.modify_byte_in_file(save_path, 0x0CE8F1, 0xDD, 0xE0)

        elif game_name == 'Emerald':
            if infinite_tms.get():
                romByteModifier.modify_byte_in_file(save_path, 0x1B6EE0, 0xA9, 0x90)
            if running_shoes.get():
                romByteModifier.modify_byte_in_file(save_path, 0x11A1E8, 0x08, 0x00)

        elif game_name == 'Platinum':
            if disable_frame_limiter.get():
                romByteModifier.modify_byte_in_file(save_path, 0x004DF8, 0x25, 0x00)
                romByteModifier.modify_byte_in_file(save_path, 0x004DF9, 0x63, 0x00)
            if infinite_tms.get():
                platinumROMModifier.platinum_infinite_tms(save_path)

        elif game_name == 'HeartGold':
            if disable_frame_limiter.get():
                romByteModifier.modify_byte_in_file(save_path, 0x004E28, 0x25, 0x00)
                romByteModifier.modify_byte_in_file(save_path, 0x004E29, 0x63, 0x00)
            if infinite_tms.get():
                heartGoldSoulSilverROMModifier.heartgold_soulsilver_infinite_tms(save_path)

        elif game_name == 'SoulSilver':
            if disable_frame_limiter.get():
                romByteModifier.modify_byte_in_file(save_path, 0x004E28, 0x25, 0x00)
                romByteModifier.modify_byte_in_file(save_path, 0x004E29, 0x63, 0x00)
            if infinite_tms.get():
                heartGoldSoulSilverROMModifier.heartgold_soulsilver_infinite_tms(save_path)

        elif game_name == 'Colosseum':
            if infinite_tms.get():
                romByteModifier.apply_ips_patch("clean.dol", "modified.dol", "patches/colo_infinite_tms.ips")
            if save_anywhere.get():
                romByteModifier.apply_ips_patch("clean.dol", "modified.dol", "patches/colo_save_anywhere.ips")

        elif game_name == 'XD':
            if infinite_tms.get():
                romByteModifier.apply_ips_patch("clean.dol", "modified.dol", "patches/xd_infinite_tms.ips")
            if disable_battle_animations.get():
                romByteModifier.apply_ips_patch("clean.dol", "modified.dol", "patches/xd_disable_battle_animations.ips")

        if game_name == 'Colosseum' or game_name == 'XD':
            dolString = "start.dol"
            gamecubeISOModifier.write_gamecube(save_path, dolString.encode("ascii"), "modified.dol")

        patch_window.destroy()
        messagebox.showinfo("Done", f"Patching for {game_name} is complete!")

        if os.path.exists("clean.dol"):
            os.remove("clean.dol")

        if os.path.exists("modified.dol"):
            os.remove("modified.dol")

    def on_window_close():
        patch_window.destroy()

    patch_window = tk.Toplevel()
    patch_window.title(f"Select Patches for {game_name}")
    patch_window.protocol("WM_DELETE_WINDOW", on_window_close)

    infinite_tms = tk.BooleanVar()
    running_shoes = tk.BooleanVar()
    national_dex_evos = tk.BooleanVar()
    disable_frame_limiter = tk.BooleanVar()
    save_anywhere = tk.BooleanVar()
    disable_battle_animations = tk.BooleanVar()

    tk.Checkbutton(patch_window, text="Infinite TMs", variable=infinite_tms).pack(anchor="w")
    if game_name in ['FireRed', 'LeafGreen', 'Emerald']:
        tk.Checkbutton(patch_window, text="Running Shoes Indoors", variable=running_shoes).pack(anchor="w")
    if game_name in ['FireRed', 'LeafGreen']:
        tk.Checkbutton(patch_window, text="Evolutions Don't Require National Dex", variable=national_dex_evos).pack(anchor="w")
    if game_name in ['Platinum', 'HeartGold', 'SoulSilver']:
        tk.Checkbutton(patch_window, text="Disable Frame Limiter", variable=disable_frame_limiter).pack(anchor="w")
    if game_name in ['Colosseum']:
        tk.Checkbutton(patch_window, text="Save Anywhere (Press R in overworld)", variable=save_anywhere).pack(anchor="w")
    if game_name in ['XD']:
        tk.Checkbutton(patch_window, text="Disable Battle Animations", variable=disable_battle_animations).pack(anchor="w")

    tk.Button(patch_window, text="Apply Patches", command=apply_patches).pack(pady=10)
    patch_window.wait_window(patch_window)

root = tk.Tk()
root.title("Pokemon QoL Patcher")
icon = PhotoImage(file='images/tm-icon.png')
root.iconphoto(True, icon)

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
colosseum_img = load_image("images/colosseum.png")
xd_img = load_image("images/xd.png")

button1 = tk.Button(frame1, image=fire_red_img, command=lambda: open_file('FireRed'))
button1.grid(row=0, column=0, padx=10, pady=10)

button2 = tk.Button(frame1, image=leaf_green_img, command=lambda: open_file('LeafGreen'))
button2.grid(row=0, column=1, padx=10, pady=10)

button3 = tk.Button(frame1, image=emerald_img, command=lambda: open_file('Emerald'))
button3.grid(row=0, column=2, padx=10, pady=10)

button4 = tk.Button(frame1, image=platinum_img, command=lambda: open_file('Platinum'))
button4.grid(row=0, column=3, padx=10, pady=10)

button5 = tk.Button(frame1, image=heart_gold_img, command=lambda: open_file('HeartGold'))
button5.grid(row=1, column=0, padx=10, pady=10)

button6 = tk.Button(frame1, image=soul_silver_img, command=lambda: open_file('SoulSilver'))
button6.grid(row=1, column=1, padx=10, pady=10)

button7 = tk.Button(frame1, image=colosseum_img, command=lambda: open_file('Colosseum'))
button7.grid(row=1, column=2, padx=10, pady=10)

button8 = tk.Button(frame1, image=xd_img, command=lambda: open_file('XD'))
button8.grid(row=1, column=3, padx=10, pady=10)

root.mainloop()
