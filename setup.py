"""The setup for Mailroom distribution."""

from setuptools import setup

setup(
    name='data_structures',
    description='Implementation of Data Structures.',
    version=0.1,
    author='Jordan Schatzman, Julien Wilson, Claire Gatenby, Conor Clary',
    author_email='j.schatzman@outlook.com, julienawilson@gmail.com, clairejgatenby@gmail.com, sclary50@gmail.com',
    license='MIT',
    package_dir={'': 'src'},
    py_modules=['data_structures'],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']},
)
