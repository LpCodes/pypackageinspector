import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pypackageinspector",
    version="1.0.3",
    author="https://github.com/LpCodes",
    description="A Python package to inspect other Python packages.",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/LpCodes/pypackageinspector",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
