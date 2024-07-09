# Mentés

## Feladat

Adott egy PC egy belső Winchesterrel és egy külsővel.\
A külsőn személyes adato is vannak és vannak nem személyes adatok is.\
A fenti két típusú adatokat meteni szeretném.

Az érzékeny adatokat egy PenDrive-ra,\
a fontos de nem érzékenyek egy részét szintén PenDrive-ra,\
másik részét Google Drive-ra szeretném menteni.

## Megoldás

Valamilyen szkript nyelevn szeretném megoldani a problémát. Először Node.Js-re gondoltam,
de a W3School kurzusa előbb végetért, mint hogy a nekem fontos részhez értem volna. Fizetni a folytatásért pedig nem akartam.

A Python lett a következő választás. Azért is erre gondoltam, mert a rá épülő Django-t is meg szeretném ismerni.

Amíg a Python szkripthez nem tudok eleget, az egyszerű Win10 Cmd Script-et használom: v0.1

## v 01a

* Stabil verzió: 2024-01-20
* Script nyelv: Win CMD
* Tömörítés: 7zip
* Mentés paraméterek tárolása a CMD script-ben.
* A (mentendő és a cél könvytár) pároknak a CMD script-ben.
* Logozás 
    - Script echo üzenetek átirányítása text file-ba.
    - Tömörító stdout átirányítása text file-ba.

## v 01b

Új funkciók a v01a-hz képest:

1. A mentendő utasítások feltételhez kötése (if 1==1...) a tesztelés könnytéséhez.
1. A mentés idejének mérése és kiírása a Python-os verzióval való összehasonlíthatóság érdekébe.

### Készült

Budapest, 2024-07-07

## v 02a

* Stabil verzió: nincs
* Script nyelv: Win CMD/PowerShell, Python
* Tömörítés: zipfile (Python module)
* A (mentendő és a cél könvytár) pároknak a tárolás a **mentestabla.cvs** file-ban.
* Logozás 
    - Script üzenetek írása a képernyőre.
    - A futásról mapló/log file készül, file-onként mutatja\
    a mentés sikerességét, és a végén egy összegzést.
    - A logozásra külön modul készült: z9log_mod.py.\
    Ha módosítani akarjuk a logozást, akkor a "**z9log.cfg**" (encode=utf-8) file-t kell használni.\
    Info
      * [python &raquo; logging.config — Logging configuration &raquo; Configuration file format](https://docs.python.org/3/library/logging.config.html)

# Github

Link: [mentes_verziok](https://github.com/zavorszky/mentes_verziok)

# Szerző

Závorszky István\
zavorszky@yahoo.com
