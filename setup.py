# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2018 CERN.
# Copyright (C) 2017 RERO.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""REST API for invenio-records."""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()
history = open('CHANGES.rst').read()

tests_require = [
    'Flask-Login>=0.3.2',
    'invenio-config>=1.0.2',
    'invenio-db[all]>=1.0.9',
    'pytest-invenio>=1.4.0',
]

invenio_search_version = '1.4.2'

extras_require = {
    'elasticsearch5': [
        'invenio-search[elasticsearch5]>={}'.format(invenio_search_version),
    ],
    'elasticsearch6': [
        'invenio-search[elasticsearch6]>={}'.format(invenio_search_version),
    ],
    'elasticsearch7': [
        'invenio-search[elasticsearch7]>={}'.format(invenio_search_version),
    ],
    'citeproc': [
        'citeproc-py>=0.6.0',
        'citeproc-py-styles>=0.1.3',
    ],
    'datacite': [
        'datacite>=1.0.1',
    ],
    'docs': [
        'Sphinx>=4.2.0',
    ],
    'dublincore': [
        'dcxml>=0.1.2',
    ],
    'jsonld': [
        'pyld>=1.0.5,<2',
    ],
    'tests': tests_require,
}

extras_require['all'] = []
for name, reqs in extras_require.items():
    if name[0] == ':' or name in ('elasticsearch5',
                                  'elasticsearch6', 'elasticsearch7'):
        continue
    extras_require['all'].extend(reqs)

setup_requires = [
    'Babel>=2.8',
]

install_requires = [
    'bleach>=2.1.3',
    'ftfy>=4.4.3',
    'invenio-base>=1.2.5',
    'invenio-pidstore>=1.2.1',
    'invenio-records>=1.6.0',
    'invenio-rest>=1.2.4',
    'invenio-indexer>=1.2.0',
    'invenio-i18n>=1.3.0',
]

packages = find_packages()


# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('invenio_records_rest', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='invenio-records-rest',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + history,
    keywords='invenio api',
    license='MIT',
    author='CERN',
    author_email='info@inveniosoftware.org',
    url='https://github.com/inveniosoftware/invenio-records-rest',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'invenio_base.api_apps': [
            'invenio_records_rest = invenio_records_rest:InvenioRecordsREST',
        ],
        'invenio_base.converters': [
            'pid = invenio_records_rest.utils:PIDConverter',
            'pidpath = invenio_records_rest.utils:PIDPathConverter',
        ],
        'invenio_base.api_blueprints': [
            ('invenio_records_rest = '
             'invenio_records_rest.views:create_blueprint_from_app'),
        ],
        'invenio_base.api_converters': [
            'pid = invenio_records_rest.utils:PIDConverter',
            'pidpath = invenio_records_rest.utils:PIDPathConverter',
        ],
        'invenio_i18n.translations': [
            'messages = invenio_records_rest',
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Development Status :: 5 - Production/Stable',
    ],
)
