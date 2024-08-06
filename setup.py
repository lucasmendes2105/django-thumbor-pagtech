# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='django-thumbor-pagtech',
    version='0.6.0.1',
    description=(
        'A django application to resize images using the thumbor service'),
    long_description=open('README.rst').read(),
    author=u'Lucas Mendes',
    author_email='lucasmendes2105@gmail.com',    
    license=(
        'django-thumbor is licensed under the MIT license. '
        'For more information, please see LICENSE file.'),
    classifiers=[
        'License :: OSI Approved :: MIT License',
    ],
    packages=[
        'django_thumbor_pagtech',
        'django_thumbor_pagtech.templatetags',
    ],
    install_requires=(
        'Django>=1.4',
        'libthumbor>=1.2.0',
    ),
    tests_require=(
        'django-nose',
        'mock',
    )
)
