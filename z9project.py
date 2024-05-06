# File: z9project.py
# Code type: module
# Description: Project feladatok/dokumentáció készítés támogatása.
# Use: $ python -c 'import z9project; z9import.prgFile_gen()'
# Info:
#   1) stackowerflow: Run function from the command line: https://stackoverflow.com/questions/3987041/run-function-from-the-command-line
#   2) stackowerflow: How do I create a constant in Python?: https://stackoverflow.com/questions/2682745/how-do-i-create-a-constant-in-python
#   3) GeeksforGeeks:Read JSON file using Python: https://www.geeksforgeeks.org/read-json-file-using-python/
# Importok: re (RegExp)
# Created: 2024-05-05
# Author: zavorszky@yahoo.com

import re
import datetime
import json

# Konstansok
# (A Pyton-ban nincs nyelvi eszköz konstansok definiálására.
#  A csupa nagybetű névkonvenciót használják figyelmeztetésül,
#  hogy a változó konstansnak van tervezve, ezért ne adjunk értéket neki.

F_NEV_MASZK = "^[a-zA-Z]([a-zA-Z]|[0-9])*$"
AKT_DATUM = datetime.datetime.now()


def file_gen():
    ftipus_kod = ""  # File tipus kód
    ftipus = ""  # File tipus
    fnev = ""  # File név
    teljes_fnev = ""  # Teljes file név
    pktipus_kod = ""
    pktipus = ""
    fejsorok = []
    prjnev = ""
    prjszerzo = ""
    try:
        print("\nProject feladatok/dokumentáció készítés támogatása.")
        print("--------------------")

        print("\tProject adatok beolvasása...")
        f = open("z9project.json")
        projektadatok = json.load(f)
        prjnev = projektadatok["nev"]
        prjszerzo = projektadatok["file_fej_informaciok"]["szerzo"]["email"]
        f.close()
        print(f"\tProjekt név: {prjnev}")
        print(f"\tSzerző email: {prjszerzo}")

        #
        print("\nMilyen file-t kell készíteni?")
        print("\tÉrvényes file tipus kódok: 1=(.py).")
        ftipus_kod = input("\tVálasztás: ")
        while True:
            if ftipus_kod == "":
                raise RuntimeError("Info: Nincs megadva File Type kód.")
            if ftipus_kod == "1":
                ftipus = "py"
                break
            else:
                raise RuntimeError(
                    f"Hiba: Nem megfelelő a file tipus kód: [{ftipus_kod}]."
                )
        #
        print("\nMi legyen a file neve?")
        print(f"\tA file névnek illeszkednie kell a [{F_NEV_MASZK}]-ra.")
        fnev = input("\tFile név: ")
        while True:
            if fnev == "":
                raise RuntimeError("Info: Nincs megadva File név.")
            if re.search(F_NEV_MASZK, fnev):
                break
            else:
                raise RuntimeError(
                    f"Hiba: A [{fnev}] nem illeszkedik a [{F_NEV_MASZK}] maszkra."
                )
        #
        print("\nMilyen típusú programkód kerül a file-ba?")
        print("\tÉrvényes programkódtípus kódok: 1=(Python app), 2=(Python module).")
        pktipus_kod = input("\tVálasztás: ")
        while True:
            if pktipus_kod == "":
                raise RuntimeError("Info: Nincs megadva a programkódtípus kód.")
            if pktipus_kod == "1":
                pktipus = "Python app"
                break
            if pktipus_kod == "2":
                pktipus = "Python module"
                break
            else:
                raise RuntimeError(
                    f"Hiba: Nem megfeleló programkódtípus kód: [{pktipus_kod}]."
                )
        #
        teljes_fnev = fnev + "." + ftipus

        #
        fejsorok.append("# Project: " + prjnev)
        fejsorok.append("# File: " + teljes_fnev)
        fejsorok.append("# Code type: " + pktipus)
        fejsorok.append("# Created: " + AKT_DATUM.strftime("%Y-%m-%d"))
        fejsorok.append("# Author: " + prjszerzo)

        #
        for sor in fejsorok:
            print(sor)

        print("Kész.")
    except RuntimeError as e:
        print(e)
