@ECHO OFF

REM Some common chores
pushd %~dp0

REM cleans the directory

if "%1" == "clean" goto clean
if "%1" == "active" goto active
if "%1" == "inactive" goto inactive

ECHO "What would you like to do?"
goto end

:clean
ECHO del /s .\*.pyc
del /s .\*.pyc > nul 2> nul
ECHO del /s __pycache__
del /s __pycache__ > nul 2> nul
ECHO rmdir /s /q .pytest_cache\
rmdir /s /q .pytest_cache\ > nul 2> nul
ECHO rmdir /s /q .mypy_cache\
rmdir /s /q .mypy_cache\ > nul 2> nul
ECHO rmdir /s /q dist\
rmdir /s /q dist\ > nul 2> nul
ECHO rmdir /s /q *.egg-info\
rmdir /s /q *.egg-info\ > nul 2> nul
ECHO rmdir /s /q build\
rmdir /s /q build\ > nul 2> nul
ECHO del .coverage
del .coverage > nul 2> nul
goto end

:active
ECHO.
ECHO.
ECHO.
ECHO Wonder Twin powers, activate!
ECHO.
ECHO.
ENV\Scripts\activate.bat
goto end

:inactive
ECHO.
ECHO.
ECHO.
ECHO It wasn't my fault, sir; please don't deactivate me.
ECHO I told him not to go, but he's faulty, malfunctioning.
ECHO Kept babbling on about his 'mission.'
ECHO.
ECHO.
ENV\Scripts\deactivate.bat
goto end 

:end
popd
