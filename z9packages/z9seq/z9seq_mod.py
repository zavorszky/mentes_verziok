"""
Csomag
    z9seq
File
    z9seq_mod
Info:
  A projekt könyvtárban kell lennie egy konfig file-nak,
  a következő tartalommal:
    [Sorszam]
    kovetkezo = n
  ahonnan az 'n' egész számot olvassa be a Python a Sorszam
  osztály példányosításakor.
Fejlesztő
    zavorszky@yahoo.com
Létrehozás
    2024.05.xx
"""

import os
import configparser


OSERROR_ENOENT = 2
OSERROR_ENOENT_MESSAGE = "A file vagy a könyvtár nem létezik"


class Sorszam:
    def __init__(self, p_file_nev: str) -> None:
        if not os.path.exists(p_file_nev):
            raise FileNotFoundError(OSERROR_ENOENT, OSERROR_ENOENT_MESSAGE, p_file_nev)
        self.file_nev = p_file_nev
        self.config = configparser.ConfigParser()
        self.config.read(p_file_nev)
        self.sorszam = self.config.getint("Sorszam", "kovetkezo")

    def kovetkezo(self) -> int:
        i: int = self.sorszam
        self.sorszam += 1
        return i

    def valtozasMentes(self) -> None:
        # A következő sorszám meírása a configuration registry-be.
        self.config.set("Sorszam", "kovetkezo", str(self.sorszam))
        # A configuration registry mentése.
        try:
            f = open(self.file_nev, "w")
        except Exception as e:
            raise OSError(f"Nem sikerült a '{self.file_nev}' file-t megnyini: {e}")
        # Írás, zárás
        try:
            self.config.write(f)
        except Exception as e:
            raise OSError(f"Hiba a '{self.file_nev}' file-t írásakor: {e}")
        finally:
            f.close()
