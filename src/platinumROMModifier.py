"""
Code is not written by me. Credit goes to Pseurae
Code: https://gist.github.com/Pseurae/3c47b93bec10f9a1b1792466e26c456d
"""

from io import SEEK_SET
import ndspy.rom
import ndspy.narc

BAG_TM_COUNT_PRINT_BL = 0x08A5F8
TM_DECREMENT_AFTER_USE_BL = 0x36A972


def insert_zeros(f, offset, n=2):
    f.seek(offset, SEEK_SET)
    f.write(b"\x00" * n)


def set_tms_as_important(fname):
    rom = ndspy.rom.NintendoDSRom.fromFile(fname)
    item_data_bytes = rom.getFileByName("itemtool/itemdata/pl_item_data.narc")
    item_data = ndspy.narc.NARC(item_data_bytes)
    files = item_data.files

    # for i in range(306, 398):
    for i in range(len(files)):
        struct = files[i]
        bitfield = struct[8] | struct[9] << 8

        pocket = (bitfield >> 7) & 0b1111
        imp = (bitfield >> 5) & 0b1

        if pocket != 3 or imp:
            continue

        struct[8] |= 0b00100000
        files[i] = struct

    new_item_data_bytes = item_data.save()
    rom.setFileByName("itemtool/itemdata/pl_item_data.narc", new_item_data_bytes)
    rom.saveToFile(fname)


def platinum_infinite_tms(file_path):
    set_tms_as_important(file_path)

    with open(file_path, "rb+") as f:
        insert_zeros(f, BAG_TM_COUNT_PRINT_BL, 4)
        insert_zeros(f, TM_DECREMENT_AFTER_USE_BL, 4)
