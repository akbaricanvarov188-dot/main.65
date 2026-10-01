class Hayvon:
    def __init__(self, nomi, yoshi):
        self.nomi = nomi
        self.yoshi = yoshi

    def malumot(self):
        print("Nomi:", self.nomi)
        print("Yoshi:", self.yoshi)


hayvon = Hayvon("Mushuk", 2)
hayvon.malumot()

class Futbolchi:
    def __init__(self, ism, jamoa, raqam):
        self.ism = ism
        self.jamoa = jamoa
        self.raqam = raqam

    def malumot(self):
        print("Ism:", self.ism)
        print("Jamoa:", self.jamoa)
        print("Raqam:", self.raqam)


futbolchi = Futbolchi("Messi", "Inter Miami", 10)
futbolchi.malumot()

class Mahsulot:
    def __init__(self, nomi, narxi, soni):
        self.nomi = nomi
        self.narxi = narxi
        self.soni = soni

    def malumot(self):
        print("Mahsulot:", self.nomi)
        print("Narxi:", self.narxi)
        print("Soni:", self.soni)
        print("Umumiy:", self.narxi * self.soni)


mahsulot = Mahsulot("Olma", 10000, 5)
mahsulot.malumot()

class Bank:
    def __init__(self, ism, balans):
        self.ism = ism
        self.balans = balans

    def pul_qoshish(self, pul):
        self.balans += pul

    def malumot(self):
        print("Ism:", self.ism)
        print("Balans:", self.balans)


bank = Bank("Akbar", 50000)

bank.pul_qoshish(20000)

bank.malumot()