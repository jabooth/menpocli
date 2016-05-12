import sys
from os.path import join
from setuptools import setup
import versioneer

# note that we don't explicitly version numpy,
# let menpo handle that
install_requires = [
    'docopt>=0.6,<0.7',
    'pyyaml>=3.0,<4.0',
    'menpofit>=0.4,<0.5',
    'menpodetect>=0.4,<0.5',
    'numpy'
]

if sys.version_info.major == 2:
    install_requires.append('pathlib==1.0')

setup(name='menpocli',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='A command line interface to the Menpo Project',
      author='James Booth',
      author_email='james.booth08@imperial.ac.uk',
      packages=['menpocli'],
      scripts=[join('bin', 'menpofit'),
               join('bin', 'menpodetect')],
      install_requires=install_requires
      )
