# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
LICENSE = open(os.path.join(here, 'LICENSE')).read()

# rm -rf *.egg-info dist/* && python setup.py sdist
# pip install dist/restructuredWeb-0.1.0.tar.gz
# twine upload --repository pypi dist/*
# twine upload --repository pypitest dist/*
setup(
    name='restructuredWeb',
    version='1.0.0',
    description="Web directives for use with Sphinx.",
    keywords=['sphinx', 'bootstrap', 'restructuredText'],
    author='Anil Lakhman',
    author_email='restructured.web@anil.io',
    url='https://github.com/lakhman/restructuredWeb',
    long_description=README,
    license=LICENSE,
    packages=find_packages('.', exclude=['tests']),
    data_files=[("", ["LICENSE"])],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools', 'Sphinx >= 1.4', 'six'],
    entry_points={},
    test_suite='tests',
    tests_require=['sphinx-testing'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Documentation',
        'Topic :: Text Processing',
        'Topic :: Software Development :: Documentation',
        'Framework :: Sphinx',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
