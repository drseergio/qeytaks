import os

from setuptools import setup

README = os.path.join(os.path.dirname(__file__), 'README.md')

setup(
    name='qeytaks',
    version = '1.0.1',
    description='keyword and label editor for photos',
    long_description=open(README).read() + 'nn',
    author='Sergey Pisarenko',
    author_email='drseergio@gmail.com',
    url='http://pisarenko.net',
    license='GPL',
    py_modules=['qeytaks_main'],
    packages=['qeytaks'],
    entry_points={
        'console_scripts': [
            'qeytaks=qeytaks_main:main']})
