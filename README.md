[![Publish Package](https://github.com/LpCodes/pypackageinspector/actions/workflows/python-publish.yml/badge.svg)](https://github.com/LpCodes/pypackageinspector/actions/workflows/python-publish.yml)
# pypackageinspector

pyCryptobox is a package in Python that inspects a Python package and prints out all the functions and methods defined in that package. It takes a single argument, package, which is a string representing the name of the package to be inspected.
This can be useful in situations where you want to explore the functionality of a package before deciding whether or not to use it in your project, or when you need to quickly get a sense of what functions and methods are available in a package.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pypackageinspector.

```bash
pip install pypackageinspector
```

## Sample Usage

```python
from pypackageinspector import inspector

# add package name as the arg you want to check
inspector('math')


```

This will inspect the math package and print out all the functions and methods defined in that package. The output might look something like this

```python
Functions:
0. acos
1. acosh
2. asin
3. asinh
4. atan
5. atan2
6. atanh
7. ceil
8. comb
9. copysign
10. cos
11. cosh
12. degrees
13. dist

...

Methods:
0. __doc__
1. __file__
2. __loader__
3. __name__
4. __package__
5. __spec__


```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
