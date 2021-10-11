from setuptools import find_packages, setup

VERSION = "0.1"


def read_requirements():
    req = []
    with open("requirements.txt") as requirements:
        for module in requirements.readlines():
            req.append(module.strip())
    return req


setup(
    name="data",
    packages=[
        package for package in find_packages() if package.startswith("data.models")
    ],
    install_requires=read_requirements(),
    zip_safe=False,
)
