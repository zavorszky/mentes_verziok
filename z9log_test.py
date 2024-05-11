# Projekt: n/a
# Rövid leírás: Naplózás tesztelése.
# File: z9log_test.py
# Programkód tipus: Python test
# Feladat: ...
# Felhasználás:
#   > & python z9log_test.py
# Info:
#   ...
# Készült: 2024-05-11
# Szerző: zavorszky@yahoo.com

import z9log_mod

if __name__ == "__main__":
    log = z9log_mod.get_logger(p_logger_name=__name__, p_logfile_name="z9log_test.log")
    log.info("1.Indul logozás teszt...")
    log.info("2.logozás...")
    log.info("3.Vége a logozás tesztnek.")
