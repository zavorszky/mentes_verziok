"""
File
    test_01.py
Feladat
    A 'z9timer_mod' modul próbája.
    (A 'tesztelés' szót fenntartom az olyan komolyabb tesztelésre
    ahol tesztnaplót készítek teszt esetekkel, használom a Python
    'unittest' modult.)
Info
    Tutorial Python: Python Import from parent directory: https://tutorpython.com/python-import-from-parent-directory/
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# *************************************

import z9timer_mod as t

print("\n")

stopper = t.Stopper()

stopper.inditas()

valasz = input("Várakozás (Enter)-rel...")

stopper.megallitas()

print("Eltelt idő: ", stopper.eltelt_ido_str())
print("Eltelt idő: ", stopper.eltelt_ido_masodperc())
