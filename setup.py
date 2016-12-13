"""The setup for Mailroom distribution."""

from setuptools import setup

setup(
    name='linked_list',
    description='Implementation of Linked List.',
    version=0.1,
    author='Jordan Schatzman, Julien Wilson',
    author_email='j.schatzman@outlook.com, julienawilson@gmail.com',
    license='MIT',
    package_dir={'': 'src'},
    py_modules=['linked_list'],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']},
)
