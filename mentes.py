"""
File:
    mentes.py
Feladat:
    Mentés applikáció - Főprogram
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
Fejlesztő:
    zavorszky@yahoo.com
Létrehozás:
    2024-05-08
"""

import os

# import logging
import z9packages.z9seq.z9seq_mod as sm
import z9packages.z9log.z9log_mod as lm
import z9packages.z9timer.z9timer_mod as tm
import menteshiba_mod as mhm
import csv
import zipfile

PRG_VERZIO = "1.0"
PRG_NEV = "mentes.main"

OSERROR_ENOENT = 2
OSERROR_ENOENT_MESSAGE = "A file vagy a könyvtár nem létezik"


def naplozas_init(p_logfile_nev: str) -> lm.Naplo:
    """
    Felkészülés a naplózásra:
    1) sorszám szakítás
    2) naplózási paraméterek beállítása
    """
    SEQ_NEV = "mentes_sorszam.cfg"
    # PRGLOGFILE_NEV =

    # Sorszám a naplózáshoz
    # ---------------------

    try:
        ms = sm.Sorszam(p_file_nev=SEQ_NEV)
    except Exception as e:
        raise mhm.H_Sorszam_KonfigOlvasasa(SEQ_NEV) from e

    sorszam: int = ms.kovetkezo()

    try:
        ms.valtozasMentes()
    except Exception as e:
        raise mhm.H_Sorszam_KonfigIrasa(SEQ_NEV) from e

    # A napló előkészítése
    # --------------------

    try:
        naplo = lm.Naplo(
            p_logger_name=__name__,
            p_logfile_name=p_logfile_nev,
            p_sorszam=sorszam,
        )
    except Exception as e:
        raise mhm.H_Naplozas_Elokeszites(
            p_logger_name=__name__, p_file_nev=p_logfile_nev, p_sorszam=sorszam
        ) from e
    return naplo


def file_utvonal_szabvanyositas(p_path: str) -> str:
    """
    A Win10 '\' elválasztójának cseréje Linux/UNIX stílusúra: '/'
    """
    return p_path if os.sep == "/" else p_path.replace("\\", "/")


def getForras_konyvtarak(p_konyvtar: str) -> list[str]:
    """
    A 'p_konyvtar'-ban lévő minden file TELJES elérési útvonalát
    tartalmazó listát készítő függvény.
    """
    file_paths: list[str] = []
    try:
        for root, directories, files in os.walk(p_konyvtar):
            for file_name in files:
                file_path = file_utvonal_szabvanyositas(os.path.join(root, file_name))
                file_paths.append(file_path)
        return file_paths
    except Exception as e:
        raise mhm.H_File_Paths(p_directory_nev=p_konyvtar) from e


def mentes_konyvtar(p_konyvtar: str, p_cel_archivum: str) -> None:
    """
    Egy megadott könyvtár és az összes alattalévő, file-ok mentése/tömörítése.
    Az alkönyvtára bekerülnek az archívumba.
    """
    # Elmegyünk a 'p_konyvtar'-ba, hogy ne kerüljön be a .zip-be
    # az esetleg nagyszámú, 'p_konyvtar'-ig vezető alkönyvtar az
    # archívumba.
    os.chdir(p_konyvtar)

    # Összegyűjtjük a mentendő/tömörítendő file-okat.
    forras_konyvtarak: list[str] = getForras_konyvtarak(p_konyvtar="./")

    # Mentünk, tömörítünk...
    try:
        with zipfile.ZipFile(
            file=p_cel_archivum, mode="w", compression=zipfile.ZIP_DEFLATED
        ) as zipf:
            for allomany in forras_konyvtarak:
                zipf.write(allomany)
    except Exception as e:
        raise mhm.H_ZIP_Egyeb(f"Hiba a  {p_cel_archivum} Sikertelen ") from e


def mentes_konyvtarak(p_mentestablafile_nev: str, p_stat: dict) -> None:
    """
    A 'p_mentestablafile_nev'-ben megadott .csv file-ban rögzített
    forrás könyvtárak mentése a szintén ott megadott archívumokba.
    A file szerkezete:
    -----------------
    A1:   megengedett:ZipFile
    A2:C2 Fejléc
    A3:A* Mentés jel; csal akkor történik feldolgozás, ha az értéke 'I'
    B3:B* A forrás könyvtár, ezt és az alkönyvtárait kell menteni.
    C3:C* A cél archívum.
    """
    ZIPTIPUS_ERVENYES: str = "ZIPFILE"
    CSV_MENTES_JEL: int = 0
    CSV_FORRAS_KONYVTAR: int = 1
    CSV_CEL_ARCHIVUM: int = 2

    p_stat["darab_sikeres"] = 0
    p_stat["darab_sikertelen"] = 0
    p_stat["darab_nem_mentett"] = 0

    if not os.path.exists(p_mentestablafile_nev):
        raise FileNotFoundError(
            OSERROR_ENOENT, OSERROR_ENOENT_MESSAGE, p_mentestablafile_nev
        )

    try:
        with open(p_mentestablafile_nev) as f:
            # Az első sor ('A1', ebben van milyen zip tipusú modul
            # dolgozik.
            ziptipus: str = ((next(f)).rstrip()).upper()
            if ziptipus != ZIPTIPUS_ERVENYES:
                raise mhm.H_CSV_File_Cella(
                    p_file_nev=p_mentestablafile_nev,
                    p_hibas_cella="A1",
                    p_helyes_ertekek=ZIPTIPUS_ERVENYES,
                )
            # Fejlec nem kell
            sor_kuka = next(f)
            #
            stopper = tm.Stopper()
            uzenet: str = ""
            olvaso = csv.reader(f, dialect="excel", delimiter=";")
            i: int = 0
            for sor in olvaso:
                i += 1
                mentes_jel: bool = (sor[CSV_MENTES_JEL]).upper() == "I"
                if mentes_jel:
                    stopper.nullazas()
                    try:
                        if vegrehajtas["tomorites"]:
                            stopper.inditas()
                            try:
                                mentes_konyvtar(
                                    sor[CSV_FORRAS_KONYVTAR], sor[CSV_CEL_ARCHIVUM]
                                )
                            except:
                                raise
                            finally:
                                stopper.megallitas()
                        p_stat["darab_sikeres"] += 1
                        uzenet = f"{i}. OK '{sor[CSV_FORRAS_KONYVTAR]}' {stopper.eltelt_ido_str()}"
                        print("\t" + uzenet)
                        naplo.irInfo(uzenet)
                    except Exception as e:
                        stopper.megallitas()
                        p_stat["darab_sikertelen"] += 1
                        uzenet = f"{i}. HIBA a '{sor[CSV_FORRAS_KONYVTAR]}' tömörítésekor {stopper.eltelt_ido_str()}"
                        print("\t" + uzenet)
                        print("\t" + mhm.hibauzenet(e))
                        naplo.irErr(uzenet)
                        naplo.irErr(":: " + mhm.hibauzenet(e))
                else:
                    p_stat["darab_nem_mentett"] += 1
                    uzenet = f"{i}. Nem mentett a '{sor[CSV_FORRAS_KONYVTAR]}' könyvtár"
                    print("\t" + uzenet)
                    naplo.irWarn(uzenet)
    except Exception as e:
        p_stat["darab_sikeres"] = None
        p_stat["darab_sikertelen"] = None
        p_stat["darab_nem_mentett"] = None
        raise mhm.H_Egyeb(
            f"Hiba történt a '{p_mentestablafile_nev}' file beolvasásakor"
        ) from e


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


def main(
    p_mentestablafile_nev: str = "mentestabla.csv", p_logfile_nev: str = "mentes.log"
) -> None:
    global naplo
    try:
        print("A naplózás üzembehelyezése...")
        naplo = naplozas_init(p_logfile_nev=p_logfile_nev)
        print("\tSikeres")
        naplo.irInfo("")
        naplo.irInfo(f"{PRG_NEV} (v{PRG_VERZIO})")

        try:
            print(f"\nA mentés a '{p_mentestablafile_nev}' tábla alapján...")

            stat: dict = {"darab_sikeres": 0, "darab_sikertelen": 0, "darab_nem_mentett": 0}
            mentes_konyvtarak(p_mentestablafile_nev=p_mentestablafile_nev, p_stat=stat)

            print("\tMentés statisztika:")
            uzenet: str = (
                f"{stat['darab_sikeres'] + stat['darab_sikertelen']} összes mentés kisérlet [db]"
            )
            print("\t" + uzenet)
            naplo.irInfo(uzenet)

            uzenet = f"{stat['darab_sikeres']} sikeres mentés [db]"
            print("\t" + uzenet)
            naplo.irInfo(uzenet)

            uzenet = f"{stat['darab_sikertelen']} sikertelen mentés [db]"
            print("\t" + uzenet)
            naplo.irInfo(uzenet)

            uzenet = f"{stat['darab_nem_mentett']} nem mentett [db]"
            print("\t" + uzenet)
            naplo.irInfo(uzenet)

            print("\nA program sikeresen befejeződött")
            naplo.irInfo("A program sikeresen befejeződött")
        except Exception as h:
            print("\tHiba történt a program végrehajtása közben:")
            print(f"\t{mhm.hibauzenet(h)}")
            naplo.irErr(mhm.hibauzenet(h))
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


global vegrehajtas

if __name__ == "__main__":
    vegrehajtas: dict = {"tomorites": True}
    main(p_mentestablafile_nev="mentestabla.csv", p_logfile_nev="mentes.log")
