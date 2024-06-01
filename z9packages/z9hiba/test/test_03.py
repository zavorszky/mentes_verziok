import sys


aktualis_file_utvonal_list = __file__.split("\\")
n = len(aktualis_file_utvonal_list)
print(aktualis_file_utvonal_list[0 : (n - 4)])
sys.path.append("\\".join(aktualis_file_utvonal_list[0 : (n - 4)]))

import z9packages.z9hiba.z9hiba_mod as hm

hibak = hm.Hibak()
hibak.addHiba(
    hm.EgyebHiba(
        p_prg_nev="teszt_prg",
        p_hiba_uzenet="Program hiba történt (tesztelés)",
        p_hiba_kivetel=Exception("Helló!"),
    )
)
