python -m pip install --user --upgrade setuptools==58.3.0
python setup.py sdist
pip install wheel
python setup.py bdist_wheel
pip install ./dist/my_minipack-1.0.0.tar.gz