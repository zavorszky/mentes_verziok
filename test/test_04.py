import sys

def modulKeresesiUtBeallitasa() -> None:
    aktualis_file_utvonal_list: list = __file__.split("\\")
    n: int = len(aktualis_file_utvonal_list)
    sys.path.append("\\".join(aktualis_file_utvonal_list[0 : (n - 2)]))


modulKeresesiUtBeallitasa()

import menteshiba_mod as mhm

e1 = FileNotFoundError(2, "Hiányzó file", "abrakadabra.txt")
e2 = mhm.H_Egyeb("Valami hiba")

try:
    raise e1
except Exception as ea:
    try:
        raise e2 from ea
    except Exception as eb:
        print(mhm.hibauzenet(eb))
        print(repr(eb))
        print(repr(eb.__context__))
        print(repr(eb.__cause__))
        print(repr(eb.__suppress_context__))