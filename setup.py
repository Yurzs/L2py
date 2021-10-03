from setuptools import find_packages, setup


def read_requirements():
    req = []
    with open("requirements.txt") as requirements:
        for module in requirements.readlines():
            req.append(module.strip())
    return req


setup(
    name="l2py",
    packages=find_packages(),
    install_requires=read_requirements(),
)
