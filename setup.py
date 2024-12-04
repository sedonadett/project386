from setuptools import setup, find_packages


with open('requirements.txt') as f:
    requirements = f.readlines()


setup(
    name = 'nfl386',
    version = '0.0.1',
    packages = find_packages(),
    # install_requires = ['numpy', 'pandas'],
    install_requires = requirements,
    author = 'Sedona Dettwiler and Ethan Beckstead',
    author_email = 'sedonadett@gmail.com',
    description = 'A package for NFL Win Analysis for Chiefs and Vikings',
    # idk about this package_data = {'nfl_package': ['datasets/chiefs.csv']}
)