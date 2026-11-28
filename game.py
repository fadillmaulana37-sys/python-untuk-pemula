import random

angka_rahasia = random.randint(1, 10)
print("Kuring mikir angka 1 nepi ka 10!")

while True:
    tebakan = int(input("Tebakan maneh: "))

    if tebakan == angka_rahasia:
        print("BENERRR! Maneh hebat!")
        break
    elif tebakan > angka_rahasia:
        print("Kagedean! Coba leuwih leutik")
    else:
        print("Kaleutikan! Coba leuwih gede")