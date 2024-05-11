# Projekt: mentes
# Rövid leírás: Tömörített mentés készítése HD-ról PenDrive-ra.
# File: mentes.py
# Feladat:
# Programkód tipus: Python app
# Felhasználás:
#   > & python mentes.py
# Info:
#   ...
# Készült: 2024-05-08
# Szerző: zavorszky@yahoo.com

import z9log_mod


# Konstansok
# ----------
PRG_NEV = "mentes.main()"
PRGLOGFILE_NEV = "mentes.log"
LOG = z9log_mod.get_logger(p_logger_name=__name__, p_logfile_name=PRGLOGFILE_NEV)


# Függvények
# ----------
def main():
    pass


def test_main():
    LOG.info("Indul a '%s' függvény.", PRG_NEV)
    LOG.debug("Hibakereső bejegyzés.")
    LOG.info("Információs bejegyzés.")
    LOG.warning("Figyelmeztetés.")
    LOG.error("Hiba bejegyzés.")
    LOG.critical("Kritikus hiba bejegyzés.")
    LOG.info("Befejeződik a '%s' függvény.", PRG_NEV)


# %%%%%%%%%%%%%%%%%

main()
