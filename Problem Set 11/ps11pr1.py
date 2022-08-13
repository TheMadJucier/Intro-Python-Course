
# File: ps11pr1.py
# Author: Wadner Simon , 8/12/22
# Description: Creating Holiday Class

from ps9pr1 import Date

class Holiday(Date):
    """Creates objects for any holiday"""
    def __init__(self, month, day, year, name):
        """Constructor"""
        super().__init__(month, day, year)
        self.name = name


    def __repr__(self):
        """Reprints emthod"""
        return self.name + ' ' + '('+super().__repr__() + ')'
        



