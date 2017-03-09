try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': "Tool for Google's DFP",
    'author': 'M T',
    'url': 'n/a',
    'download_url': 'n/a',
    'author_email': 'mthompson at cars dot com',
    'version': '0.1',
    'install_requires': ['openpyxl', 'googleads'],
    'packages': ['ZombieScript'],
    'scripts': ['Spreadsheets', 'main'],
    'name': 'ZombieScript'
}

setup(**config)
