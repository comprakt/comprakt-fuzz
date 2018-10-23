import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="comprakt-fuzz",
    version="0.0.1",
    author="flip1995",
    author_email="hello@philkrones.com",
    description="A fuzzer for the MiniJava language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/comprakt/comprakt-fuzz",
    packages=setuptools.find_packages(),
    install_requires=[
        'gramfuzz',
    ],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
