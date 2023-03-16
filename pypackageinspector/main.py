import importlib


def inspector(package):
    """
    Inspect a Python package and print out its functions and methods.

    Args:
        package (str): The name of the package to inspect.

    Returns:
        None
    """
    module = importlib.import_module(package)

    # get all functions and methods
    functions = [func for func in dir(module) if callable(getattr(module, func))]
    methods = [method for method in dir(module) if not callable(getattr(module, method))]

    # print functions
    print("Functions:")
    for i, func in enumerate(functions):
        print(f"{i}. " + func)

    # print methods
    print("\n\nMethods:")
    for i, method in enumerate(methods):
        print(f"{i}. " + method)
