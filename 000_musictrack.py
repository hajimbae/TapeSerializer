import binascii
import json
import zlib
import os

print("JUST DANCE MUSICTRACK ENCRYPTOR BY YUNYL")
musictrack = input("Name of JDU musictrack: ")

with open(musictrack) as json_file:
    data = json.load(json_file)

b_ = b''
i = 0

codename = data['COMPONENTS'][i]['trackData']['path'].split('/')[-1][:-4]
codename_wii = (("WII_" + codename))
codename_wii_musictrack = codename_wii + "_musictrack.tpl.ckd"

OUTPUT = codename_wii_musictrack
ENCODING = 'utf-8'

# configuration
startbeat = msc_signatures_sections = binascii.unhexlify(str.encode("FFFFFFFC"))
print(startbeat)

endbeat = data['COMPONENTS'][i]['trackData']['structure']['endBeat'].to_bytes(4, 'big')
print(endbeat)

howmanyclipsinktape = (len(data['COMPONENTS']))
howmanyclipsinktapeadd10000 = howmanyclipsinktape * 2000 + 3514
howmanyclipsinktapehexreadywith10000 = (hex(int(howmanyclipsinktapeadd10000)).replace("0x", ""))
howmanyzero = int(8 - (len(howmanyclipsinktapehexreadywith10000)))
test1 = (str("0") * howmanyzero) + str(howmanyclipsinktapehexreadywith10000)
print(startbeat)

# useless stuff
msc_start = binascii.unhexlify(str.encode(
    "00000001" + test1 +  "1B857BCE0000006C000000000000000000000000000000000000000000000000000000000000000102883A7E000000A0000000900000006C"))
print(msc_start)

# markers
msc_markers = data['COMPONENTS'][i]['trackData']['structure']['markers']
msc_markers_tohex = b''.join(map(lambda x: x.to_bytes(4, 'big'), msc_markers))
print(msc_markers_tohex)

# markers length
msc_markers_length = data['COMPONENTS'][i]['trackData']['structure']['endBeat']
msc_markers_length_tohex = msc_markers_length.to_bytes(4, 'big')
print(msc_markers_length)

# useless signatures & sections together
msc_signatures_sections = binascii.unhexlify(str.encode(
    "000000010000000800000010000000040000000F00000014000000000000000000000000000000140000001000000004000000000000001400000020000000030000000000000014000000300000000100000000000000140000004800000003000000000000001400000068000000010000000000000014000000780000000400000000000000140000008800000007000000000000001400000098000000030000000000000014000000A8000000020000000000000014000000C8000000010000000000000014000000D8000000020000000000000014000000E8000000030000000000000014000000F80000000300000000000000140000010800000005"))
print(msc_signatures_sections)

# idk about this part?? maybe videostarttime etc.
beforestartbeat = binascii.unhexlify(str.encode("00000000"))

videostarttime = binascii.unhexlify(str.encode("00000000"))

aftervideo = binascii.unhexlify(str.encode("0000000000000000000000000000000000000000"))

# codename.wav
wavname = codename + ".wav"
wavname_tohex = wavname.encode()
print(wavname_tohex)

# wav length to hex
wavname_length = len(wavname).to_bytes(4, 'big')
print(wavname_length)

# wav path
wavpath = "world/maps/" + codename + "/audio/"
wavpath_tohex = wavpath.encode()
print(wavpath_tohex)

# wav path length to hex
wavpath_length = len(wavpath).to_bytes(4, 'big')
print(wavpath_length)

# wav name crc32
wavname_crc32 = zlib.crc32(wavname.encode('utf-8')).to_bytes(4, 'little')
print(wavname_crc32)

# useless between endbeat and videostarttime
useless2 = binascii.unhexlify(str.encode("00000000000000000000"))

# useless ending
msc_end = binascii.unhexlify(str.encode("0000000000000000"))
print(msc_end)

everything_together = msc_start + msc_markers_length_tohex + msc_markers_tohex + msc_signatures_sections + beforestartbeat + startbeat + endbeat + useless2 + videostarttime + aftervideo + wavname_length + wavname_tohex + wavpath_length + wavpath_tohex + wavname_crc32 + msc_end

print(everything_together)

i = i + 1
with open(codename_wii_musictrack, "ab") as g:
    g.write(everything_together)
    g.close()
