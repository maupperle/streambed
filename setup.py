from distutils.core import setup
from streambed import __version__

setup(
    name = 'streambed',
    packages = ['streambed','streambed/core','streambed/domain','streambed/tutorials','streambed/tutorials/exampleData'],
    version =  __version__,
    description = 'Model streambed grain size',
    author = 'Nathan Lyons',
    author_email = 'nathan.j.lyons@gmail.com',
    url = 'https://github.com/nathanlyons/streambed',
    download_url = 'https://github.com/nathanlyons/streambed/tarball/0.1',
    keywords = ['stream', 'sediment', 'grain'],
    classifiers = [],
)
