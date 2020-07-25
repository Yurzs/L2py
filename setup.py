from setuptools import setup, find_packages


setup(name="l2py-server-login",
      packages=find_packages(),
      install_requires=[
            "l2py-server-common @ https://l2py@bitbucket.org/l2py/l2py-server-common.git"])
