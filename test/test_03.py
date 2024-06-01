# Info:
#   stackoverflow: How to use "/" (directory separator) in both Linux and Windows in Python?: https://stackoverflow.com/questions/16010992/how-to-use-directory-separator-in-both-linux-and-windows-in-python
import sys


def modulKeresesiUtBeallitasa() -> None:
    aktualis_file_utvonal_list: list = __file__.split("\\")
    n: int = len(aktualis_file_utvonal_list)
    sys.path.append("\\".join(aktualis_file_utvonal_list[0 : (n - 2)]))


modulKeresesiUtBeallitasa()


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

import os
import z9packages.z9log.z9log_mod as lm
import z9packages.z9hiba.z9hiba_mod as hm

PRG_NEV = "test_main()"
PRGLOGFILE_NEV = "test_03.log"
PRGLOGFILE_PATH = "./test"  # A projekt gyökérkönyvtárhoz képest relatív útvonal.

# lfn: str = "./test/" + PRGLOGFILE_NEV  # Jó
# lfn: str = ".\\test\\" + PRGLOGFILE_NEV  # Jó
lfn: str = os.path.join(".","test", PRGLOGFILE_NEV) # Jó, ezt választom
# lfn: str = os.path.join("test", PRGLOGFILE_NEV) # Jó
# print(os.sep)
print("lfn=", lfn)

hibak = hm.Hibak()
LOG = lm.get_logger(
    p_logger_name=__name__,
    p_logfile_name=lfn,
    p_hibak=hibak,
)


def test_main():
    LOG.info("")
    LOG.info("Indul a '%s' függvény.", PRG_NEV)
    LOG.debug("Hibakereső bejegyzés.")
    LOG.info("Információs bejegyzés.")
    LOG.warning("Figyelmeztetés.")
    LOG.error("Hiba bejegyzés.")
    LOG.critical("Kritikus hiba bejegyzés.")
    LOG.info("Befejeződik a '%s' függvény.", PRG_NEV)


test_main()
