#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='django-remote-forms',
    version='0.0.1-p1',
    description='A platform independent form serializer for Django.',
    author='WiserTogether Tech Team',
    author_email='tech@wisertogether.com',
    url='http://github.com/wisertoghether/django-remote-forms/',
    long_description=open('README.md', 'r').read(),
    packages=find_packages(),
    package_data={
    },
    zip_safe=False,
    requires=[
    ],
    install_requires=[
    ],
    classifiers=[
        'Development Status :: Pre Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: MIT',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)
