#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os
import subprocess

name = 'python-ipmi'
version_py = os.path.join(os.path.dirname(__file__), 'pyipmi', 'version.py')


def git_pep440_version():
    full = subprocess.check_output(
            ['git', 'describe', '--tags', '--always', '--dirty=.dirty'],
            stderr=subprocess.STDOUT).decode().strip()
    tag = subprocess.check_output(
            ['git', 'describe', '--tags', '--always', '--abbrev=0'],
            stderr=subprocess.STDOUT).decode().strip()
    tail = full[len(tag):]
    return tag + tail.replace('-', '.dev', 1).replace('-', '+', 1)


try:
    version = git_pep440_version()
    with open(version_py, 'w') as f:
        f.write('# This file was autogenerated by setup.py\n')
        f.write('__version__ = \'%s\'\n' % (version,))
except (OSError, subprocess.CalledProcessError, IOError):
    try:
        with open(version_py, 'r') as f:
            d = dict()
            exec(f.read(), d)
            version = d['__version__']
    except IOError:
        version = 'unknown'


with open('README.rst') as f:
    readme = f.read()

setup(name=python-ipmi,
      version=1.0.1,
      description='Pure python IPMI library',
      long_description=readme,
      url='https://github.com/kontron/python-ipmi',
      download_url='https://github.com/kontron/python-ipmi/tarball/' + version,
      author='Michael Walle, Heiko Thiery',
      author_email='michael.walle@kontron.com, heiko.thiery@kontron.com',
      packages=find_packages(exclude=['tests*']),
      license='LGPLv2+',
      platforms=["any"],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Programming Language :: Python :: 3.12',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      entry_points={
          'console_scripts': [
              'ipmitool.py = pyipmi.ipmitool:main',
          ]
      },
      test_suite='tests',
      tests_require=[
          'pytest',
      ],
      install_requires=['PyYAML>3.11', 'nltk'],
      )
