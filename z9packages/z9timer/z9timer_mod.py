"""
File
    z9timer_mod.py
Feladat
    Mentés applikáció - Főprogram
Info
    stacoverflow: How to format elapsed time from seconds to hours, minutes, seconds and milliseconds in Python?: https://stackoverflow.com/questions/27779677/how-to-format-elapsed-time-from-seconds-to-hours-minutes-seconds-and-milliseco
    Python documentation: time - Time access and conversions: https://docs.python.org/3/library/time.html
Fejlesztő
    zavorszky@yahoo.com
Létrehozás
    2024-06-18
"""

import time


class Stopper:
    def __init__(self) -> None:
        self.ido_inditas: float = 0
        self.ido_megallitas: float = 0
        self.ido_eltelt: float = 0

    def nullazas(self) -> None:
        self.ido_inditas = 0
        self.ido_megallitas = 0
        self.ido_eltelt = 0

    def inditas(self) -> None:
        # time.time() : éjfél óta eltelt idő [másodperc] ([mp])
        self.ido_inditas = time.time()
        self.ido_megallitas = self.ido_inditas

    def megallitas(self) -> None:
        self.ido_megallitas = time.time()
        self.ido_eltelt = self.ido_megallitas - self.ido_inditas

    def eltelt_ido_masodperc(self) -> int:
        return self.ido_eltelt

    def eltelt_ido_str(self) -> str:
        ora, maradek = divmod(self.ido_eltelt, 3600)
        perc, masodperc = divmod(maradek, 60)
        return "{:0>2}:{:0>2}:{:05.2f}".format(int(ora), int(perc), masodperc)
        # return "{:0>2} óra {:0>2} perc {:05.2f} másodperc".format(int(ora), int(perc), masodperc)
