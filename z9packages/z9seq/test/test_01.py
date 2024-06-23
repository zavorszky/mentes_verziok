import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
print("\nMunka/aktuális könyvtár:", os.getcwd())

# *************************************


import z9seq_mod as seq

mentesSorszam = seq.Sorszam(p_file_nev="./z9packages/z9seq/test/mentes_sorszam.cfg")

print("")
print(mentesSorszam.kovetkezo())
print(mentesSorszam.kovetkezo())
print(mentesSorszam.sorszam)

mentesSorszam.valtozasMentes()
