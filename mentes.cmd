chcp 65001
@echo off

setlocal

rem -- set z9logfilename=mentes.log
set z9logfilename=test_mentes.log
echo . 
echo . Mentések (mentes.cmd)
echo . ---------------------
echo . Kérem csatlakoztassa a pendrive-ot az I: meghajtóhoz!
echo . 
echo . A folytatáshoz nyomjon egy (Enter)-t,
echo . vagy (Ctrl-C)-vel megszakíthatja az indítást.
echo .
pause > nul
echo .
echo . A mentés elindult...

if not exist %z9logfilename% echo "create %z9logfilename%" > %z9logfilename%
call mentes_mag.cmd >> %z9logfilename%

@echo off
echo .
echo . A mentés kész.
echo . Az ablak bezárásához nyomjon egy (Enter)-t.
pause > nul

endlocal
