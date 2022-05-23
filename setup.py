"""genie package setup"""
import os
from setuptools import setup, find_packages

# figure out the version
about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "synapsegenie", "__version__.py")) as f:
    exec(f.read(), about)

# Add readme
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='synapsegenie-example-registry',
      version=about["__version__"],
      description='synapsegenie example registry',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/Sage-Bionetworks/synapsegenie-example-registry',
      author='Thomas Yu',
      author_email='thomas.yu@sagebionetworks.org',
      license='Apache2',
      packages=find_packages(),
      zip_safe=False,
      python_requires='>=3.6',
      install_requires=['pandas>=1.0', 'synapseclient>=2.2.2'])
