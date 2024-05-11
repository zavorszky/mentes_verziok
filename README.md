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

A Python let a következő választás. Azért is erre gondoltam, mert a rá épülő Django-t is meg szeretném ismerni.

Amíg a Python szkripthez nem tudok eleget, az egyszerű Win10 Cmd Script-et használom: v0.1

## v0.1

* Stabil verzió: 2024-01-20
* Script nyelv: Win CMD
* Tömörítés: 7zip
* Logozás 
    - Script echo üzenetek átirányítása text file-ba.
    - Tömörító stdout átirányítása text file-ba.

## v2.0

* Stabil verzió: nincs
* Script nyelv: Win CMD, Python
* Tömörítés: 7zip
* Mentés paraméterek tárolása a "**mentes.json**" file-ban.
* Logozás 
    - Script üzenetek írása text file-ba. Ez egy log file,\
    amiben összefoglaló üzenetek kerülnek a mentés lépéseirő,\
    majd a mentésről egy összefoglaló információs sor.
    - Tömörító stdout átirányítása text file-ba. Minden mentés esetén
      külön text file készül a tömörítő üzeneteiről.
    - A tömörítő üzeneteit tartalmazó file-ok közül a régieket törölni kell.
    - A logozásra külön modul készült: z9log_mod.py.\
    Ha módosítani akarjuk a logozást, akkor a "**z9log.cfg**" (ecode=utf-8) file-t kell használni.\
    Info: [python &raquo; logging.config — Logging configuration &raquo; Configuration file format](https://docs.python.org/3/library/logging.config.html)


# Készült

Budapest, 2024-04-20 ...\
Závorszky István

zavorszky@yahoo.com
