
@echo off
echo -----------------------------
echo Mentés mag (menets_mag.cmd)
echo %date%
echo %time%
@echo off

call e:\felhasznalok\dady\sajat_programok\_ini_\set_ffn_7za.cmd

rem -- Kezdési idő feljegyzése

set z9kezdido = %time%

:feladatblokk_eleje

%ffn_7za% u -r -wc:\ProgramData\tmp\ i:\DADY\mentes\esemenyek       h:\DADY\rend\esemenyek\
goto cim_feladatblokk_vege
%ffn_7za% u -r i:\DADY\mentes\temak           h:\DADY\rend\temak\
%ffn_7za% u    i:\DADY\mentes\rend            h:\DADY\rend\rend\
%ffn_7za% u -r i:\DADY\mentes\konyvek         h:\DADY\raktar\Konyvtar\konyvek\

%ffn_7za% u -r i:\DADY\mentes\sajat_programok e:\felhasznalok\dady\sajat_programok\_ini_\
%ffn_7za% u -r i:\DADY\mentes\sajat_programok e:\felhasznalok\dady\sajat_programok\mentes\ -xr!*.log

:cim_feladatblokk_vege

rem -- Befejezési idő feljegyzése

set z9befido = %time%

rem -- Tömörítési idő kiszámítása, kiírása
echo Kezdés időpontja: %z9kezdido%
echo Befejezés időpontja: %z9befido%

rem -- Az időpontok (centisec = század másodperc)-re konvertálva
set /A kezdido_csec=(1%z9kezdido:~0,2%-100)*360000 + (1%z9kezdido:~3,2%-100)*6000 + (1%z9kezdido:~6,2%-100)*100 + (1%z9kezdido:~9,2%-100)
set /A befido_csec=(1%z9befido:~0,2%-100)*360000 + (1%z9befido:~3,2%-100)*6000 + (1%z9befido:~6,2%-100)*100 + (1%z9befido:~9,2%-100)

rem -- Végrehajtási idő kiszámítása század másodpercben
set /A vegrehajtásido_csec=%befido_csec%-%kezdido_csec%

rem -- A végrehajtási idő felbintása órára, percre, másodpercre
set /A vegrehajtásido_hora=%vegrehajtásido_csec% / 360000
set /A vegrehajtásido_min=(%vegrehajtásido_csec% - %vegrehajtásido_hora%*360000) / 6000
set /A vegrehajtásido_sec=(%vegrehajtásido_csec% - %vegrehajtásido_hora%*360000 - %vegrehajtásido_min%*6000) / 100
set /A vegrehajtásido_sec2=(%vegrehajtásido_csec% - %vegrehajtásido_hora%*360000 - %vegrehajtásido_min%*6000 - %vegrehajtásido_sec%*100)

rem -- Formázás, 0-val kiegészítés, ha kell
if %vegrehajtásido_h% LSS 10 set vegrehajtásido_h=0%vegrehajtásido_h%
if %vegrehajtásido_min% LSS 10 set vegrehajtásido_min=0%vegrehajtásido_min%
if %vegrehajtásido_sec% LSS 10 set vegrehajtásido_sec=0%vegrehajtásido_sec%
if %vegrehajtásido_sec2% LSS 10 set vegrehajtásido_sec2=0%vegrehajtásido_sec2%

rem -- Kiírás
echo Kezdés időpontja: %kezdido_csec% [centisecond]
echo Befejezés időpontja: %befido_csec% [centisecond]
echo Végrehajtás ideje: %vegrehajtásido_csec% [centisecond]
echo %vegrehajtásido_h% h  %vegrehajtásido_min% m  %vegrehajtásido_sec%,%vegrehajtásido_sec2% s

rem -- Info
rem --   SS64: SET: https://ss64.com/nt/set.html#expressions
rem --   stackoverflow: Calculate time difference in Windows batch file: https://stackoverflow.com/questions/9922498/calculate-time-difference-in-windows-batch-file
