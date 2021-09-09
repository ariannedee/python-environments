from package import package_func
from package.package_module import package_module_func as pmf
from package.subpackage import sub_module_func


def func():
    print('example 1 modules: ' + __name__)


if __name__ == '__main__':
    func()
    package_func()
    pmf()
    sub_module_func()

    import sys
    for path in sys.path:
        print(path)
