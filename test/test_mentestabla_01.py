import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# *************************************

import mentesglogal_mod as mgm
import mentes

mgm.vegrehajtas = {"tomorites": True}

mentes.main(p_mentestablafile_nev="./test/test_mentestabla_01.csv")
