import sys


def modulokEleresenekBeallitasa():
    aktualis_file_utvonal_list = __file__.split("\\")
    n = len(aktualis_file_utvonal_list)
    sys.path.append("\\".join(aktualis_file_utvonal_list[0 : (n - 4)]))


modulokEleresenekBeallitasa()

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

import z9packages.z9seq.z9seq_mod as seq

mentesSorszam = seq.Sorszam(p_file_nev="mentes_sorszam.cfg")
print(mentesSorszam.kovetkezo())
print(mentesSorszam.kovetkezo())
print(mentesSorszam.sorszam)
mentesSorszam.valtozasMentes()
