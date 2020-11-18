import binascii
import json
import io
import unidecode
import os

import hanzidentifier  # to see if file contains chinese
import pinyin  # to convert chinese to english

# io.open("myfile.txt", 'r', encoding="windows-1252")
print("JUST DANCE KTAPE ENCRYPTOR BY YUNYL")
filename = input("Enter JDU ktape: ")

with io.open(filename, 'r', encoding="utf-8") as json_file:
    data = json.load(json_file)

# check all lyrics for chinese and convert to its english pronunciation
for track in data["Clips"]:
    # if the track contains chinese characters
    if hanzidentifier.has_chinese(track['Lyrics']):
        # convert to enlish
        track['Lyrics'] = pinyin.get(track['Lyrics'], format="strip", delimiter=" ") + " "

i = 0

songname = (json.dumps(data['MapName'], sort_keys=False, indent=4).lower())
songnamenormal = songname[1:-1]
songnameready = (( "WII_" + songnamenormal))
songnamereadyt = songnameready + "_tml_karaoke.ktape.ckd"
filewhereput = open(songnamereadyt, "w")
howmanyclipsinktape = (len(data['Clips']))
howmanyclipsinktapeadd10000 = howmanyclipsinktape * 200 + 3514
howmanyclipsinktapehexreadywith10000 = (hex(int(howmanyclipsinktapeadd10000)).replace("0x", ""))
howmanyzero = int(8 - (len(howmanyclipsinktapehexreadywith10000)))
test1 = (str("0") * howmanyzero) + str(howmanyclipsinktapehexreadywith10000)

ktapestart = "00000001" + test1 + "9E8454600000008C"

howmanyclipsinktape = (len(data['Clips']))
howmanyclipsinktapehexready = (hex(int(howmanyclipsinktape)).replace("0x", ""))
howmanyzero = int(8 - (len(howmanyclipsinktapehexready)))
howmanymarkersandzero = (str("0") * howmanyzero) + str(howmanyclipsinktapehexready)
howmanymarkersencrypted = binascii.unhexlify(ktapestart + howmanymarkersandzero)

with open(songnamereadyt, "ab") as tr:
    tr.write(howmanymarkersencrypted)
    tr.close()

while i < int(howmanyclipsinktape):
    clipid = int(json.dumps(data['Clips'][i]['Id'], sort_keys=False, indent=4))
    trackid = int(json.dumps(data['Clips'][i]['TrackId'], sort_keys=False, indent=4))
    isactive = int(json.dumps(data['Clips'][i]['IsActive'], sort_keys=False, indent=4))
    starttime = int(json.dumps(data['Clips'][i]['StartTime'], sort_keys=False, indent=4))
    duration = int(json.dumps(data['Clips'][i]['Duration'], sort_keys=False, indent=4))
    lyricslength = (len(data['Clips'][i]['Lyrics']))

    lyrics = unidecode.unidecode(data['Clips'][i]['Lyrics'])

    # lyrics = (json.dumps(data['Clips'][i]['Lyrics'], sort_keys=False, indent=4))

    isendofline = int(json.dumps(data['Clips'][i]['IsEndOfLine'], sort_keys=False, indent=4))
    contenttype = int(json.dumps(data['Clips'][i]['ContentType'], sort_keys=False, indent=4))
    starttimetolerance = int(json.dumps(data['Clips'][i]['StartTimeTolerance'], sort_keys=False, indent=4))
    endtimetolerance = int(json.dumps(data['Clips'][i]['EndTimeTolerance'], sort_keys=False, indent=4))

    mapname = (json.dumps(data['MapName'], sort_keys=False, indent=4))
    mapnamenormal = mapname[1:-1]
    s = mapnamenormal.rstrip()
    mapnamenormalhex = "".join("{:02x}".format(ord(c)) for c in s)
    mapnamelength = (len(data['MapName']))
    mapnamelengthexready = (hex(int(mapnamelength)).replace("0x", ""))
    howmanyzero = int(8 - (len(mapnamelengthexready)))
    mapnamelengthexandzero = (str("0") * howmanyzero) + str(mapnamelengthexready)
    ktapeend = "000000000000000000000000000000000000000100000000" + mapnamelengthexandzero + mapnamenormalhex
    ktapeclipskobkaopen = "68552A41"
    ktapecliptype = "00000050"
    ktapepitch = "410A9761"
    ktapeclipskobkaclose = "40C00000"

    clipidhex = (hex(clipid).replace("0x", ""))
    howmanyzero = int(8 - (len(clipidhex)))
    clipidhexready = (str("0") * howmanyzero) + str(clipidhex)

    trackidhex = (hex(trackid).replace("0x", ""))
    howmanyzero = int(8 - (len(trackidhex)))
    trackidhexready = (str("0") * howmanyzero) + str(trackidhex)

    isactivehex = (hex(isactive).replace("0x", ""))
    howmanyzero = int(8 - (len(isactivehex)))
    isactivehexready = (str("0") * howmanyzero) + str(isactivehex)

    starttimehex = (hex(starttime).replace("0x", ""))
    howmanyzero = int(8 - (len(starttimehex)))
    starttimehexready = (str("0") * howmanyzero) + str(starttimehex)

    durationhex = (hex(duration).replace("0x", ""))
    howmanyzero = int(8 - (len(durationhex)))
    durationhexready = (str("0") * howmanyzero) + str(durationhex)

    lyricslengthhex = (hex(lyricslength).replace("0x", ""))
    howmanyzero = int(8 - (len(lyricslengthhex)))
    lyricslengthhexready = (str("0") * howmanyzero) + str(lyricslengthhex)

    # s is removing the space at the end of the lyrics
    s = lyrics
    lyricshex = "".join("{:02x}".format(ord(c)) for c in s)

    namemsm1lentohex = (hex(len(lyrics))).replace("0x", "")
    howmanyzero = int(8 - (len(namemsm1lentohex)))
    namemsm1hexlenhexready = (str("0") * howmanyzero) + str(namemsm1lentohex)

    # c.decode('utf8')

    isendoflinehex = (hex(isendofline).replace("0x", ""))
    howmanyzero = int(8 - (len(isendoflinehex)))
    isendoflinehexready = (str("0") * howmanyzero) + str(isendoflinehex)

    contenttypehex = (hex(contenttype).replace("0x", ""))
    howmanyzero = int(8 - (len(contenttypehex)))
    contenttypehexready = (str("0") * howmanyzero) + str(contenttypehex)

    starttimetolerancehex = (hex(starttimetolerance).replace("0x", ""))
    howmanyzero = int(8 - (len(starttimetolerancehex)))
    starttimetolerancehexready = (str("0") * howmanyzero) + str(starttimetolerance)

    endtimetolerancehex = (hex(endtimetolerance).replace("0x", ""))
    howmanyzero = int(8 - (len(endtimetolerancehex)))
    endtimetolerancehexready = (str("0") * howmanyzero) + str(endtimetolerance)

    dataencrypted = binascii.unhexlify(
        ktapeclipskobkaopen + ktapecliptype + clipidhexready + trackidhexready + isactivehexready + starttimehexready + durationhexready + ktapepitch + lyricslengthhexready + lyricshex + isendoflinehexready + contenttypehexready + starttimetolerancehexready + endtimetolerancehexready + ktapeclipskobkaclose)
    i = i + 1
    with open(songnamereadyt, "ab") as g:
        g.write(dataencrypted)
        g.close()

    if i == int(howmanyclipsinktape):
        ktapeendhex = binascii.unhexlify(ktapeend)
        with open(songnamereadyt, "ab") as g:
            g.write(ktapeendhex)
            g.close()
