from __future__ import absolute_import, division, print_function

import os
import sys
import platform
from setuptools import setup, find_packages

_this = os.path.abspath(os.path.dirname(__file__))

# for fn in os.listdir(_this):
#     print('files:', fn)

# def get_version(package):
#     with open(os.path.join(_this, package, 'version.py')) as f:
#         variables = {}
#         exec(f.read(), variables)
#         return variables['__version__']

# def get_version(package):
#     return open(os.path.join(_this, package, '__version__.py')).read()

def get_requirements(filename):
    contents = open(os.path.join(_this, filename)).read()
    return [
        req for req in contents.split('\n')
        if req != '' and not req.startswith('#')
    ]

setup(
    version='0.2.1',
    # package_data={
    #     'code_faster': ['sample/**/*'],
    # },
    install_requires=get_requirements('requirements-client.txt')
)