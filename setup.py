"""genie package setup"""
import os
from setuptools import setup, find_packages
import shutil

# figure out the version
about = {}
here = os.path.abspath(os.path.dirname(__file__))
# with open(os.path.join(here, "synapsegenie", "__version__.py")) as f:
#     exec(f.read(), about)

# Add readme
with open("README.md", "r") as fh:
    long_description = fh.read()

# Must install bftools in the root directory of this repo
command = os.path.join(here, 'bftools/xmlvalid')
if shutil.which(command) is None:
    raise ValueError("Must install bftools in the root directory of this repo")

# Must have libtiff-tools installed
if shutil.which('tiffinfo') is None:
    raise ValueError("Must install libtiff-tools to use tiffinfo: sudo apt install libtiff-tools")

setup(name='htan-registry',
      # version=about["__version__"],
      description='synapsegenie example registry',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/Sage-Bionetworks/synapsegenie-htan-registry',
      author='Thomas Yu',
      author_email='thomas.yu@sagebionetworks.org',
      license='Apache2',
      packages=find_packages(),
      zip_safe=False,
      python_requires='>=3.6',
      install_requires=['synapsegenie==0.0.2', 'pandas>=1.0', 'synapseclient>=2.2.2'])
