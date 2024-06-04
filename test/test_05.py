"""
Info:
  geeksforgeeks: Working with zip files in Python: https://www.geeksforgeeks.org/working-zip-files-python/
  Python: zipfile — Work with ZIP archives: https://docs.python.org/3/library/zipfile.html
  stackoverflow: Python zipfile module: difference between zipfile.ZIP_DEFLATED and zipfile.ZIP_STORED: https://stackoverflow.com/questions/5298169/python-zipfile-module-difference-between-zipfile-zip-deflated-and-zipfile-zip-s
"""

#from zipfile import ZipFile
import zipfile
import os
import datetime


def get_all_file_path(p_konyvtar) -> list:
    file_paths = []

    for root, directories, files in os.walk(p_konyvtar):
        for filename in files:
            if os.sep == "/":
                filepath = os.path.join(root, filename)
            else:
                filepath = (os.path.join(root, filename)).replace("\\", "/")
            file_paths.append(filepath)
    return file_paths


# gafp = get_all_file_path('./test')
# print(gafp)


def main() -> None:
    konyvtar: str = "./test"

    allomanyok = get_all_file_path(konyvtar)

    print("Tömörítendő file-ok:")
    for allomany in allomanyok:
        print(f"\t{allomany}")

    print("\nTömörítés...")
    # with ZipFile("teszt.zip","w") as zip:
    # with zipfile.ZipFile(file="teszt.zip",mode="w",compression=zipfile.ZIP_STORED) as zip:
    with zipfile.ZipFile(file="teszt.zip",mode="w",compression=zipfile.ZIP_DEFLATED) as zip:
        for allomany in allomanyok:
            zip.write(allomany)

    print("\tKész a tömörítés")

    print("\nA tömörítés adatai:")
    with zipfile.ZipFile("teszt.zip", "r") as zip:
        for info in zip.infolist():
            print(info.filename)
            print("\tModified:\t" + str(datetime.datetime(*info.date_time)))
            print("\tSystem:\t\t" + str(info.create_system) + "(0 = Windows, 3 = Unix)")
            print("\tZIP version:\t" + str(info.create_version))
            print("\tCompressed:\t" + str(info.compress_size) + " bytes")
            print("\tUncompressed:\t" + str(info.file_size) + " bytes")


if __name__ == "__main__":
    main()
