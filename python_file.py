import os

import numpy as np
import pandas as pd
from ase import Atoms
from ase.visualize import view

from ase.io.vasp_parsers.vasp_outcar_parsers import Cell

df = pd.DataFrame()


class Human:
    def __init__():
        pass


human = Human()

########## ASE example ##########

# Easy example
a = 4.05  # Gold lattice constant
b = a / 2
au_fcc = Atoms("Au", cell=[(0, b, b), (b, 0, b), (b, b, 0)], pbc=True)


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
