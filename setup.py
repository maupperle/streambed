from distutils.core import setup
from setuptools.command.develop import develop
from streambed import __version__

class developer_install(develop):
    def run(self):
        develop.run(self)

setup(
    name = 'streambed',
    packages = ['streambed','streambed/core','streambed/domain','tutorials','tutorials/exampleData'],
    version =  __version__,
    description = 'Model streambed grain size',
    author = 'Nathan Lyons',
    author_email = 'nathan.j.lyons@gmail.com',
    url = 'https://github.com/nathanlyons/streambed',
    download_url = 'https://github.com/nathanlyons/streambed/tarball/0.3',
    keywords = ['stream', 'sediment', 'grain'],
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Physics',
        'Intended Audience :: Science/Research'
        ],
    cmdclass = {'develop': developer_install},
)
