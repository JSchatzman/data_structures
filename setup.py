"""The setup for Mailroom distribution."""

from setuptools import setup

setup(
    name='data_structures',
    description='Implementation of Data Structures.',
    version=0.1,
    author='Jordan Schatzman, Julien Wilson',
    author_email='j.schatzman@outlook.com, julienawilson@gmail.com',
    license='MIT',
    package_dir={'': 'src'},
    py_modules=['linked_list', 'stack', 'dll'],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']},
)
