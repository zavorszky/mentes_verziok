"""
Csomag:     z9log
File:       z9log_mod
Feladat:
  Logoláshoz logger szolgáltatása.
  Ha meg van a "z9log.cfg" konfigurációs file, akkor annak a beállítása szerint
  történik a loggolás, ha nincs meg, akkor a program beállít néhány jellemzőt.
Info:
  * python: Logging HOWTO: https://docs.python.org/3/howto/logging.html#logging-howto
  * python: logging — Logging facility for Python: https://docs.python.org/3/library/logging.html
  * stackoverflow: Python logging: use milliseconds in time format: https://stackoverflow.com/questions/6290739/python-logging-use-milliseconds-in-time-format
    A "z9log.cfg"-ben a log rekord formátumának beállításához hasznos.
  Saját tapasztalatok:
    (1) A "logging.config"-nak olyan log file nevet adunk meg, ami Win-ben használatos (\),
    akkor a "logger" objektum  "NoneType" objektum lesz, így nincs attribútuma.
Fejlesztő:  zavorszky@yahoo.com
Létrehozás: 2024-05-11
"""

import os
import logging
import logging.config


# Konstansok
# ----------
LOGCFGFILE_NAME = "z9log.cfg"
LOGCFGFILE_ENCODING = "utf-8"
LOGFILE_ENCODING = "utf-8"
LOG_LINEFORMAT = "%(asctime)s [%(levelname)s] %(message)s"


# Függvények
# ----------


class Naplo:
    def __init__(self, p_logger_name: str, p_logfile_name: str, p_sorszam: int) -> None:
        self.logger_name = p_logger_name
        self.sorszam = p_sorszam

        if os.sep == "/":
            self.logfile_name = p_logfile_name
        else:
            self.logfile_name = p_logfile_name.replace("\\", "/")

        try:
            # logger készítése
            self.logger = logging.getLogger(p_logger_name)
            # logger beállítása
            if os.path.exists(LOGCFGFILE_NAME):
                # Van a logozást beállító konfigurációs file.
                logging.config.fileConfig(
                    LOGCFGFILE_NAME,
                    defaults={"logfilename": self.logfile_name},
                    disable_existing_loggers=False,
                    encoding=LOGCFGFILE_ENCODING,
                )
            else:
                # A logozás jellemzőit a program állítja be.
                logging.basicConfig(
                    filename=p_logfile_name,
                    format=LOG_LINEFORMAT,
                    encoding=LOGFILE_ENCODING,
                    level=logging.DEBUG,
                )
        except Exception as e:
            self.logger = None
            raise RuntimeError(
                f"Nem sikerült a 'Naplo' osztályt példányosítani. Hiba:{e}"
            )

    def irInfo(self, p_uzenet: str) -> None:
        self.logger.info(f"[{self.sorszam}] {p_uzenet}")

    def irWarn(self, p_uzenet: str) -> None:
        self.logger.warning(f"[{self.sorszam}] {p_uzenet}")

    def irErr(self, p_uzenet: str) -> None:
        self.logger.error(f"[{self.sorszam}] {p_uzenet}")
