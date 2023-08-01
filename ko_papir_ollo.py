from random import randint

print(
    'Üdvözölek!\n'
    'Ez egy kő, papír, olló játék.\n'
    'Add meg a választott eszközt, vagy a játékból való kilépéshez írd be: "vége"')

kpo = ["kő", "papír", "olló"]
gep = kpo[randint(0, 2)]
jatekos = False

while jatekos is False:

    # itt "jatekos" True értéket kap
    jatekos = input("kő, papír, olló? ")
    if jatekos == gep:
        print("Döntetlen, az ellenfeled választása: \"" + gep + "\"")
    elif jatekos == "kő":
        if gep == "papír":
            print("Vesztettél, az ellenfeled választása: \"" + gep + "\"")
        else:
            print("Nyertél, az ellenfeled választása: \"" + gep + "\"")
    elif jatekos == "papír":
        if gep == "olló":
            print("Vesztettél, az ellenfeled választása: \"" + gep + "\"")
        else:
            print("Nyertél, az ellenfeled választása: \"" + gep + "\"")
    elif jatekos == "olló":
        if gep == "kő":
            print("Vesztettél, az ellenfeled választása: \"" + gep + "\"")
        else:
            print("Nyertél, az ellenfeled választása: \"" + gep + "\"")

# kilépési lehetőség
    elif jatekos == "vége":
        break
    else:
        print("Nem megfelelő szót adtál meg! (kő, papír, olló)")

# visszaállítja a "jatekos" értékét False-ra, hogy folytatódjon a loop, és ad egy új értéket a "gep"-nek
    jatekos = False
    gep = kpo[randint(0, 2)]
