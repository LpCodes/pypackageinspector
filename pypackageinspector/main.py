import importlib.util
from typing import List


def inspector(package: str, inspect_functions: bool = True, inspect_methods: bool = True) -> None:
    """
    Inspect a Python package and print out its functions and/or methods.

    Args:
        package (str): The name of the package to inspect.
        inspect_functions (bool): Whether to inspect functions (default True).
        inspect_methods (bool): Whether to inspect methods (default True).

    Returns:
        None
    """
    try:
        spec = importlib.util.find_spec(package)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    except (ImportError, AttributeError):
        print(f"Error: Package or module '{package}' not found.")
        return

    # get all functions and methods
    functions: List[str] = []
    methods: List[str] = []
    for name in dir(module):
        obj = getattr(module, name)
        if inspect_functions and callable(obj):
            functions.append(name)
        elif inspect_methods and not callable(obj):
            methods.append(name)

    # print functions
    if inspect_functions and functions:
        print("\n" + "=" * 20 + " Functions " + "=" * 20)
        for i, func in enumerate(functions):
            print(f"{i + 1}. {func}")

    # print methods
    if inspect_methods and methods:
        print("\n" + "=" * 20 + " Methods " + "=" * 20)
        for i, method in enumerate(methods):
            print(f"{i + 1}. {method}")



