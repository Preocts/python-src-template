# Author: Preocts <preocts@preocts.com>

if [[ $# -eq 0 ]]; then
    echo "Usage: ./module_setup.sh [name_of_module]"
    exit 1
fi

echo "Setting up venv..."
if [ ! -d "./venv" ]; then
    python3 -m venv venv
    echo "Updating pip and tools in venv"
    ./venv/bin/pip install --upgrade pip wheel setuptools
fi
echo "Done."

echo "Creating module directories..."
if [ ! -d "./src" ]; then
    mkdir ./src
fi
if [ ! -d "./src/$1" ]; then
    mkdir ./src/$1
fi
echo "Done."

echo "Creating testing directories..."
if [ ! -d "./tests" ]; then
    mkdir ./tests
fi
if [ ! -d "./tests/fixtures" ]; then
    mkdir ./tests/fixtures
fi
echo "Done."

echo "Adding __init__.py ..."
touch ./src/$1/__init__.py
touch ./tests/__init__.py
echo "Done."

echo "Initialize git..."
if [ ! -d "./.git" ]; then
    git init
fi
echo "Done."

echo "Enter venv..."
source ./venv/bin/activate
INVENV=$( python -c 'import sys ; print( 0 if sys.prefix == sys.base_prefix else 1 )' )
if [ $INVENV -eq "0" ]; then
    echo "Something has gone wrong, aborting."
    exit 1
fi
echo "Done."

echo "Setup environment..."
make update
make install-dev
echo "Done."
echo "End of Line."
