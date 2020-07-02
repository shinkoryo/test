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


＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃
LinuxコマンドとWindowsコマンドで、それぞれListWorksフォルダーの一覧を更新日時が新しい順で取得します。
取得したリストをもとに、マッピングリストを作成します。

Linuxコマンド：
	ls -ltri --time-style="+%Y/%m/%d %H:%M:%S.%N" >/tmp/lvdata_sortbymtime.txt
	
Windowsコマンド：
	dir /a:d /TW /OD \\10.11.1.35\lv-data$\LVDATA |findstr /v /r "\.\.*$">c:\tmp\Windows_sortBymtime.txt

図を貼り付ける。



