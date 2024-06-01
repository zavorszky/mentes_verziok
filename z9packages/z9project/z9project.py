# File: z9project.py
# Code type: Python application
# Description: Project feladatok és dokumentáció készítés támogatása.
# Use:
#   > & python z9project.py
# Info:
#   * GeeksforGeeks: Read JSON file using Python: https://www.geeksforgeeks.org/read-json-file-using-python/
#   * GeeksforGeeks: User-defined Exceptions in Python with Examples: https://www.geeksforgeeks.org/user-defined-exceptions-python-examples/
#   * Medium: 5 Best Practices for Python Exception Handling: https://medium.com/@saadjamilakhtar/5-best-practices-for-python-exception-handling-5e54b876a20
#   * python: Handling Exceptions: https://wiki.python.org/moin/HandlingExceptions
#   * Real Python: What Does if __name__ == "__main__" Do in Python?: https://realpython.com/if-name-main-python/
#   * Rollbar: How to Catch Multiple Exceptions in Python: https://rollbar.com/blog/python-catching-multiple-exceptions/
#   * stackowerflow: How do I create a constant in Python?: https://stackoverflow.com/questions/2682745/how-do-i-create-a-constant-in-python
#   * stackowerflow: Run function from the command line: https://stackoverflow.com/questions/3987041/run-function-from-the-command-line
#   * stackowerflow: Unicode (UTF-8) reading and writing to files in Python: https://stackoverflow.com/questions/491921/unicode-utf-8-reading-and-writing-to-files-in-python
# Created: 2024-05-05
# Author: zavorszky@yahoo.com

import re
import datetime
import json
import sys

# Konstansok
# (A Pyton-ban nincs nyelvi eszköz konstansok definiálására.
#  A csupa nagybetű névkonvenciót használják figyelmeztetésül,
#  hogy a változó konstansnak van tervezve, ezért ne adjunk értéket neki.

# Konstansok
F_NEV_MASZK = "^[a-zA-Z]([a-zA-Z]|[0-9]|[_])*$"
AKT_DATUM = datetime.datetime.now()
PRJFILE_ENCODING = "utf-8"
PRJFILE_NEV = "z9project.json"
TELJES_FNEV_ENCODING = "utf-8"


# Osztályok
class AltalanosKivetel(Exception):
    pass


class HianyzoErtek(AltalanosKivetel):
    def __init__(self, uzenet_tipus, uzenet):
        self.msg = f"[{uzenet_tipus}] Hiányzó {uzenet} érték."


class HibasErtek(AltalanosKivetel):
    def __init__(self, uzenet_tipus, uzenet, ertek):
        self.msg = f"[{uzenet_tipus}] Hibás {uzenet} érték: {ertek}."


class HibasFileNev(AltalanosKivetel):
    def __init__(self, uzenet_tipus, fnev, fmaszk):
        self.msg = f"[{uzenet_tipus}] Az [{fnev}] nem illeszkedik az [{fmaszk}]-ra."


class EgyebHiba(AltalanosKivetel):
    def __init__(self, uzenet_tipus, uzenet):
        self.msg = f"[{uzenet_tipus}] Egyéb hiba: {uzenet}."


def file_gen():
    ftipus_kod = ""  # File tipus kód
    ftipus = ""  # File tipus
    fnev = ""  # File név
    fnev_postfix = ""
    teljes_fnev = ""  # Teljes file név
    pktipus_kod = ""  # Programkódtipus kód
    pktipus = ""  # Programkódtipus kód
    fejsorok = []  # Fejsorok
    prjnev = ""  # Projektnév
    prjleiras = ""  # Projekt rövid leírás
    prjszerzo = ""  # Project szerző
    try:
        print("\nProject feladatok/dokumentáció készítés támogatása.")
        print("--------------------")

        print("\tProject adatok beolvasása...")
        try:
            f = open(PRJFILE_NEV, encoding=PRJFILE_ENCODING)

            try:
                projektadatok = json.load(f)
                prjnev = projektadatok["nev"]
                prjleiras = projektadatok["rovid_leiras"]
                prjszerzo = projektadatok["file_fej_informaciok"]["szerzo"]["email"]
            except Exception as e:
                raise EgyebHiba("H", f"Probléma a {PRJFILE_NEV} beovasásánál: {e}.")
            finally:
                f.close()
        except Exception as e:
            raise EgyebHiba("H", f"Probléma a {PRJFILE_NEV} file megnyitásánál: {e}.")

        print(f"\tProjekt név: {prjnev}")
        print(f"\tProjekt rövid leírás: {prjleiras}")
        print(f"\tSzerző email: {prjszerzo}")

        #
        print("\nMilyen file-t kell készíteni?")
        print("\tÉrvényes file tipus kódok: 1=(.py).")
        ftipus_kod = input("\tVálasztás: ")
        if ftipus_kod == "":
            raise HianyzoErtek("I", "ftipus_kod")
        if ftipus_kod == "1":
            ftipus = "py"
        else:
            raise HibasErtek("H", "ftipus_kod", ftipus_kod)
        #
        print("\nMi legyen a file neve?")
        print(f"\tA file névnek illeszkednie kell a [{F_NEV_MASZK}]-ra.")
        fnev = input("\tFile név: ")
        if fnev == "":
            raise HianyzoErtek("I", "fnev")
        if re.search(F_NEV_MASZK, fnev):
            pass
        else:
            raise HibasFileNev("H", fnev, F_NEV_MASZK)
        #
        print("\nMilyen típusú programkód kerül a file-ba?")
        print(
            "\tÉrvényes programkódtípus kódok: 1=(Python app), 2=(Python module), 3=(Python test)."
        )
        pktipus_kod = input("\tVálasztás: ")
        if pktipus_kod == "":
            raise HianyzoErtek("I", "pktipus_kod")
        if pktipus_kod == "1":
            pktipus = "Python app"
            fnev_postfix = ""
        elif pktipus_kod == "2":
            pktipus = "Python module"
            fnev_postfix = "_mod"
        elif pktipus_kod == "3":
            pktipus = "Python test"
            fnev_postfix = "_test"
        else:
            raise HibasErtek("H", "pktipus_kod")
        #
        teljes_fnev = fnev + fnev_postfix + "." + ftipus

        #
        fejsorok.append("# Projekt: " + prjnev)
        fejsorok.append("# Rövid leírás: " + prjleiras)
        fejsorok.append("# File: " + teljes_fnev)
        fejsorok.append("# Programkód tipus: " + pktipus)
        fejsorok.append("# Feladat: ...")
        fejsorok.append("# Felhasználás:")
        fejsorok.append("#   ...")
        fejsorok.append("# Info:")
        fejsorok.append("#   ...")
        fejsorok.append("# Készült: " + AKT_DATUM.strftime("%Y-%m-%d"))
        fejsorok.append("# Szerző: " + prjszerzo)
        fejsorok.append("#   ...")
        fejsorok.append("# importok")
        fejsorok.append("#  -------")
        fejsorok.append("#   ...")
        fejsorok.append("# Konstansok")
        fejsorok.append("# ----------")
        fejsorok.append("#   ...")
        fejsorok.append("# Függvények")
        fejsorok.append("#   ...")
        fejsorok.append("#  %%%%%%%%%%%%%%%%%%%%")
        fejsorok.append("#   ...")

        #
        for sor in fejsorok:
            print(sor)

        #
        try:
            f = open(teljes_fnev, "x", encoding=TELJES_FNEV_ENCODING)
            for fejsor in fejsorok:
                f.write(fejsor + "\n")
        except Exception as e:
            raise EgyebHiba("H", f"Probléma a {teljes_fnev} létrehozásánál: {str(e)}.")
        finally:
            f.close()

        print("\nKész.")
    except Exception as e:
        print("\nFIGYELEM!")
        print("Probléma volt a végrehajtás közben.")
        print(e.msg)


if __name__ == "__main__":
    file_gen()
