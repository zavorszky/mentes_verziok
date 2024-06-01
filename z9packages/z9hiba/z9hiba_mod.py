"""
Csomag:     z9hiba
File:       z9hiba_mod
Fejlesztő:  zavorszky@yahoo.com
Létrehozás: 2024.05.xx
"""

"""
Vezérlő hiba osztályok.
Ezek nem kivételek, kivétel esetén ezekkel az osztályok
példányaival ADMINISZTRÁLJU a program kivételeket.
"""


class Hiba:
    def __init__(self, p_prg_nev):
        self.hiba_tipus = "ALTALANOS_HIBA"
        self.prg_nev = p_prg_nev
        self.hiba_kod = 0
        self.hiba_uzenet = ""
        self.hiba_kivetel = None

    def setPrgNev(self, p_prg_nev):
        self.prg_nev = p_prg_nev

    def getOsszetettHibauzenet(self):
        return f"{self.prg_nev}: [{self.hiba_tipus},{self.hiba_kod}] {self.hiba_uzenet}"
        # return f"{self.prg_nev}"


class NincsHiba(Hiba):
    def __init__(self, p_prg_nev):
        super().__init__(p_prg_nev)
        self.hiba_tipus = "NINCS_HIBA"
        self.hiba_uzenet = ""


class EgyebHiba(Hiba):
    def __init__(self, p_prg_nev, p_hiba_uzenet, p_hiba_kivetel):
        super().__init__(p_prg_nev)
        self.hiba_tipus = "EGYEB_HIBA"
        self.prg_nev = p_prg_nev
        self.hiba_kod = 1
        self.hiba_uzenet = p_hiba_uzenet
        self.hiba_kivetel = p_hiba_kivetel


class Hibak:
    def __init__(self):
        self.hibak = []

    def addHiba(self, p_hiba):
        self.hibak.append(p_hiba)

    def getUtolsoHiba(self):
        return self.hibak[-1]
