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

import z9packages.z9log.z9log_mod as lm
import mentesglogal_mod as mgm
import menteshiba_mod as mhm
import mentesnaplo_mod as mnm
import meneteskonyvtarak_mod as mkm


PRG_VERZIO = "1.0"
PRG_NEV = "mentes"


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


def main(
    p_mentestablafile_nev: str = "mentestabla.csv", p_logfile_nev: str = "mentes.log"
) -> None:
    global naplo
    try:
        print(f"{PRG_NEV} v{PRG_VERZIO}")
        print("A naplózás üzembehelyezése...")
        mgm.naplo = mnm.naplozas_init(p_logfile_nev=p_logfile_nev)
        print("\tSikeres")
        mgm.naplo.irInfo("")
        mgm.naplo.irInfo(f"{PRG_NEV} (v{PRG_VERZIO})")

        try:
            print(f"\nA mentés a '{p_mentestablafile_nev}' tábla alapján...")

            stat: dict = {
                "darab_sikeres": 0,
                "darab_sikertelen": 0,
                "darab_nem_mentett": 0,
            }
            mkm.mentes_konyvtarak(
                p_mentestablafile_nev=p_mentestablafile_nev, p_stat=stat
            )

            print("\tMentés statisztika:")

            uzenet: str = f"{stat['darab_sikeres']} sikeres mentés [db]"
            print("\t" + uzenet)
            mgm.naplo.irInfo(uzenet)

            uzenet = f"{stat['darab_sikertelen']} sikertelen mentés [db]"
            print("\t" + uzenet)
            mgm.naplo.irInfo(uzenet)

            uzenet = f"{stat['darab_nem_mentett']} nem mentett [db]"
            print("\t" + uzenet)
            mgm.naplo.irInfo(uzenet)

            print("\nA program sikeresen befejeződött\n")
            mgm.naplo.irInfo("A program sikeresen befejeződött")
        except Exception as h:
            print("\tHiba történt a program végrehajtása közben:")
            print(f"\t{mhm.hibauzenet(h)}")
            mgm.naplo.irErr(mhm.hibauzenet(h))
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
        mgm.naplo.irErr(mhm.hibauzenet(h))


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


if __name__ == "__main__":
    global vegrehajtas
    vegrehajtas = {"tomorites": True}
    main(p_mentestablafile_nev="mentestabla.csv", p_logfile_nev="mentes.log")
