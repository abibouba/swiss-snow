from setuptools import setup, find_packages

VERSION = "0.1"

REQUIRES = ["requests >= 2.23.0", "beautifulsoup4>=4.9.1"]

setup(
    name="swiss-snow",
    version=VERSION,
    url="https://github.com/robmarkcole/London-tube-status",
    author="Sebastien Trosset",
    author_email="seb@trosset.net",
    description="Parse Swiss snow conditions from various websites",
    install_requires=REQUIRES,
    packages=find_packages(),
    license="Apache License, Version 2.0",
    python_requires=">=3.5",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)
