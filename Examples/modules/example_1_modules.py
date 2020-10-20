from package import package_func
from package.package_module import package_module_func as pmc
from package.subpackage import sub_module_func


def func():
    print('example 1 modules: ' + __name__)


if __name__ == '__main__':
    func()
    package_func()
    pmc()
    sub_module_func()

    import sys
    print(sys.path)  # Python searches for modules here (in-order)
