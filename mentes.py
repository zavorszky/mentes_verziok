"""
File:       mentes.py
Feladat:    Mentés applikáció - Főprogram
Info:
    (1) A 'csv' csomag egy sorokból álló listát dolgoz fel.
    A sorokat szöveg file esetén (és a .csv file az) '\r',
    '\n' karakterek zárják. A 'csv' csomag 'csv.reader()'-e
    egy olyan reader példányt hoz létre, ami egy-egy beolvasott
    sorból egy-egy litát (list) készít. Ha még a reader példány
    létrehozása előtt 'next()'-el olvasunk a file-ból, akkor
    a file sor egy sztringben kerül átadásra a változónak.
    Figyelem! A '\r', '\n' karakterekkel együtt. Ha az így
    beolvasott sort is feldolgozzul le kell vágni a sorvégi
    '\r', '\n' karaktereket. Ld.: str_obj.rstrip()
    stackoverflow: How can I remove carriage return from a text file with Python?: https://stackoverflow.com/questions/17658055/how-can-i-remove-carriage-return-from-a-text-file-with-python
    valójában egy iterátorral dolgozza fel
     a megnyitott file-t. Itt a file sorai jelentik 
Fejlesztő:  zavorszky@yahoo.com
Létrehozás: 2024-05-08
"""

# Projekt: mentes
# Rövid leírás: Tömörített mentés készítése HD-ról PenDrive-ra.
# File:
# Feladat:      Főprogram
# Felhasználás:
#   > & python mentes.py
# Info:

# Készült:
# Szerző: zavorszky@yahoo.com

import os
import logging
import z9packages.z9seq.z9seq_mod as sm
import z9packages.z9log.z9log_mod as lm
import menteshiba_mod as mhm
import csv

PRG_VERZIO = "1.0"
PRG_NEV = "mentes.main"

OSERROR_ENOENT = 2
OSERROR_ENOENT_MESSAGE = "A file vagy a könyvtár nem létezik"

SEQ_NEV = "mentes_sorszam.cfg"
PRGLOGFILE_NEV = "mentes.log"

MENTESTABLAFILE_NEV = "mentestabla.csv"
ZIPTIPUS_ERVENYES = "ZIPFILE"


def naplozas_init() -> None:
    try:
        ms = sm.Sorszam(p_file_nev=SEQ_NEV)
    except Exception as e:
        raise mhm.H_Sorszam_KonfigOlvasasa(SEQ_NEV) from e

    sorszam: int = ms.kovetkezo()

    try:
        ms.valtozasMentes()
    except Exception as e:
        raise mhm.H_Sorszam_KonfigIrasa(SEQ_NEV) from e

    # oooo

    try:
        naplo = lm.Naplo(
            p_logger_name=__name__,
            p_logfile_name=PRGLOGFILE_NEV,
            p_sorszam=sorszam,
        )
    except Exception as e:
        raise mhm.H_Naplozas_Elokeszites(
            p_logger_name=__name__, p_file_nev=PRGLOGFILE_NEV, p_sorszam=sorszam
        ) from e
    return naplo


def mentes_konyvtarak(p_naplo: lm.Naplo, p_stat: dict):
    if not os.path.exists(MENTESTABLAFILE_NEV):
        raise FileNotFoundError(
            OSERROR_ENOENT, OSERROR_ENOENT_MESSAGE, MENTESTABLAFILE_NEV
        )

    try:
        with open(MENTESTABLAFILE_NEV) as f:
            # Első sor nem kell
            sor_kuka: str = next(f)
            # A második sor (A2, ebben van milyen zip parancsokat és kapcsolókat használ a file)
            ziptipus: str = ((next(f)).rstrip()).upper()
            if ziptipus != ZIPTIPUS_ERVENYES:
                raise mhm.H_ZIP_File_Cella(
                    p_file_nev=MENTESTABLAFILE_NEV,
                    p_hibas_cella="A2",
                    p_helyes_ertekek=ZIPTIPUS_ERVENYES,
                )
            # Fejlec nem kell
            sor_kuka = next(f)
            olvaso = csv.reader(f, dialect="excel", delimiter=";")
            i: int = 0
            for sor in olvaso:
                i += 1
                print("\t", i, sor)
                p_stat["darab_sikeres"] += 1
            p_stat
    except Exception as e:
        raise mhm.H_Egyeb(
            f"Hiba történt a '{MENTESTABLAFILE_NEV}' file beolvasásakor"
        ) from e


def main():
    try:
        print("A naplózás üzembehelyezése...")
        naplo = naplozas_init()
        print("\tSikeres")

        naplo.irInfo("")
        naplo.irInfo(f"{PRG_NEV} (v{PRG_VERZIO})")

        print(f"\nA mentés a '{MENTESTABLAFILE_NEV}' tábla alapján...")

        stat: dict = {"darab_sikeres": 0, "darab_sikertelen": 0}
        mentes_konyvtarak(p_naplo=naplo, p_stat=stat)

        print("\tMentés statisztika:")
        munka_str: str = (
            f"{stat['darab_sikeres'] + stat['darab_sikertelen']} összes mentés kisérlet [db]"
        )
        print("\t" + munka_str)
        naplo.irInfo(munka_str)

        munka_str = f"{stat['darab_sikeres']} sikeres mentés [db]"
        print("\t" + munka_str)
        naplo.irInfo(munka_str)

        munka_str = f"{stat['darab_sikertelen']} sikertelen mentés [db]"
        print("\t" + munka_str)
        naplo.irInfo(munka_str)

        print("\nLevél(email) küldés...")
        print("\tSikeres levél küldés")

        print("\nA program sikeresen befejeződött")
        naplo.irInfo("A program sikeresen befejeződött")

    except (
        mhm.H_Sorszam_KonfigOlvasasa,
        mhm.H_Sorszam_KonfigIrasa,
        mhm.H_Naplozas_Elokeszites,
    ) as h:
        print("\tHiba történt a program végrehajtása közben:")
        print(f"\t{mhm.hibauzenet(h)}")
        print(h.__traceback__)
    except Exception as h:
        print("\tHiba történt a program végrehajtása közben:")
        print(f"\t{mhm.hibauzenet(h)}")
        naplo.irErr(mhm.hibauzenet(h))


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

main()
