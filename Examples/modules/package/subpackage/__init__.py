"""
Anything imported in __init__.py can be imported from the package

e.g. You can do:
from package.subpackage import sub_module_func

As well as the standard:
from package.subpackage.sub_module import sub_module_func
"""

from .sub_module import sub_module_func  # relative import
