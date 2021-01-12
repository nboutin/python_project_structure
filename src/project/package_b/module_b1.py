'''
Created on 12 janv. 2021

@author: F24178C
'''

# Aboslute import: start at top-level package and walks down into package_a
from project.package_a.module_a1 import ModuleA1

# Relative import: '..' means this package parent
# from ..package_a.module_a1 import ModuleA1

# Relative import: '.' means this package
from .module_b2 import ModuleB2


class ModuleB1:

    def __init__(self):
        print('module B1')
        _ = ModuleA1()
        _ = ModuleB2()
