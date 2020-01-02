import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MLDToolkit", 
    version="0.0.8",
    author="Matthew Zorumski", 
    author_email="mattzor@cox.net",
    description="A text analysis tool.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jorymorrison/MLD",
    license='Apache License 2.0',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
