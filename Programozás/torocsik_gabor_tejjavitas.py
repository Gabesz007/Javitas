# 1) Feladat – Írjon programot, amely megvizsgálja három tehenészeti telephely egy
# hónapos tejhozamát és eldönti, hogy kell -e a hozam növelése érdekében több tehenet
# vásárolni.
# Törőcsik Gábor 2023.01.17.

print("Törőcsik Gábor 2023.01.17.\nEz a program megvizsgálja három tehenészeti telephely egy hónapos tejhozamát és eldönti, hogy kell -e a hozam növelése érdekében több tehenet vásárolni.\nTehenet, csak akkor kell vásárolni, ha a hozam 500 liter tejhozam átlag alatt van.")

honap1 = 452.35
honap2 = 628,45
honap3 = 553

def atlag(honap1, honap2, honap3):
    hozam = round((honap1 + honap2 + honap3)/3)
    
    if (hozam < 500):
        print(f"Az átlag tejhozam: {hozam} liter, tehenet kell vásárolni.")
    else:
        print(f"Az átlag tejhozam: {hozam} liter, nem kell tehenet vásárolni.")
        
atlag(honap1, honap2, honap3)        
