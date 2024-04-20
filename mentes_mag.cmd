
@echo off
echo -----------------------------
echo Mentés mag (menets_mag.cmd)
date < nul
time < nul
@echo on

call e:\felhasznalok\dady\sajat_programok\_ini_\set_ffn_7za.cmd

%ffn_7za% u -r -wc:\ProgramData\tmp\ i:\DADY\mentes\esemenyek       h:\DADY\rend\esemenyek\
%ffn_7za% u -r -wc:\ProgramData\tmp\ i:\DADY\mentes\temak           h:\DADY\rend\temak\
%ffn_7za% u    -wc:\ProgramData\tmp\ i:\DADY\mentes\rend            h:\DADY\rend\rend\
%ffn_7za% u -r -wc:\ProgramData\tmp\ i:\DADY\mentes\konyvek         h:\DADY\raktar\Konyvtar\konyvek\

%ffn_7za% u -r -wc:\ProgramData\tmp\ i:\DADY\mentes\sajat_programok e:\felhasznalok\dady\sajat_programok\_ini_\
%ffn_7za% u -r -wc:\ProgramData\tmp\ i:\DADY\mentes\sajat_programok e:\felhasznalok\dady\sajat_programok\mentes\ -xr!*.log
