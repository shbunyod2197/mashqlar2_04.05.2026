# 1
class KItob:
    def __init__(self, nomi, narxi):
        self.nomi = nomi
        self.narx = narxi

    def chegirma(self, qiymat):
        self.narx -= qiymat

    def info(self):
        print(self.nomi)
        print(self.narx)


a = KItob("ajoyib", 30)
a.info()
a.chegirma(100)

# 2
class Talaba:
    def __init__(self, fulname, ball):
        self.fulname = fulname
        self.ball = ball

    def ball_qosh(self, qiymat):
        self.ball += qiymat

    def info(self):
        print(self.fulname, self.ball)


a = Talaba("", 999)
a.info()
a.ball_qosh(999)

# 3
class BankHisob:
    def __init__(self, egasi):
        self.egasi = egasi
        self.__balase = 0

    def pul_qosh(self, summ):
        self.__balase += summ

    def pul_ayir(self, summ):
        self.__balase -= summ

    def info(self):
        print(self.egasi)
        print(self.__balase)

a = BankHisob("bunyod")
a.pul_qosh(1000)
a.pul_ayir(100)
a.info()

# 4
class Telefon:
    def __init__(self, model, batareya):
        self.model = model
        self.batareya = batareya

    def zaryad_qil(self, foiz):
        self.batareya += foiz

    def foydalan(self, foiz):
        self.batareya -= foiz

    def info(self):
        print(self.model)
        print(self.batareya)


a = Telefon("iphone", 40)
a.info()
a.zaryad_qil(70)
a.info()

# 5
class Ishchi:
    def __init__(self, fulname, oylik):
        self.fulname = fulname
        self.oylik = oylik

    def oshirish(self, q):
        self.oylik += q

    def kamaytirish(self, q):
        self.oylik -= q

    def info(self):
        print(self.fulname, self.oylik)

a = Ishchi("ajyt",8888)
a.info()

# 6
class Avtomobil:
    def __init__(self, model, tezlik):
        self.model = model
        self.tezlik = tezlik

    def tezlashtir(self, qiymat):
        self.tezlik -= qiymat

    def kamaytir(self, qiymat):
        self.tezlik -= qiymat

    def info(self):
        print(self.model)
        print(self.tezlik)


a = Avtomobil("a", 399)
a.info()


# 7
class Dokon:
    def __init__(self, name):
        self.nomi = name
        self.__kassa = 0

    def sotuv(self, s):
        self.__kassa += s

    def harajat(self, s):
        self.__kassa -= s

    def info(self):
        print(self.__kassa)


a = Dokon("")
a.info()

# 8
class Bak:
    def __init__(self,sigim, yoqilgi ):
        self.sigim = sigim
        self.yoqilgi = yoqilgi

    def qosh(self, q):
        self.yoqilgi += q


    def ayir(self, a):
        self.yoqilgi -= a


    def info(self):
        print(self.yoqilgi)

a = Bak("agiaug", 89)
a.info()

# 9
class KUrs:
    def __init__(self, nomi, study_soni):
        self.nomi = nomi
        self.study_soni = study_soni

    def qosh(self,a):
        self.study_soni += a

    def ayir(self, a):
        self.study_soni -= a

    def info(self):
        print(self.nomi, self.study_soni)


a = KUrs(123, 123)
a.qosh(123)
a.ayir(123)

# 10
class Stadion:
    def __init__(self, name, muhlislar):
        self.name = name
        self.muhlis = muhlislar

    def kirish(self, a):
        self.muhlis += a

    def chiq(self, a):
        self.muhlis += a

    def info(self):
        print(self.name)
        print(self.muhlis)


a = Stadion("", 100)
a.info()

# 11
class Kompuyuter:
    def __init__(self, name, xotira):
        self.nomi = name
        self.xotira = xotira

    def yuklash(self, gb):
        self.xotira -= gb

    def ochirish(self, gb):
        self.xotira = gb

    def info(self):
        print(self.nomi)
        print(self.xotira)


a = Kompuyuter("", 100)
a.info()

# 12
class Kino:
    def __init__(self, nomi, reyting):
        self.nomi = nomi
        self.reyting = reyting

    def baho_qosh(self, baho):
        self.reyting = baho

    def info(self):
        print(self.nomi)
        print(self.reyting)


a = Kino(123, 2)
a.baho_qosh(a)

# 13
class Universitet:
    def __init__(self, name, studentlar):
        self.name = name
        self.studentlar = studentlar

    def qabul(self, n):
        self.studentlar += n

    def bitiruv(self, n):
        self.studentlar -= n

    def info(self):
        print(self.name)
        print(self.studentlar)


av = Universitet("", "")
av.info()

# 14
class Kafe:
    def __init__(self, nomi, daromat):
        self.nomi = nomi
        self.daromat = daromat

    def sotuv(self, a):
        self.daromat += a

    def harajat(self, a):
        self.daromat -= a


    def info(self):
        print(self.nomi, self.daromat)


a = Kafe('+', '-')
a.info()

# 15
class Uy:
    def __init__(self, manzuil, narx):
        self.manzil = manzuil
        self.narx = narx

    def narx_osh(self, a):
        self.narx += a

    def narx_tush(self, a):
        self.narx -= a

    def info(self):
        print(self.manzil, self.narx)


a = Uy('manzuil', 100)
a.info()


# 16
class Sportchi:
    def __init__(self, ism, ochko):
        self.ism = ism
        self.ochko = ochko

    def gol_ur(self, n):
        self.ochko += n

    def info(self):
        print(self.ism, self.ochko)

a = Sportchi("Ali", 900)
a.gol_ur(10)
a.info()
a.gol_ur(20)

# 17
class Oyin:
    def __init__(self, nomi, level):
        self.nomi = nomi
        self.level = level

    def level_osh(self):
        self.level += 1

    def level_tush(self):
        self.level -= 1

    def info(self):
        print(self.nomi, self.level)


a = Oyin(1, 2)
a.level_osh()
a.level_tush()

# 18
class Kutubxona:
    def __init__(self, nomi, kitob_soni):
        self.nomi = nomi
        self.kitob_soni = kitob_soni

    def qoshish(self, n):
        self.kitob_soni += n

    def olishish(self, n):
        self.kitob_soni -= n

    def info(self):
        print(self.kitob_soni)
        print(self.nomi)


a = Kutubxona(1, 2)
a.info()

# 19
class Dars:
    def __init__(self, nomi, soat):
        self.nomi = nomi
        self.soat = soat

    def oshir(self, m):
        self.soat += m

    def kamaytir(self, m):
        self.soat -= m

    def info(self):
        print(self.nomi, self.soat)


a = Dars("", "")
a.info()

# 20
class Internet:
    def __init__(self, egasi, mb):
        self.egasi = egasi
        self.mb = mb

    def ishlat_mb(self, mb):
        self.mb -= mb

    def qosh(self, mb):
        self.mb += mb

    def info(self):
        print(self.egasi)
        print(self.mb)


a = Internet(2, 3)
a.ishlat_mb(3)
a.qosh(3)


# 21
class Oila:
    def __init__(self, familiya, azolar_soni):
        self.familiya = familiya
        self.azolar_soni = azolar_soni

    def qoshish(self):
        self.azolar_soni += 1

    def kamaytirish(self):
        self.azolar_soni -= 1

    def info(self):
        print(self.familiya, self.azolar_soni)


a = Oila("vey", 100)
a.qoshish()
a.info()

# 22
class Restoran:
    def __init__(self, nomi, mihozi):
        self.nomi = nomi
        self.mihozi = mihozi

    def kelish(self, a):
        self.mihozi += a

    def ketish(self, a):
        self.mihozi -= a

    def info(self):
        print(self.nomi, self.mihozi)

a = Restoran(123, 456)
a.info()

# 23
class Oqituvchi:
    def __init__(self, ism, maosh):
        self.ism = ism
        self.maosh = maosh

    def oshir(self, a):
        self.maosh += a

    def kamaytr(self, a):
        self.ism += a

    def info(self):
        print(self.ism)
        print(self.maosh)


a = Oqituvchi("ali", 6)
a.info()

# 24
class Ombor:
    def __init__(self, nomi, mahsulot_soni):
        self.nomi = nomi
        self.mahsulot_soni = mahsulot_soni

    def qabul(self, a):
        self.mahsulot_soni += a

    def kamaytir(self, a):
        self.mahsulot_soni -= a

    def info(self):
        print(self.mahsulot_soni, self.nomi)

a = Ombor(1, 1)
a.qabul(1)
a.kamaytir(1)

# 25
class Hisoblagich:
    def __init__(self, qiymat):
        self.qiymat = qiymat

    def oshy(self):
        self.qiymat += 1

    def kamay(self):
        self.qiymat -= 1

    def info(self):
        print(self.qiymat)

a = Hisoblagich(10)
a.oshy()
a.kamay()
