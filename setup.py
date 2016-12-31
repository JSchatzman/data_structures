"""The setup for data structures."""

from setuptools import setup

setup(
    name='data_structures',
    description='Implementation of Data Structures in Python.',
    version=0.1,
    author='Jordan Schatzman, Julien Wilson, Claire Gatenby',
    author_email='j.schatzman@outlook.com, julienawilson@gmail.com, clairejgatenby@gmail.com',
    license='MIT',
    package_dir={'': 'src'},
    py_modules=['linked_list', 'stack', 'dll', 'deque', 'queue', 'heap'],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']},
)
