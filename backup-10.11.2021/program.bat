@echo off
goto menu

:menu
cls
echo Witam w programie m7n5KAROTKA
echo 1. Uruchom program
echo 2. Informacje
echo 3. Backup
echo 4. Zakoncz program
set /p choice=
cls
if %choice%==1 goto runScript
if %choice%==2 goto showInformation
if %choice%==3 goto backup
if %choice%==4 exit
goto :menu

:runScript
call main.py
start chrome.exe index.html
pause
cls
goto menu

:showInformation
echo Artur Pabjan Semestr III
echo m7naKAROTKA
echo Skrypt polega na znalezieniu slow, gdzie ostatnia dana liczba liter czytana od końca znajduje sie w słowniku, lecz czytana od poczatku nie. Program wykonuje skrypt zapisujacy wyniki, a nastepnie tworzy strony i ją otwiera, gdzie podana jest statystyka.
pause
cls
goto menu

:backup
md backup-%date%
xcopy *.* backup-%date%\
pause
cls
goto menu

@echo on