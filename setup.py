#!/usr/bin/env python
from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

requires = ['ply>=3.4', 
            'jssc']

setup(
    name='jssc',
    version='0.1',
    description='JavaScript Source Compiler',
    long_description=readme,
    author='Adam Venturella',
    author_email='aventurella@gmail.com',
    url='https://github.com/aventurella/jssc',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=requires,
    platforms=['Any'],
    scripts=[],
    provides=[],
    namespace_packages=[],
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'jssc = jssc.main:main'
            ]
        },
    zip_safe=False,
)
