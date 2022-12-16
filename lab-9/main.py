"""
Title: Modules & Imports

Task: Split your class topology into python package (several packages are preferred) and
    configure importing between them.

Note: it's recommended to add importing data in the `__init__.py` file.
"""
import topology.dependency as tdep
import topology.composition as tcom
import topology.association as tass
import topology.aggregation as tagg


if __name__ == '__main__':
    print(dir(tdep))
    print(dir(tcom))
    print(dir(tass))
    print(dir(tagg))

    print(locals())
