# Info:
#   favtutor: How to Import File from Parent Directory in Python? (with code): https://favtutor.com/blogs/import-from-parent-directory-python


# A szülő modul könyvtár beillesztése a Python interpreter keresési sorába.
import os
import sys

sys.path.append(
    "h:\\DADY\\Rend\\temak\\mentes_240420_1454\\mentes_verziok\\z9packages\\z9hiba"
)

# Teszt


print(sys.path)


import z9hiba_mod as hm

print("** 0 **")
print(__file__)


print("\n** 1 **")
hiba = hm.NincsHiba(p_prg_nev="prgnev_1")
print(hiba)
print("prg_nev=", hiba.prg_nev)
print("hiba_kod=", hiba.hiba_kod)
print("hiba_uzenet=", hiba.hiba_uzenet)
print("getOsszetettHibauzenet", hiba.getOsszetettHibauzenet())

print("\n** 2 **")
hiba2 = hm.EgyebHiba(
    p_prg_nev="prgnev_2",
    p_hiba_uzenet="Egyéb 'a' hiba",
    p_hiba_kivetel=Exception("Komoly hiba"),
)

hibak2 = hm.Hibak()
hibak2.addHiba(p_hiba=hiba)
hibak2.addHiba(p_hiba=hiba2)
print(hibak2)
print(hibak2.hibak)
print(hibak2.getUtolsoHiba())
print(hibak2.getUtolsoHiba().getOsszetettHibauzenet())
