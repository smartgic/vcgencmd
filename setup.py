import sys

try:
    from setuptools import setup, find_packages
except Exception:
    print("please install setuptools using pip:")
    print("    <pip> install setuptools")
    sys.exit(-1)

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="vcgencmd2",
    version="1.0.0",
    description="Python binding for RaspberryPi vcgencmd command-line tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Sushant Nadkar",
    license="The MIT License (MIT)",
    url="https://github.com/smartgic/vcgencmd2",
    packages=find_packages(),
    scripts=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
