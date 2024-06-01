import sys


def modulKeresesiUtBeallitasa() -> None:
    """ """
    aktualis_file_utvonal_list: list = __file__.split("\\")
    n: int = len(aktualis_file_utvonal_list)
    sys.path.append("\\".join(aktualis_file_utvonal_list[0 : (n - 2)]))


modulKeresesiUtBeallitasa()


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


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
