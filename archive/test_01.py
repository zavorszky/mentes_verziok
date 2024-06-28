import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
print("\nMunka/aktuális könyvtár:", os.getcwd())


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

"""
File
    test_01.py
Feladat
    A 'z9hiba.z9hiba_mod' modul kipróbálása.
    A modul a 'Hiba' alaposztályt, és leszármazottait definiálja.
    Ezek az osztályok csak dokumentálják a hibákat/kivételeket,
    de nem kivételek!
Fejlesztő
    zavorszky@yahoo.com
Létrehozás
    2024-05-??
"""


import z9packages.z9hiba.z9hiba_mod as hm


print("** 0 **")
print(sys.path)


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
