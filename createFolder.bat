@echo off
set /p n="Enter number of folders: "
for /L %%i in (1,1,%n%) do (
	mkdir "Module_%%i"
	echo This is Module %%i > "Module_%%i\README.MD"
)
pause