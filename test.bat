# makedir
@echo off

setlocal enabledelayedexpansion
SET row=0
FOR /F "tokens=2" %%i IN (ListWorksFolderList.txt) DO (
  SET /a row+=1
  IF !row! gtr 1 MD .\temp\%%i
)

# Rename
@echo off

SETLOCAL enabledelayedexpansion
SET row=0
FOR /F "tokens=2, 3" %%i IN (ListWorksFolderList.txt) DO (
  SET /a row+=1
  IF !row! gtr 1 REN .\temp\%%i "%%j"
)

rem output renamed folder name
FOR /d %%i IN (temp\*) DO (
  SET temp=%%i
  (ECHO !temp:temp\=%!) >> output.txt
)
