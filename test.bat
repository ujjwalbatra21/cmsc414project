@echo off
START "" notepad
pause
dir c:\
pause
mkdir c:\test
dir c:\
pause
echo "test">c:\test\temp.txt
dir c:\test
pause
del c:\test\temp.txt
dir c:\test
pause
rmdir c:\test
dir c:\
pause