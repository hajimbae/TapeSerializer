import binascii
import json
import zlib
import os
print("JUST DANCE DTAPE ENCRYPTOR BY YUNYL")
jdudtape = input("Name of JDU dtape: ")

with open(jdudtape) as json_file:
    data = json.load(json_file)

i = 0

msmopenskobka = "955384A1"
msmcliptype = "00000070"
pictocliptype = "00000038"
goldeffecttype = "0000001C"
thingaftermsmpath = "496D424500000000"
msmcloseskobka = "3F7CFCFE3F30B0B13F5CDCDE3F80000000000003000000010000000C3F8000000000000000000000000000030000000C3F80000000000000000000000000000A0000000C3F8000000000000000000000"
pictoopenskobka = "52EC8962"
pictocloseskobka = "5BC2D82F00000000FFFFFFFF"
goldeffectopenskobka = "FD69B110"
songname = (json.dumps(data['MapName'], sort_keys=False, indent=4).lower())
songnamenormal = songname[1:-1]
msmpath = "world/maps/" + songnamenormal + "/timeline/moves/"
pictopath = "world/maps/" + songnamenormal + "/timeline/pictos/"

songname = (json.dumps(data['MapName'], sort_keys=False, indent=4).lower())
songnamenormal = songname[1:-1]
songnameready = (("WII_" + songnamenormal))
songnamereadyt = songnameready + "_tml_dance.dtape.ckd"
filewhereput = open(songnamereadyt, "w")
howmanyclipsinktape = (len(data['Clips']))
howmanyclipsinktapeadd10000 = howmanyclipsinktape * 200 + 3514
howmanyclipsinktapehexreadywith10000 = (hex(int(howmanyclipsinktapeadd10000)).replace("0x", ""))
howmanyzero = int(8 - (len(howmanyclipsinktapehexreadywith10000)))
test1 = (str("0") * howmanyzero) + str(howmanyclipsinktapehexreadywith10000)

dtapestart = "00000001" + test1 + "9E8454600000009C"
mapname = (json.dumps(data['MapName'], sort_keys=False, indent=4))
mapnamenormal = mapname[1:-1]
s = mapnamenormal.rstrip()
mapnamenormalhex = "".join("{:02x}".format(ord(c)) for c in s)
mapnamelength = (len(data['MapName']))
mapnamelengthexready = (hex(int(mapnamelength)).replace("0x", ""))
howmanyzero = int(8 - (len(mapnamelengthexready)))
mapnamelengthexandzero = (str("0") * howmanyzero) + str(mapnamelengthexready)
dtapeend = "0000000000000000000000000000000100000000" + mapnamelengthexandzero + mapnamenormalhex
howmanyclipsinktape = (len(data['Clips']))
howmanyclipsinktapehexready = (hex(int(howmanyclipsinktape)).replace("0x", ""))
howmanyzero = int(8 - (len(howmanyclipsinktapehexready)))
howmanymarkersandzero = (str("0") * howmanyzero) + str(howmanyclipsinktapehexready)
howmanymarkersencrypted = binascii.unhexlify(dtapestart + howmanymarkersandzero)
with open(songnamereadyt, "ab") as tr:
    tr.write(howmanymarkersencrypted)
    tr.close()

while i < howmanyclipsinktape:
    cliptype = ((json.dumps(data['Clips'][i]['__class'], sort_keys=False, indent=4))[1:-1])
    if cliptype == "MotionClip":
        clipidmsm = int(json.dumps(data['Clips'][i]['Id'], sort_keys=False, indent=4))
        trackidmsm = int(json.dumps(data['Clips'][i]['TrackId'], sort_keys=False, indent=4))
        isactivemsm = int(json.dumps(data['Clips'][i]['IsActive'], sort_keys=False, indent=4))
        starttimemsm = int(json.dumps(data['Clips'][i]['StartTime'], sort_keys=False, indent=4))
        durationmsm = int(json.dumps(data['Clips'][i]['Duration'], sort_keys=False, indent=4))
        namerawmsm = (json.dumps(data['Clips'][i]['ClassifierPath'], sort_keys=False, indent=4))
        namemsm1 = (json.dumps(data['Clips'][i]['ClassifierPath'], sort_keys=False, indent=4)).split('/')[-1][
                   :-1]  # [((len(msmpath)) + 3):-1]
        goldmovemsm = int(json.dumps(data['Clips'][i]['GoldMove'], sort_keys=False, indent=4))
        coachidmsm = int(json.dumps(data['Clips'][i]['CoachId'], sort_keys=False, indent=4))
        movetypemsm = int(json.dumps(data['Clips'][i]['MoveType'], sort_keys=False, indent=4))

        clipidmsmhex = (hex(clipidmsm).replace("0x", ""))
        howmanyzero = int(8 - (len(clipidmsmhex)))
        clipidmsmhexready = (str("0") * howmanyzero) + str(clipidmsmhex)

        trackidmsmhex = (hex(trackidmsm).replace("0x", ""))
        howmanyzero = int(8 - (len(trackidmsmhex)))
        trackidmsmhexready = (str("0") * howmanyzero) + str(trackidmsmhex)

        isactivemsmhex = (hex(isactivemsm).replace("0x", ""))
        howmanyzero = int(8 - (len(isactivemsmhex)))
        isactivemsmhexready = (str("0") * howmanyzero) + str(isactivemsmhex)

        starttimemsmhex = (hex(starttimemsm).replace("0x", ""))
        howmanyzero = int(8 - (len(starttimemsmhex)))
        starttimemsmhexready = (str("0") * howmanyzero) + str(starttimemsmhex)

        durationmsmhex = (hex(durationmsm).replace("0x", ""))
        howmanyzero = int(8 - (len(durationmsmhex)))
        durationmsmhexready = (str("0") * howmanyzero) + str(durationmsmhex)

        s = namemsm1

        thingaftermsmpath = "00000000"

       # print('thingaftermsmpath', bytes.fromhex(thingaftermsmpath))
       # print('a', zlib.crc32(s.encode('utf-8')).to_bytes(4, 'little'))

       # print('add the two together')
        thingaftermsmpath = zlib.crc32(s.encode('utf-8')).to_bytes(4, 'little') + bytes.fromhex(thingaftermsmpath)

        thingaftermsmpath = str(binascii.hexlify(thingaftermsmpath).decode('utf-8'))

       # print('thingaftermsmpath', thingaftermsmpath)

        namemsm1hex = "".join("{:02x}".format(ord(c)) for c in s)

        namemsm1lentohex = (hex(len(namemsm1))).replace("0x", "")
        howmanyzero = int(8 - (len(namemsm1lentohex)))
        namemsm1hexlenhexready = (str("0") * howmanyzero) + str(namemsm1lentohex)

        a = msmpath
        msmpathhex = "".join("{:02x}".format(ord(c)) for c in a)

        namemsm1lentohe2x = (hex(len(msmpath))).replace("0x", "")
        howmanyzero = int(8 - (len(namemsm1lentohe2x)))
        msmpathhexlenhexready = (str("0") * howmanyzero) + str(namemsm1lentohe2x)

        goldmovemsmhex = (hex(goldmovemsm).replace("0x", ""))
        howmanyzero = int(8 - (len(goldmovemsmhex)))
        goldmovemsmhexready = (str("0") * howmanyzero) + str(goldmovemsmhex)

        coachidmsmhex = (hex(coachidmsm).replace("0x", ""))
        howmanyzero = int(8 - (len(coachidmsmhex)))
        coachidmsmhexready = (str("0") * howmanyzero) + str(coachidmsmhex)

        movetypemsmhex = (hex(movetypemsm).replace("0x", ""))
        howmanyzero = int(8 - (len(movetypemsmhex)))
        movetypemsmhexready = (str("0") * howmanyzero) + str(movetypemsmhex)

        dataencrypted = binascii.unhexlify(
            msmopenskobka + msmcliptype + clipidmsmhexready + trackidmsmhexready + isactivemsmhexready +
            starttimemsmhexready + durationmsmhexready + namemsm1hexlenhexready + namemsm1hex + msmpathhexlenhexready +
            msmpathhex + thingaftermsmpath + goldmovemsmhexready + coachidmsmhexready + movetypemsmhexready +
            msmcloseskobka)
        i = i + 1
        with open(songnamereadyt, "ab") as g:
            g.write(dataencrypted)
            g.close()
    elif cliptype == "PictogramClip":
        clipidmsm = int(json.dumps(data['Clips'][i]['Id'], sort_keys=False, indent=4))
        trackidmsm = int(json.dumps(data['Clips'][i]['TrackId'], sort_keys=False, indent=4))
        isactivemsm = int(json.dumps(data['Clips'][i]['IsActive'], sort_keys=False, indent=4))
        starttimemsm = int(json.dumps(data['Clips'][i]['StartTime'], sort_keys=False, indent=4))
        durationmsm = int(json.dumps(data['Clips'][i]['Duration'], sort_keys=False, indent=4))
        namepicto1 = (json.dumps(data['Clips'][i]['PictoPath'], sort_keys=False, indent=4)).split('/')[-1][
                     :-1]  # [((len(pictopath)) + 3):-1]

        clipidmsmhex = (hex(clipidmsm).replace("0x", ""))
        howmanyzero = int(8 - (len(clipidmsmhex)))
        clipidmsmhexready = (str("0") * howmanyzero) + str(clipidmsmhex)

        trackidmsmhex = (hex(trackidmsm).replace("0x", ""))
        howmanyzero = int(8 - (len(trackidmsmhex)))
        trackidmsmhexready = (str("0") * howmanyzero) + str(trackidmsmhex)

        isactivemsmhex = (hex(isactivemsm).replace("0x", ""))
        howmanyzero = int(8 - (len(isactivemsmhex)))
        isactivemsmhexready = (str("0") * howmanyzero) + str(isactivemsmhex)

        starttimemsmhex = (hex(starttimemsm).replace("0x", ""))
        howmanyzero = int(8 - (len(starttimemsmhex)))
        starttimemsmhexready = (str("0") * howmanyzero) + str(starttimemsmhex)

        durationmsmhex = (hex(durationmsm).replace("0x", ""))
        howmanyzero = int(8 - (len(durationmsmhex)))
        durationmsmhexready = (str("0") * howmanyzero) + str(durationmsmhex)

        e = namepicto1

        pictocloseskobka = "00000000FFFFFFFF"

        pictocloseskobka = zlib.crc32(e.encode('utf-8')).to_bytes(4, 'little') + bytes.fromhex(pictocloseskobka)
        # print('pictocloseskobka bytes', pictocloseskobka)

        pictocloseskobka = str(binascii.hexlify(pictocloseskobka).decode('utf-8'))

        # print('pictocloseskobka str', pictocloseskobka)

        namepicto1hex = "".join("{:02x}".format(ord(c)) for c in e)

        namemsm1lentohex = (hex(len(namepicto1))).replace("0x", "")
        howmanyzero = int(8 - (len(namemsm1lentohex)))
        namemsm1hexlenhexready = (str("0") * howmanyzero) + str(namemsm1lentohex)

        v = pictopath
        pictopathhex = "".join("{:02x}".format(ord(c)) for c in v)

        namepicto1lentohe2x = (hex(len(pictopath))).replace("0x", "")
        howmanyzero = int(8 - (len(namepicto1lentohe2x)))
        msmpathhexlenhexready = (str("0") * howmanyzero) + str(namepicto1lentohe2x)

        dataencrypted = binascii.unhexlify(
            pictoopenskobka + pictocliptype + clipidmsmhexready + trackidmsmhexready + isactivemsmhexready +
            starttimemsmhexready + durationmsmhexready + namemsm1hexlenhexready + namepicto1hex +
            msmpathhexlenhexready + pictopathhex + pictocloseskobka)
        i = i + 1
        with open(songnamereadyt, "ab") as g:
            g.write(dataencrypted)
            g.close()
    elif cliptype == "GoldEffectClip":
        clipidmsm = int(json.dumps(data['Clips'][i]['Id'], sort_keys=False, indent=4))
        trackidmsm = int(json.dumps(data['Clips'][i]['TrackId'], sort_keys=False, indent=4))
        isactivemsm = int(json.dumps(data['Clips'][i]['IsActive'], sort_keys=False, indent=4))
        starttimemsm = int(json.dumps(data['Clips'][i]['StartTime'], sort_keys=False, indent=4))
        durationmsm = int(json.dumps(data['Clips'][i]['Duration'], sort_keys=False, indent=4))
        effecttype = int(json.dumps(data['Clips'][i]['EffectType'], sort_keys=False, indent=4))

        clipidmsmhex = (hex(clipidmsm).replace("0x", ""))
        howmanyzero = int(8 - (len(clipidmsmhex)))
        clipidmsmhexready = (str("0") * howmanyzero) + str(clipidmsmhex)

        trackidmsmhex = (hex(trackidmsm).replace("0x", ""))
        howmanyzero = int(8 - (len(trackidmsmhex)))
        trackidmsmhexready = (str("0") * howmanyzero) + str(trackidmsmhex)

        isactivemsmhex = (hex(isactivemsm).replace("0x", ""))
        howmanyzero = int(8 - (len(isactivemsmhex)))
        isactivemsmhexready = (str("0") * howmanyzero) + str(isactivemsmhex)

        starttimemsmhex = (hex(starttimemsm).replace("0x", ""))
        howmanyzero = int(8 - (len(starttimemsmhex)))
        starttimemsmhexready = (str("0") * howmanyzero) + str(starttimemsmhex)

        durationmsmhex = (hex(durationmsm).replace("0x", ""))
        howmanyzero = int(8 - (len(durationmsmhex)))
        durationmsmhexready = (str("0") * howmanyzero) + str(durationmsmhex)

        effecttypehex = (hex(effecttype).replace("0x", ""))
        howmanyzero = int(8 - (len(effecttypehex)))
        effecttypehexready = (str("0") * howmanyzero) + str(effecttypehex)

        dataencrypted = binascii.unhexlify(
            goldeffectopenskobka + goldeffecttype + clipidmsmhexready + trackidmsmhexready + isactivemsmhexready + starttimemsmhexready + durationmsmhexready + effecttypehexready)
        i = i + 1
        with open(songnamereadyt, "ab") as g:
            g.write(dataencrypted)
            g.close()

if i == howmanyclipsinktape:
    dataencrypted = binascii.unhexlify(dtapeend)
    with open(songnamereadyt, "ab") as g:
        g.write(dataencrypted)
        g.close()
