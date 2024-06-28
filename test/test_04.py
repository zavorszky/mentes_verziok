"""
File
    test_04.py
Feladat
    A 'menteshiba_mod' modul kipróbálása: Milyen információ
    telenik meg a 'FileNotFoundError' kivételnél.
    repr() vs. str()
Fejlesztő
    zavorszky@yahoo.com
Létrehozás
    2024-05-??
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
print("\nMunka/aktuális könyvtár:", os.getcwd())


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

import menteshiba_mod as mhm

e1 = FileNotFoundError(2, "Hiányzó file", "abrakadabra.txt")
e2 = mhm.H_Egyeb("Valami hiba")

print(e1)

try:
    raise e1
except Exception as ea:
    try:
        print('*1*', ea)
        print('*1*', repr(ea))
        print('*1*', str(ea))
        raise e2 from ea
    except Exception as eb:
        print(mhm.hibauzenet(eb))
        print('*', eb)
        print(repr(eb))
        print(repr(eb.__context__))
        print(repr(eb.__cause__))
        print(repr(eb.__suppress_context__))
