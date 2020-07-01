from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="alarm_grpc",
    version="0.0.1",
    author="stonest",
    author_email="theking@beerfie.com",
    description="A server that stores alarm data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pypi.fury.io/stonest/alarm_grpc",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)