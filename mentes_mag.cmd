@echo off

setlocal
echo .
echo . -----------------------------
echo . Mentés mag (menets_mag.cmd)
echo . %date% %time%
@echo off

call e:\felhasznalok\dady\sajat_programok\_ini_\set_ffn_7za.cmd

rem -- Kezdési idő feljegyzése

set z9kezdido=%time%

rem -- Mentések, teszteléshez 'if'-ek

if 1==1 %ffn_7za% a -r i:\DADY\mentes\esemenyek h:\DADY\rend\esemenyek\
if 1==0 %ffn_7za% a -r i:\DADY\mentes\temak   h:\DADY\rend\temak\
if 1==0 %ffn_7za% a    i:\DADY\mentes\rend    h:\DADY\rend\rend\
if 1==0 %ffn_7za% a -r i:\DADY\mentes\konyvek h:\DADY\raktar\Konyvtar\konyvek\
if 1==0 %ffn_7za% a -r i:\DADY\mentes\sajat_programok_ini_   e:\felhasznalok\dady\sajat_programok\_ini_\
if 1==0 %ffn_7za% a -r i:\DADY\mentes\sajat_programok_mentes e:\felhasznalok\dady\sajat_programok\mentes\ -xr!*.log

rem -- Befejezési idő feljegyzése

set z9befido=%time%

rem -- Tömörítési idő kiszámítása, kiírása

rem -- Az időpontok (centisec = század másodperc)-re konvertálva
set /A kezdido_csec=(1%z9kezdido:~0,2%-100)*360000 + (1%z9kezdido:~3,2%-100)*6000 + (1%z9kezdido:~6,2%-100)*100 + (1%z9kezdido:~9,2%-100)
set /A befido_csec=(1%z9befido:~0,2%-100)*360000 + (1%z9befido:~3,2%-100)*6000 + (1%z9befido:~6,2%-100)*100 + (1%z9befido:~9,2%-100)

rem -- Végrehajtási idő kiszámítása század másodpercben
set /A vegrehajtasido_csec=%befido_csec%-%kezdido_csec%

rem -- A végrehajtási idő felbintása órára, percre, másodpercre
set /A vegrehajtasido_h=%vegrehajtasido_csec% / 360000
set /A vegrehajtasido_min=(%vegrehajtasido_csec% - %vegrehajtasido_h%*360000) / 6000
set /A vegrehajtasido_sec=(%vegrehajtasido_csec% - %vegrehajtasido_h%*360000 - %vegrehajtasido_min%*6000) / 100
set /A vegrehajtasido_sec2=(%vegrehajtasido_csec% - %vegrehajtasido_h%*360000 - %vegrehajtasido_min%*6000 - %vegrehajtasido_sec%*100)

rem -- Formázás, 0-val kiegészítés, ha kell
if %vegrehajtasido_h% LSS 10 set vegrehajtasido_h=0%vegrehajtasido_h%
if %vegrehajtasido_min% LSS 10 set vegrehajtasido_min=0%vegrehajtasido_min%
if %vegrehajtasido_sec% LSS 10 set vegrehajtasido_sec=0%vegrehajtasido_sec%
if %vegrehajtasido_sec2% LSS 10 set vegrehajtasido_sec2=0%vegrehajtasido_sec2%

rem -- Kiírás
rem -- echo Kezdés időpontja: %kezdido_csec% [centisecond]
rem -- echo Befejezés időpontja: %befido_csec% [centisecond]
rem -- echo Végrehajtás ideje: %vegrehajtasido_csec% [centisecond]
echo . Mentés kezdete: %z9kezdido%
echo . Mentés befejezése: %z9befido%
echo .
echo . Mentés/tömörítés-re fordított idő
echo . %vegrehajtasido_h% h  %vegrehajtasido_min% m  %vegrehajtasido_sec%,%vegrehajtasido_sec2% s

rem -- Info
rem --   SS64: SET: https://ss64.com/nt/set.html#expressions
rem --   stackoverflow: Calculate time difference in Windows batch file: https://stackoverflow.com/questions/9922498/calculate-time-difference-in-windows-batch-file

endlocal
