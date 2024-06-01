# A szülő modul könyvtár beillesztése a Python interpreter keresési sorába.
# Info:
#   stackoverflow: How to concatenate (join) items in a list to a single string: https://stackoverflow.com/questions/12453580/how-to-concatenate-join-items-in-a-list-to-a-single-string
#   stackoverflow: Python - Get path of root project structure: https://stackoverflow.com/questions/25389095/python-get-path-of-root-project-structure
import os
import sys

print("os.path.curdir=", os.path.curdir)
print("os.path.abspath(.)=", os.path.abspath(".")) # A program elindításakor a default könyvtár. Nem jó.
print("os.path.abspath(..)=", os.path.abspath(".."))
print("__file__=", __file__) # A file helye. Ez a teszt könyvtár ennek szülő könyvtára a modul könyvtár.
print("__file__.count(\\)=", __file__.count("\\"))
print("__file__.split(\\)=", __file__.split("\\"))
n = len(__file__.split("\\"))
print("n=", n)
print("__file__.split(\\)[0:n-2]=", __file__.split("\\")[0 : (n - 2)])
module_dir_1 = __file__.split("\\")[0 : (n - 2)]
module_dir_2 = "\\".join(module_dir_1)
print("module_dir_2=", module_dir_2)


"""
sys.path.append(
    "h:\\DADY\\Rend\\temak\\mentes_240420_1454\\mentes_verziok\\z9packages\\z9hiba"
)

"""
