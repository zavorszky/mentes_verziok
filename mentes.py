# Projekt: mentes
# Rövid leírás: Tömörített mentés készítése HD-ról PenDrive-ra.
# File:         mentes.py
# Feladat:      Főprogram
# Felhasználás:
#   > & python mentes.py
# Készült: 2024-05-08
# Szerző: zavorszky@yahoo.com

import os
import logging
import z9packages.z9seq.z9seq_mod as sm
import z9packages.z9log.z9log_mod as lm
import menteshiba_mod as mhm
import csv

OSERROR_ENOENT = 2
OSERROR_ENOENT_MESSAGE = "A file vagy a könyvtár nem létezik"

PRG_VERZIO = "1.0"
PRG_NEV = "mentes.main"
PRGLOGFILE_NEV = "mentes.log"
SEQ_NEV = "mentes_sorszam.cfg"

MENTESTABLAFILE_NEV = "mentestabla.csv"


def main():
    try:
        print(f"A szekvencia ({SEQ_NEV}) üzembehelyezése...")
        try:
            ms = sm.Sorszam(p_file_nev=SEQ_NEV)
        except Exception as e:
            raise mhm.H_Sorszam_KonfigOlvasasa(SEQ_NEV) from e

        sorszam: int = ms.kovetkezo()

        try:
            ms.valtozasMentes()
        except Exception as e:
            raise mhm.H_Sorszam_KonfigIrasa(SEQ_NEV) from e

        print("\tSikeres")

        print("A naplózás üzembehelyezése...")
        try:
            naplo: lm.Naplo = lm.Naplo(
                p_logger_name=__name__,
                p_logfile_name=PRGLOGFILE_NEV,
                p_sorszam=sorszam,
            )
        except Exception as e:
            raise mhm.H_Naplozas_Elokeszites(
                p_logger_name=__name__, p_file_nev=PRGLOGFILE_NEV, p_sorszam=sorszam
            ) from e

        print("\tSikeres")

        naplo.irInfo("")
        naplo.irInfo(f"{PRG_NEV} (v{PRG_VERZIO})")

        print(f"A mentés a '{MENTESTABLAFILE_NEV}' tábla alapján...")

        if not os.path.exists(MENTESTABLAFILE_NEV):
            raise FileNotFoundError(
                OSERROR_ENOENT, OSERROR_ENOENT_MESSAGE, MENTESTABLAFILE_NEV
            )

        try:
            with open(MENTESTABLAFILE_NEV) as f:
                fejsor = next(f)
                olvaso = csv.reader(f, dialect="excel",delimiter=";")
                for sor in olvaso:
                    print(sor)
        except Exception as e:
            raise mhm.H_Egyeb(
                f"Hiba történt a '{MENTESTABLAFILE_NEV}' file beolvasásakor"
            ) from e

        print("\tSikeres a mentés")

        print("Levél(email) küldés...")
        print("\tSikeres levél küldés")

        print("A program sikeresen befejeződött")
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
