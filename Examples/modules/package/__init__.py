print("Package imported")


def package_func():
    print('package init: ' + __name__)


if __name__ == '__main__':
    package_func()
