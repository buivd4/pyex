from setuptools import setup, find_packages
from pyex import VERSION

setup(
   name='pyex',
   version=VERSION,
   description='Excel to JSON converter.',
   author='Duong Bui',
   author_email='buivd4@hotmail.com',
   packages=find_packages(),
   entry_points = {
        'console_scripts': ['pyex=pyex.main:run'],
    },
   install_requires=[
       "openpyxl==3.0.10"
   ]
)