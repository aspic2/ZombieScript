try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Tool for Google\'s DFP',
    'author': 'Michael Thompson',
    'url': 'n/a',
    'download_url': 'n/a',
    'author_email': 'mthompson@cars.com',
    'version': '0.1',
    'install_requires': ['openpyxl', 'googleads'],
    'packages': ['ZombieScript'],
    'scripts': ['Spreadsheets', 'main'],
    'name': 'ZombieScript'
}

setup(**config)
