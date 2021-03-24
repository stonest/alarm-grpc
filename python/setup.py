from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="alarmgrpc",
    version="0.1.0",
    author="stonest",
    author_email="theking@beerfie.com",
    description="GRPC generated server and client code for the shower alarm.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pypi.fury.io/stonest/alarmgrpc",
    packages=find_packages(),
    install_requires=[
      'grpcio',
      'protobuf'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)