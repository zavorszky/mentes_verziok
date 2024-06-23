"""
File
    menteskonyvtarak_mod.py
Feladat
    Adott a 'mentestabla.csv' file, ami tarttalmazza a mentendő
    könyvtárakat (elérési útvonallal) és a hozzájuk tartozó cél
    archívumokat (elérési útvonal + zip file név). A .csv file-t
    a 'mentes_konyvtarak' függvény kezeli. Ez hívja egy-egy [forrás
    könyvtár + cél archívum] párral a 'mentes_konyvtar' függvényt.
    Ez utóbbi végzi a mentést/tömörítést. 
Fejlesztő
    zavorszky@yahoo.com
Létrehozás
    2024.05.xx
"""

import os
import csv
import zipfile
import z9packages.z9timer.z9timer_mod as tm
import menteshiba_mod as mhm
import mentesglogal_mod as mgm


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
    A3:A  Mentés jel; csal akkor történik feldolgozás, ha az értéke 'I'
    B3:B  A forrás könyvtár, ezt és az alkönyvtárait kell menteni.
    C3:C  A cél archívum.
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
            mgm.OSERROR_ENOENT, mgm.OSERROR_ENOENT_MESSAGE, p_mentestablafile_nev
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
                        if mgm.vegrehajtas["tomorites"]:
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
                        mgm.naplo.irInfo(uzenet)
                    except Exception as e:
                        stopper.megallitas()
                        p_stat["darab_sikertelen"] += 1
                        uzenet = f"{i}. HIBA a '{sor[CSV_FORRAS_KONYVTAR]}' tömörítésekor {stopper.eltelt_ido_str()}"
                        print("\t" + uzenet)
                        print("\t" + mhm.hibauzenet(e))
                        mgm.naplo.irErr(uzenet)
                        mgm.naplo.irErr(":: " + mhm.hibauzenet(e))
                else:
                    p_stat["darab_nem_mentett"] += 1
                    uzenet = f"{i}. Nem mentett a '{sor[CSV_FORRAS_KONYVTAR]}' könyvtár"
                    print("\t" + uzenet)
                    mgm.naplo.irWarn(uzenet)
    except Exception as e:
        p_stat["darab_sikeres"] = None
        p_stat["darab_sikertelen"] = None
        p_stat["darab_nem_mentett"] = None
        raise mhm.H_Egyeb(
            f"Hiba történt a '{p_mentestablafile_nev}' file beolvasásakor"
        ) from e
