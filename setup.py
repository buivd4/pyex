from setuptools import setup, find_packages
setup(
   name='pyex',
   version="0.0.1",
   description='Excel to JSON converter.',
   author='Duong Bui',
   author_email='buivd4@hotmail.com',
   packages=find_packages(),
   entry_points = {
        'console_scripts': ['pyex=pyex.main:run'],
    },
   install_requires=[
       "openpyxl==3.0.10",
       "flask==2.1.2",
       "waitress==2.1.2",
       "accept-types==0.4.1"
   ]
)