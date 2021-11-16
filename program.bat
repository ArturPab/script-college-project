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

@REM Funkcja wlacza skrypt main.py, ktory uruchamia skrypty wykonujace zadanie oraz tworzenie strony, nastepnie ta strona zostaje otwarta w programie Google Chrome
:runScript
call main.py
start index.html
pause
cls
goto menu

@REM Funkcja wyswietlajaca informacje o projekcie
:showInformation
echo Artur Pabjan Semestr III
echo m7naKAROTKA
echo Skrypt polega na znalezieniu slow, gdzie ostatnia dana liczba liter czytana od końca znajduje sie w słowniku, lecz czytana od poczatku nie. Program wykonuje skrypt zapisujacy wyniki, a nastepnie tworzy strony i ją otwiera, gdzie podana jest statystyka.
pause
cls
goto menu

@REM Funkcja wykonujaca backup projektu
:backup
md backup-%date%
xcopy *.* backup-%date%\
pause
cls
goto menu

@echo on