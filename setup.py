"""Packaging settings."""

from codecs import open
from os.path import abspath, dirname, join
from subprocess import call
from setuptools import Command, find_packages, setup

this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

with open(join(this_dir, 'requirements.txt'), encoding='utf-8') as fp:
    install_requires = fp.read()


class RunTests(Command):
    """Run all tests."""
    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(['py.test', '--cov=bql', '--cov-report=term-missing'])
        raise SystemExit(errno)


setup(
    name='bql',
    version="0.1.0",
    description='BiznetGIO Query Language',
    long_description=long_description,
    url='https://github.com/BiznetGIO',
    author='BiznetGio',
    author_email='support@biznetgio.com',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development'
    ],
    keywords='cli',
    include_package_data=True,
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=install_requires,
    extras_require={
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    # entry_points={
    #     'console_scripts': [
    #         'bql=bql.cli:main',
    #     ],
    # },
    cmdclass={'test': RunTests},
)