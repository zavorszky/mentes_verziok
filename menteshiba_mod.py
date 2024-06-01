"""
File:       menteshiba_mod.py
Feladat:    Mentés applikáció hibái.
Fejlesztő:  zavorszky@yahoo.com
Létrehozás: 2024.05.xx
"""


class Hiba(Exception):
    pass


class H_Sorszam_KonfigOlvasasa(Hiba):
    def __init__(self, p_file_nev: str) -> None:
        self.file_name = p_file_nev
        self.message = f"Nem sikerült a sorszám beolvasása a '{self.file_name}'-ból"
        super().__init__(self.message)


class H_Sorszam_KonfigIrasa(Hiba):
    def __init__(self, p_file_nev: str) -> None:
        self.file_name = p_file_nev
        self.message = f"Nem sikerült a sorszám kiírása a '{self.file_name}'-ba"
        super().__init__(self.message)


class H_Naplozas_Elokeszites(Hiba):
    def __init__(self, p_logger_name: str, p_file_nev: str, p_sorszam: int) -> None:
        self.logger_name = p_logger_name
        self.file_nev = p_file_nev
        self.sorszam = p_sorszam
        self.message = "Nem sikerült a naplózás előkészítése. Paraméterek: {p_logger_name}, {p_file_nev}, {p_sorszam}"
        super().__init__(self.message)


class H_File_Kereses(Hiba):
    def __init__(self, p_file_nev: str) -> None:
        self.file_neve = p_file_nev
        self.message = f"Nem található a '{self.file_neve}'-ba"
        super().__init__(self.message)


class H_Egyeb(Hiba):
    def __init__(self, p_message: str) -> None:
        self.message = p_message
        super().__init__(self.message)

def hibauzenet(p_kivetel: Exception) -> str:
    huzenet: str = repr(p_kivetel)
    if p_kivetel.__context__ == None:
        return huzenet
    else:
        huzenet = huzenet + " | " + hibauzenet(p_kivetel.__context__)
        return huzenet


