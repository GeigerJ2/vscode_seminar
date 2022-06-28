import os

import numpy as np
import pandas as pd
from ase import Atoms
from ase.visualize import view
ase vasp

from ase.io.vasp_parsers.vasp_outcar_parsers import Cell

# TODO: I should code more.
ugly_dict = {"a": 3, "b": 4, "c": 10}


class Human:
    def __init__(self):
        pass


########## ASE example ##########
my_lambda_expression = lambda x: x + 1


# Easy example
a = 4.05  # Gold lattice constant
b = a / 2
au_fcc = Atoms("Au", cell=[(0, b, b), (b, 0, b), (b, b, 0)], pbc=True)

mylist = [
    "x",
]


def show_structure(ase_object: Atoms):
    view(au_fcc)
    return None


########## Automatic code formatting with black ##########
# Stolen from yapf-GitHub: https://github.com/google/yapf

# x = {  'a':37,'b':42,

# 'c':926}

# y = 'hello ''word'
# z = 'hello '+'world'
# a = 'hello {}'.format('word')
# class foo  (     object  ):
#   def f    (self   ):
#     return       37*-+2
#   def g(self, x,y=42):
#       return y
# def f  (   a ) :
#   return      37+-+a[42-x :  y**3]
