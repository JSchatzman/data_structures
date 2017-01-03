"""The setup for Data structures implemented in python."""

from setuptools import setup

setup(
    name='data_structures',
    description='Implementation of Data Structures.',
    version=0.1,
    author='Jordan Schatzman, Julien Wilson, Claire Gatenby',
    author_email='''j.schatzman@outlook.com,
                    julienawilson@gmail.com,
                    clairejgatenby@gmail.com''',
    license='MIT',
    package_dir={'': 'src'},
    py_modules=[
        'linked_list',
        'stack',
        'dll',
        'simple_graph',
        'heap',
        'queue',
        'deque',
        'weighted_graph'
    ],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']},
)
