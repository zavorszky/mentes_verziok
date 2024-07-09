rem -- A mentés alkalmazás telepítése
setlocal
set konyvtar_cel=e:\felhasznalok\dady\sajat_programok\mentes\

for /F %%g in (install_allomanynevek.txt) do (
    move /Y %konyvtar_cel%%%g %konyvtar_cel%%%g.old
    echo %%g átmozgatva
)


for /F %%g in (install_allomanynevek.txt) do (
    copy /Y %%g %konyvtar_cel%
)


endlocal
pause