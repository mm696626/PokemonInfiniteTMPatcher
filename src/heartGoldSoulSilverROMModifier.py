"""
Code is not written by me. Credit goes to Pseurae
Code: https://gist.github.com/Pseurae/3ef6b0285966db6f389974f8be8ab4d1
"""

import ndspy.rom
import ndspy.code

def make_tms_reusable(fname):
    rom = ndspy.rom.NintendoDSRom.fromFile(fname)

    arm9 = rom.loadArm9()
    arm9.sections[0].data[0x825A0:0x825A4] = bytearray(b"\x00" * 4)
    arm9.sections[0].data[0x825A7:0x825A8] = bytearray(b"\xE0")
    rom.arm9 = arm9.save(compress=True)

    overlay15: ndspy.code.Overlay = rom.loadArm9Overlays(idsToLoad=[15])[15]
    overlay15.data[0x6236:0x6238] = bytearray(b"\x00" * 2)
    overlay15.data[0x6239:0x623A] = bytearray(b"\xE0")
    rom.files[overlay15.fileID] = overlay15.save(compress=True)

    rom.saveToFile(fname)

def heartgold_soulsilver_infinite_tms(file_path):
    make_tms_reusable(file_path)