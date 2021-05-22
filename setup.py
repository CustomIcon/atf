#!/usr/bin/env python
import setuptools
from atf import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="atf",
    version=__version__,
    description="Akagi Text Formatter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GNU Lesser General Public License v3 (LGPLv3)",
    author="Pokurt",
    author_email="poki@pokurt.me",
    url="https://github.com/pokurt/atf",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.6",
)