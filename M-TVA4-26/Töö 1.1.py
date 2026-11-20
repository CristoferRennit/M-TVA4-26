#1 Tervitus 
print("Tere Maailm!")

nimi = input("Mis on sinu nimi?: ")
vanus = int(input("Kui vana sa oled?: "))

print(f"Tere Maailm! Tervitan sind {nimi}! Sa oled {vanus} aastat vana.")

#2 Tüübid
vanus = 23
eesnimi = "Cristofer"
pikkus = 34.8
kas_käib_koolis = True

print(type(vanus))
print(type(eesnimi))
print(type(pikkus))
print(type(kas_käib_koolis))

#3 Kommid
from random import *
kommid = randint(1, 100)
print("Laual on", kommid, "kommi")
võta = int(input("Mitu kommi tahad?"))
kommid = kommid - võta
print("Laual on nüüd", kommid, "alles")

#4 Puu läbimõõt
ümbermõõt = float(input("Sisesta ümbermõõt: "))
pi = 3.14
läbimõõt = ümbermõõt / pi
print("Ringjoone läbimõõt on", läbimõõt)

#5 Diagonaal
pikkus = float(input("Sisesta pikkus: "))
laius = float(input("Sisesta laius: "))
diagonaal = (pikkus ** 2 + laius ** 2) ** 0.5
print("Diagonaal on", diagonaal)

#6 Vea otsing
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg #aeg / teepikkus ei ole õige, teepikkus / aeg on õige

print("Sinu kiirus oli " + str(kiirus) + " km/h")

#7 Aritmeetiline keskmine
arv1 = int(input("Sisesta esimene täisarv: "))
arv2 = int(input("Sisesta teine täisarv: "))
arv3 = int(input("Sisesta kolmas täisarv: "))
arv4 = int(input("Sisesta neljas täisarv: "))
arv5 = int(input("Sisesta viies täisarv: "))
summa = arv1 + arv2 + arv3 + arv4 + arv5
keskmine = summa / 5
jagaja = int(input("Sisesta jagaja: "))
täisosa = summa // jagaja
jääk = summa % jagaja
print("Summa on", summa)
print("Keskmine on", keskmine)
print("Täisosa on", täisosa)
print("Jääk on", jääk)

#8 Konn
print("  @..@")
print(" (----)")
print(" (\\__/)")
print('^^ "" ^^')

#9 Kolmnurga ümbermõõt
a = int(input("Sisesta esimene külg"))
b = int(input("Sisesta teine külg"))
c = int(input("Sisesta kolmas külg"))
ümbermõõt = a + b + c
print("kolmnurga ümbermõõt on", ümbermõõt)

#10 Pitsa
pitsa_hind = 12.90
jootraha = 0.1 * pitsa_hind
kokku = pitsa_hind + jootraha
inimeste_arv = int(input("Mitu inimest kokku on? "))
ühe_inimese_arve = kokku / inimeste_arv
print("Igaüks peab maksma", round(ühe_inimese_arve, 2), "€")

#11 Vigade käsitlemine
#7 Aritmeetiline keskmine veakontroll
try:
    arv1 = int(input("Sisesta esimene täisarv: "))
    arv2 = int(input("Sisesta teine täisarv: "))
    arv3 = int(input("Sisesta kolmas täisarv: "))
    arv4 = int(input("Sisesta neljas täisarv: "))
    arv5 = int(input("Sisesta viies täisarv: "))
    summa = arv1 + arv2 + arv3 + arv4 + arv5
    keskmine = summa / 5
    print("Summa on", summa)
    print("Keskmine on", keskmine)
    jagaja = int(input("Sisesta jagaja: "))
    täisosa = summa // jagaja
    jääk = summa % jagaja
    print("Täisosa on", täisosa)
    print("Jääk on", jääk)
except ValueError:
    print("Viga! Palun sisesta täisarv.")
except ZeroDivisionError:
    print("Viga! Nulliga ei saa jagada.")


#10 Pitsa veakontroll
pitsa_hind = 12.90
jootraha = 0.1 * pitsa_hind
kokku = pitsa_hind + jootraha
try:
    inimeste_arv = int(input("Mitu inimest kokku on? "))
    ühe_inimese_arve = kokku / inimeste_arv
    print("Igaüks peab maksma", round(ühe_inimese_arve, 2), "€")
except ValueError:
    print("Viga! Palun sisesta täisarv.")
except ZeroDivisionError:
    print("Viga! Inimeste arv ei saa olla null.")
