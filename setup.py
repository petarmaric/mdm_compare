import ez_setup
ez_setup.use_setuptools()

import sys
from setuptools import setup

import mdm_compare


if sys.version_info < (2, 6):
    print 'ERROR: mdm_compare requires at least Python 2.6 to run.'
    sys.exit(1)


setup(
    name='mdm_compare',
    version=mdm_compare.__version__,
    url='https://bitbucket.org/petar/mdm_compare',
    download_url='https://bitbucket.org/petar/mdm_compare',
    license='BSD',
    author='Petar Maric',
    author_email='petarmaric@uns.ac.rs',
    description=open('README').read(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    platforms='any',
    py_modules=['mdm_compare'],
    entry_points={
        'console_scripts': ['mdm_compare=mdm_compare:main']
    },
    install_requires=open('requirements.txt').read().splitlines()
)