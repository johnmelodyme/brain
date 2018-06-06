#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
from setuptools import setup, find_packages
from codecs import open
from os import path

basedir = path.abspath(path.dirname(__file__))

# locate our version number
def read_version_py(file_name):
    try:
        version_string_line = open(file_name, "rt").read()
    except EnvironmentError:
        return None
    else:
        version_regex = r"^version_str = ['\"]([^'\"]*)['\"]"
        mo = re.search(version_regex, version_string_line, re.M)
        if mo:
            return mo.group(1)

VERSION_PY_FILENAME = 'brain/_version.py'
version = read_version_py(VERSION_PY_FILENAME)

setup(
    name='brain-ai',
    version=version,
    description='Build your own intelligent personal assistant.',
    long_description='Brain.ai is an open source intelligent personal assistant development package.',
    url='https://github.com/brain-ai/brain',
    author='Alexander Paul P. Quinit',
    author_email='paulquinit@gmail.com',
    license='GNU General Public License v3 (GPLv3)',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Home Automation',
        'Topic :: Multimedia :: Sound/Audio :: Speech',
        'Topic :: Multimedia :: Sound/Audio :: Sound Synthesis',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
    keywords='assistant bot TTS STT brain',

    packages=find_packages(exclude=['docs', 'tests']),

    install_requires=[
        'pyyaml>=3.12',
        'six>=1.10.0',
        'SpeechRecognition>=3.7.1',
        'markupsafe>=1.0',
        'pyaudio>=0.2.11',
        'pyasn1>=0.2.3',
        'ansible>=2.3,<2.4',
        'jinja2>=2.10',
        'cffi>=1.9.1',
        'ipaddress>=1.0.17',
        'flask>=0.12',
        'Flask-Restful>=0.3.5',
        'flask_cors>=3.0.2',
        'requests>=2.13',
        'httpretty>=0.8.14',
        'mock>=2.0.0',
        'Flask-Testing>=0.6.2',
        'apscheduler>=3.3.1',
        'GitPython>=2.1.3',
        'packaging>=16.8',
        'transitions>=0.4.3',
        'sounddevice>=0.3.7',
        'SoundFile>=0.9.0',
        'pyalsaaudio>=0.8.4',
        'sox>=1.3.0',
        'paho-mqtt>=1.3.0',
        'voicerss_tts>=1.0.3'
    ],

    package_data={
        'brain': [
            'trigger/snowboy/armv7l/python27/_snowboydetect.so',
            'trigger/snowboy/x86_64/python27/_snowboydetect.so',
            'trigger/snowboy/x86_64/python34/_snowboydetect.so',
            'trigger/snowboy/x86_64/python35/_snowboydetect.so',
            'trigger/snowboy/x86_64/python36/_snowboydetect.so',
            'trigger/snowboy/resources/*',
            'sounds/*'
         ],
    },

    entry_points={
        'console_scripts': [
            'brain=brain:main',
        ],
    },
)
