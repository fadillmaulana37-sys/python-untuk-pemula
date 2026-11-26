class Kucing:
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna

    def sapa(self):
        print("Meow! Ngaran kuring", self.nama, "warna kuring", self.warna)

# Ngadamel 2 kucing tina 1 cetakan
kucing1 = Kucing("Oyen", "oren")
kucing2 = Kucing("Moli", "hideung")

kucing1.sapa()
kucing2.sapa()