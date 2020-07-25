from setuptools import setup, find_packages


def read_requirements():
    req = []
    with open("requirements.txt") as requirements:
        for module in requirements.readlines():
            req.append(module.strip())


setup(name="l2py-server-login",
      packages=find_packages(),
      install_requires=read_requirements())
