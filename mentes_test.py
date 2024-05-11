# Projekt: mentes
# Rövid leírás: Tesztelés.
# File: mentes_test.py
# Feladat: Teszt vezérelt fejlesztés (Test Driven Development) támogatása.
# Programkód tipus: Python test
# Felhasználás:
#   > python -m unittest mentes_test.py
#     (A "mentes_test.py"-ben nem kell a tesztelő osztályt példányosítan.)
# Info:
#   HojaLeaks kódolási oktatóanyagok: Oktatóanyag: Tesztvezérelt fejlesztés a Pythonban: https://hojaleaks.com/tutorial-test-driven-development-in-python
#   Python: unittest - Unit testing framework: https://docs.python.org/3/library/unittest.html
# Készült: 2024-05-11
# Szerző: zavorszky@yahoo.com

import unittest
import mentes

if __name__ == "__main__":
    mentes.test_main()