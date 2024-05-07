# File: z9project_test.py
# Code type: app
# Description: A [z9project] tesztelése.
# Use: irreveláns
# Importok: nincs
# Created: 2024-05-06
# Author: zavorszky@yahoo.com

import z9project

# Éles kód, függvény hívás.

z9project.file_gen()

# Próba kódok

"""
# 1.
import re
reobj = re.search("^[a-zA-Z]([a-z]|[0-9])*$", "1aa")
if reobj:
    print(reobj)
else:
    print("x")
"""

"""
# 2.
print("Teszt 2.")
try:
    raise Exception("Exception-1")
except RuntimeError as re:
    print("RuntimeError")
    print(re)
    raise Exception("Exception-a")
except Exception as e:
    print("Exception")
    print(e)
    raise Exception("Exception-b")
finally:
    print("Finally")
"""