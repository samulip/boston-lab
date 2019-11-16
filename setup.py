from setuptools import setup, PEP420PackageFinder

setup(name='boston'
      , version='0.0.0'
      , package_dir={'': 'src'}
      , packages=PEP420PackageFinder.find("src")
      )
