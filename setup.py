from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Online Product Recommender",
    version="0.1",
    author="Cheng Hou",
    packages=find_packages(),
    install_requires = requirements,
)