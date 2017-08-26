import os
from setuptools import setup, find_packages
from pip.req import parse_requirements


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

install_reqs = parse_requirements('requirements.txt', session=False)
reqs = [str(ir.req) for ir in install_reqs]

setup(name="PyMC3 Models",
      version="2016.11.9",
      author="Eric J. Ma",
      author_email="ericmajinglong@gmail.com",
      description=("Default models for use with PyMC3"),
      license="MIT",
      keywords="network visualization, matplotlib, circos",
      url="http://github.com/ericmjl/pymc3-models",
      packages=find_packages(),
      package_data={'': ['README.md']},
      install_requires=reqs,
      long_description=read('README.md'),
      classifiers=["Topic :: Scientific/Engineering :: Visualization"],
      )
