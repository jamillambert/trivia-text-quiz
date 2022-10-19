import os
import sys

from setuptools import setup, find_packages

setup(
    name='trivia-text-quiz',
    version='1.0.0',
    description='Text based trivia quiz. Questions from the Open Trivia Database',
    license='GPL v3',
    author='Jamil Lambert',
    packages=['src'],
    install_requires=['bs4'],
    entry_points={
        'console_scripts': [
            'trivia-text-quiz=src.app:main']
    },
    classifiers=['Operating System :: OS Independent',
                 'Programming Language :: Python :: 3.10',
                 'Operating System :: MacOS :: MacOS X',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX',
                 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'],
)
