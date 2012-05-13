#
# Create a set of points, with given density
#
# NumPy is the fundamental package for scientific computing with Python.
#import numpy as np
#from numpy import *
# TODO: get rid of the * import
#from numpy import ...

# mlab is/does TODO
#try:
#    from enthought.mayavi import mlab
#except ImportError:
#    from mayavi import mlab

# splprep: spline representation interpolation
# splev:   spline evaluation
from scipy.interpolate import splprep, splev

# extentDialog represents our adef GUI element
from extentDialog import ExtentDialog

# myutil (TODO rename adef.util or so) does/is TODO
from myutil import ebene, punkt

# TODO
# K,dKt,dKtt,normalisiere,kreuzprodukt
from calculation import *

# myobject does/is TODO
from myobject import myobject

# TODO: Certain (T)VTK versions contain a bug that results in this error
# on mayavi startup:
#     QWidget: Must construct a QApplication before a QPaintDevice
#     Aborted
#
# The fix found at https://github.com/enthought/mayavi/issues/24
# does not work on openSUSE 12.1/Tumbleweed.
myobj = myobject()

extent_dialog = ExtentDialog(myobj=myobj)
# We need to use 'edit_traits' and not 'configure_traits()' as we do
# not want to start the GUI event loop (the call to mlab.show())
# at the end of the script will do it.
extent_dialog.edit_traits()
