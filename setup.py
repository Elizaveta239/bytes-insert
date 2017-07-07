from distutils.core import setup
import sys

if not (sys.version_info[0] == 3 and sys.version_info[1] >= 6):
    sys.exit('The library supports only Python 3.6')

setup(
    name='bytesinsert',
    version='0.2.0',
    packages=['bytesinsert', 'bytesinsert.tests'],
    url='https://github.com/Elizaveta239/bytes-insert',
    license='MIT',
    author='Elizaveta Shashkova',
    author_email='elizabeth.shashkova@gmail.com',
    description='A library for inserting a piece of code into another piece of code'
)
