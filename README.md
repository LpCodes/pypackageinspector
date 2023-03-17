[![Publish Package](https://github.com/LpCodes/pypackageinspector/actions/workflows/python-publish.yml/badge.svg)](https://github.com/LpCodes/pypackageinspector/actions/workflows/python-publish.yml) ![PyPI](https://img.shields.io/pypi/v/pypackageinspector)[![Downloads](https://static.pepy.tech/personalized-badge/pypackageinspector?period=total&units=none&left_color=black&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/pypackageinspector)
# pypackageinspector

pypackageinspector is a package in Python that inspects a given package and prints out all the functions and methods defined in that package. It takes a single argument, package, which is a string representing the name of the package to be inspected.
This can be useful in situations where you want to explore the functionality of a package before deciding whether or not to use it in your project, or when you need to quickly get a sense of what functions and methods are available in a package.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pypackageinspector.

```bash
pip install pypackageinspector
```

## Sample Usage

Here's an example of how to call the inspector() function:
```python
from pypackageinspector import inspector

inspector('numpy', inspect_functions=True, inspect_methods=False)

```

In this example, we're inspecting the "numpy" package and setting inspect_functions=True and inspect_methods=False, so the output will only include the list of functions in the package.

If we want to inspect both functions and methods, we can call the inspector() function like this:

```python
inspector('numpy', inspect_functions=True, inspect_methods=True)


```
 Here's an example of the output when we call the inspector() function with inspect_functions=True and inspect_methods=False for the "numpy" package:
```Functions:
0. AxisError
1. DataSource
2. MatrixPowerOperator
3. VisibleDeprecationWarning
4. add_docstring
5. add_newdoc
6. add_newdoc_ufunc
7. add_newdocs
8. arange
9. array
10. array2string
11. array_equal
12. array_equiv
13. array_repr
14. array_split
15. array_str
16. asanyarray
17. asarray
18. asarray_chkfinite
19. ascontiguousarray
20. asfarray
21. asfortranarray
22. broadcast
23. broadcast_arrays
24. broadcast_to
25. busday_count
26. busday_offset
27. busdaycalendar
28. byte_bounds
29. c_
30. can_cast
31. choose
32. column_stack
33. common_type
34. compare_chararrays
35. complex128
36. complex256
37. complex64
38. complex_
39. concatenate
40. core
41. correlate
42. corrcoef
43. count_nonzero
44. datetime64
45. datetime_as_string
46. delete
47. deprecate
48. diag
49. diag_indices
50. diag_indices_from
51. diagonal
52. disp
53. division
54. dot
55. double
56. dual
57. dtype
58. e
59. einsum
60. einsum_path
61. einsumfunc
62. empty
63. empty_like
64. equal
65. errstate
66. euler_gamma
67. expand_dims
68. extract

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
