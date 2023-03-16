import importlib.util


def inspector(package, inspect_functions=True, inspect_methods=True):
    """
    Inspect a Python package and print out its functions and/or methods.

    Args:
        package (str): The name of the package to inspect.
        inspect_functions (bool): Whether to inspect functions (default True).
        inspect_methods (bool): Whether to inspect methods (default True).

    Returns:
        None
    """
    spec = importlib.util.find_spec(package)

    if spec is None:
        print(f"Error: Package or module '{package}' not found.")
        return

    module = importlib.import_module(package)

    # get all functions and methods
    functions = []
    methods = []
    if inspect_functions:
        functions = [func for func in dir(module) if callable(getattr(module, func))]
    if inspect_methods:
        methods = [method for method in dir(module) if not callable(getattr(module, method))]

    # print functions
    if inspect_functions:
        print("Functions:")
        for i, func in enumerate(functions):
            print(f"{i}. {func}")

    # print methods
    if inspect_methods:
        if inspect_functions:
            print("\nMethods:")
        else:
            print("Methods:")
        for i, method in enumerate(methods):
            print(f"{i}. {method}")


