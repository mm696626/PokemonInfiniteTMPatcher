"""
Code is not written by me. Credit goes to everyone who wrote code to this repo
Code: https://github.com/pfirsich/gciso
"""

from src import gciso

# gciso write isofile internalfile srcfile [--offset X] [--banner]
def write_gamecube(isoFile, internalFile, srcFile, offset=0, banner=False):
    if banner:
        raise NotImplementedError("Writing banners is not implemented yet!")
    with gciso.IsoFile(isoFile) as iso, open(srcFile, "rb") as src:
        iso.writeFile(internalFile, offset, src.read())

# gciso read isofile internalfile dstfile [--offset X] [--length X] [--banner]
def read_gamecube(isoFile, internalFile, dstFile, offset=0, length=None, banner=False):
    with gciso.IsoFile(isoFile) as iso:
        if banner:
            banner = iso.getBannerFile(internalFile)
            banner.getPILImage().save(dstFile)
        else:
            with open(dstFile, "wb") as dst:
                dst.write(iso.readFile(internalFile, offset, length))