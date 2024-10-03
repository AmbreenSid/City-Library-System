@ECHO OFF
REM Change the values of the following variables to match the needs of
REM your project.
REM Run the command "virtualenv-installer-win.bat" in CMD and
REM this file will run the necessary commands to install virtualenv for you.
SET "install_virtualenv=y"
SET "install_virtualenvwrapper=y"
SET "virtualenv_name=myvirtualenv"
SET "make_new=y"

IF "%install_virtualenv%"=="y" (
    ECHO Installing virtualenv
    pip install virtualenv
)
IF "%install_virtualenvwrapper%"=="y" (
    ECHO Installing virtualenvwrapper-win
    pip install virtualenvwrapper-win
)

IF "%make_new%"=="y" (
    ECHO Making new virtualenv
    mkvirtualenv "%virtualenv_name%"
) ELSE (
    ECHO Virtualenv already exists
    workon "%virtualenv_name%"
)

ECHO ON
