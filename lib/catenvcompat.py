
#
# Catware catENV backward compatibility library.
#
# Когда-то, в catENV функции назывались в CamelCase. Отныне все по-другому, все встало как в пеп8 задано, но чтобы не ломать совместимость, мы захуярили этот пиздец...
#
# Требует самого свежего катенва нахуй!!!
#

def HostToIp(host):
    return hosttoip(host)

def Geocode(address):
    return geocode(address)

def RandomInt(ot, do):
    return randomint(ot, do)

def PlusWrite(text, target):
    pluswrite(text, target)

def Get(url):
    return get(url)

def ShortUrl(url):
    return shorturl(url)

def InstallPackage(package): #кто это блять использует мне интересно....................
    return installpackage(package)

def ReadFF(target):
    return readff(target)

def CallSystem(command):
    return callsystem(command)

def Run(file):
    run(file)

def Download(url, fn):
    download(url, fn)

def Similar(frst, scnd):
    return similar(frst, scnd)

def TextToBits(aye):
    return texttobits(aye)

def TextFromBits(blyat):
    return textfrombits(aye)

def CreateFile(ayename):
    createfile(ayename)

def Reverse(s):
    return reverse(s)

def RandomLetter():
    return randomletter()

def writeTo(txt, trgt):
    writeto(txt, trgt)
