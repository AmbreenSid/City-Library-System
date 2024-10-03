# Change the values of the following variables to match the needs of
# your project.
# Run the command "sh virtualenv-installer-mac.sh" in Terminal and
# this file will run the necessary commands to install virtualenv for you.
INSTALL_VIRTUALENV=true
INSTALL_VIRTUALENVWRAPPER=true
VIRTUALENV_NAME="myvirtualenv"
MAKE_NEW=true

if [ "$INSTALL_VIRTUALENV" = true ] ; then
    echo "Installing virtualenv"
    sudo pip3 install virtualenv --user
fi
if [ "$INSTALL_VIRTUALENVWRAPPER" = true ] ; then
    echo "Installing virtualenvwrapper"
    sudo pip3 install virtualenvwrapper --user
fi

if [ "$MAKE_NEW" = true ] ; then
    echo "Making new virtualenv"
    sudo mkvirtualenv "$VIRTUALENV_NAME"
else
    echo "Using existing virtualenv"
    sudo workon "$VIRTUALENV_NAME"
fi
