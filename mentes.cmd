chcp 65001
@echo off
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

if not exist mentes.log echo "create mentes.log" > mentes.log
call mentes_mag.cmd >> mentes.log

@echo off
echo .
echo . A mentés kész.
echo . Az ablak bezárásához nyomjon egy (Enter)-t.
pause > nul
