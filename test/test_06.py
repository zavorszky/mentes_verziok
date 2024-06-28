"""
File
    test_06.py
Feladat
    Kinlódás a szülő könyvtárban lévő modulok eléréséért,
    teszteléséért
Fejlesztő
    zavorszky@yahoo.com
Létrehozás
    2024-05-??
"""

import os


def pri(p_str: str) -> str:
    print(p_str.replace("\\", "/"))


def zipdir1(p_path) -> list[str]:
    files: list[str] = []
    for root, directories, files in os.walk(p_path):
        print("\n", root, directories, files)
        for file in files:
            # files.append((os.path.join(root, file)).replace("\\", "/"))
            # pri(os.path.join(root, file))
            pass
    return files


"""
print(os.getcwd())
os.chdir("h:\\DADY\\raktar\\Konyvtar\\")
print(zipdir1("./"))
print(os.getcwd())
"""


def path_szabvanyos(p_path: str) -> str:
    if os.sep == "/":
        return p_path
    else:
        return p_path.replace("\\", "/")


def zipdir2(p_path) -> list[str]:
    files2: list[str] = []
    for root, directories, files in os.walk(p_path):
        for file in files:
            # print(root, file)
            files2.append(path_szabvanyos(os.path.join(root, file)))
    return files2


print("\n")
path_eredeti = os.getcwd()
print("path_eredeti=", path_eredeti)
os.chdir("e:\\felhasznalok\\dady\\tmp")
print("path_uj=", os.getcwd())
print(zipdir2("./"))
# print(os.getcwd())
