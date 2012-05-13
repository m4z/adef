# -*- coding: utf-8 -*-
#
# Adjusted from https://github.com/enthought/mayavi/ \
#         blob/master/examples/mayavi/interactive/adjust_cropping_extents.py

from numpy import array

#
# HasTraits: Enables any Python class derived from it to have trait
#     attributes.
# Array, Bool, Enum, Range: Returns a trait (event) whose value must be...
#   a numpy array; a Boolean; one of an enumerated list; in a specified range.
# Button: Returns a trait event whose editor is a button.
# on_trait_change: TODO decorator
from traits.api import HasTraits, Range, Button, Bool, Enum, Array, \
    on_trait_change
#
# View: A Traits-based user interface for one or more objects.
# The attributes of the View object determine the contents and layout of an
# attribute-editing window. A View object contains a set of Group, Item, and
# Include objects. A View object can be an attribute of an object derived from
# HasTraits, or it can be a standalone object.
#
# Item: An element in a Traits-based user interface.
from traitsui.api import View, Item

from myutil import punkt
#
# the default adef curvature shapes
from parabolischer_Zylinder import parabolischer_Zylinder
from elliptischer_Zylinder import elliptischer_Zylinder
from hyperbolischer_Zylinder import hyperbolischer_Zylinder
from elliptisches_Paraboloid import elliptisches_Paraboloid
from hyperbolisches_Paraboloid import hyperbolisches_Paraboloid
from elliptischer_Kegel import elliptischer_Kegel
from Ellipsoid import Ellipsoid
from einschaliges_Hyperboloid import einschaliges_Hyperboloid
from zweischaliges_Hyperboloid import zweischaliges_Hyperboloid
from Torus import Torus

class ExtentDialog(HasTraits):
    """ A dialog to graphically adjust the extents of a filter.
    """
    #
    # extents/surfaces (unsure about correct translation).
    # this variable holds the user-selected extent.
    Flaechen = Enum('parabolischer Zylinder',
                    'elliptischer Zylinder',
                    'hyperbolischer Zylinder',
                    'elliptisches Paraboloid',
                    'hyperbolisches Paraboloid',
                    'elliptischer Kegel',
                    'Ellipsoid',
                    'einschaliges Hyperboloid',
                    'zweischaliges Hyperboloid',
                    'Torus',)
    #
    # TODO: Skalierung
    # Array(dtype = None, shape = None, value = None, **metadata)
    Skalierung = Array(float, (1, 3), array([[1, 1, 1]]))
    #
    # this ill-named variable holds the "calculate extents" button.
    Flaeche = Button('berechnen')
    #
    # button to calculate curvature
    Kurve = Button('berechnen')
    #
    # Buttons sollen einen style='button', 'radio', 'checkbox' ...haben?
    # all the boolean options.
    Flaeche_anzeigen = Bool()
    Dreibein = Bool()
    Tangente = Bool()
    zweite_Ableitung = Bool()
    Hauptnormale = Bool()
    Binormale = Bool()
    Flaechen_Tangente_u = Bool()
    Flaechen_Tangente_v = Bool()
    Flaechen_Normale = Bool()
    Normalkruemmung = Bool()
    Kruemmung = Bool()
    geodaetische_Kruemmung = Bool()
    Ebenen = Bool()
    Normalebene = Bool()
    Schmiegebene = Bool()
    rektifizierende_Ebene = Bool()
    Tangentialebene = Bool()
    #
    # Data extents (low, high, initial value)
    Kurvenpunkt = Range(0, 100, 0)

    def __init__(self, myobj):
        self.myobj = myobj
        HasTraits.__init__(self)

    # curve
    @on_trait_change('Kurve')
    def update_kurve(self):
        if self.Flaechen == 'parabolischer Zylinder' or \
           self.Flaechen == 'hyperbolisches Paraboloid':
            print "Warning: Curve calculation will fail with this extent!"
        # eigentlich sollte ich hier wahrscheinlich die 100 kurvenpunkte
        # berechnen lassen und die dazugehoerigen daten, wie tangente, ...
        #
        # if the curve button is pressed, do TODO and show the curve.
        self.myobj.fig.children[2:] = []
        self.myobj.kurve_berechnen()

    # extent/surface
    @on_trait_change('Flaeche')
    def update_flaeche(self):
        #diese if-abfrage brauch ich spaeter um zu differenzieren welche
        #flaeche angezeigt werden soll.
        #
        # if the extent button is pressed, do TODO and show the extent.
        self.myobj.fig.children[0:] = []
        ###########################################
        # TODO there must be a way to "switch" or so on this.
        if self.Flaechen == 'parabolischer Zylinder':
            self.myobj = parabolischer_Zylinder(self.Skalierung[0][0],
                                                self.Skalierung[0][1],
                                                self.Skalierung[0][2])
        elif self.Flaechen == 'elliptischer Zylinder':
            self.myobj = elliptischer_Zylinder(self.Skalierung[0][0],
                                               self.Skalierung[0][1],
                                               self.Skalierung[0][2])
        elif self.Flaechen == 'hyperbolischer Zylinder':
            self.myobj = hyperbolischer_Zylinder(self.Skalierung[0][0],
                                                 self.Skalierung[0][1],
                                                 self.Skalierung[0][2])
        elif self.Flaechen == 'elliptisches Paraboloid':
            self.myobj = elliptisches_Paraboloid(self.Skalierung[0][0],
                                                 self.Skalierung[0][1],
                                                 self.Skalierung[0][2])
        elif self.Flaechen == 'hyperbolisches Paraboloid':
            self.myobj = hyperbolisches_Paraboloid(self.Skalierung[0][0],
                                                   self.Skalierung[0][1],
                                                   self.Skalierung[0][2])
        elif self.Flaechen == 'elliptischer Kegel':
            self.myobj = elliptischer_Kegel(self.Skalierung[0][0],
                                            self.Skalierung[0][1],
                                            self.Skalierung[0][2])
        elif self.Flaechen == 'Ellipsoid':
            self.myobj = Ellipsoid(self.Skalierung[0][0],
                                   self.Skalierung[0][1],
                                   self.Skalierung[0][2])
        elif self.Flaechen == 'einschaliges Hyperboloid':
            self.myobj = einschaliges_Hyperboloid(self.Skalierung[0][0],
                                                  self.Skalierung[0][1],
                                                  self.Skalierung[0][2])
        elif self.Flaechen == 'zweischaliges Hyperboloid':
            self.myobj = zweischaliges_Hyperboloid(self.Skalierung[0][0],
                                                   self.Skalierung[0][1],
                                                   self.Skalierung[0][2])
        elif self.Flaechen == 'Torus':
            self.myobj = Torus(self.Skalierung[0][0],
                               self.Skalierung[0][1],
                               self.Skalierung[0][2])
        else:
            print "Warning: Something wrong with Flaechen, value=%s" % \
                    self.Flaechen
        ###########################################
        self.myobj.flaeche_berechnen()
        self.Flaeche_anzeigen = bool('true')
        self.Kurvenpunkt = 0


    # show or hide surface.
    @on_trait_change('Flaeche_anzeigen')
    def update_flaeche_anzeigen(self):
        self.myobj.mesh.set(visible=self.Flaeche_anzeigen)

    # show or hide triad/tripod.
    @on_trait_change('Dreibein')
    def update_dreibein(self):
        self.myobj.tangente.set(visible=self.Dreibein)
        self.myobj.hauptnormale.set(visible=self.Dreibein)
        self.myobj.binormale.set(visible=self.Dreibein)

    # show or hide tangent.
    @on_trait_change('Tangente')
    def update_tangente(self):
        self.myobj.tangente.set(visible=self.Tangente)

    # show or hide second deduction.
    @on_trait_change('zweite_Ableitung')
    def update_ableitung2(self):
        self.myobj.ableitung2.set(visible=self.zweite_Ableitung)

    # show or hide main/principal normal.
    @on_trait_change('Hauptnormale')
    def update_hauptnormale(self):
        self.myobj.hauptnormale.set(visible=self.Hauptnormale)

    # show or hide binormal.
    @on_trait_change('Binormale')
    def update_binormale(self):
        self.myobj.binormale.set(visible=self.Binormale)

    # show or hide tangent u.
    @on_trait_change('Flaechen_Tangente_u')
    def update_tangente_fu(self):
        self.myobj.tangente_fu.set(visible=self.Flaechen_Tangente_u)

    # show or hide tangent v.
    @on_trait_change('Flaechen_Tangente_v')
    def update_tangente_fv(self):
        self.myobj.tangente_fv.set(visible=self.Flaechen_Tangente_v)

    # show or hide extent normal.
    @on_trait_change('Flaechen_Normale')
    def update_normale_f(self):
        self.myobj.normale_f.set(visible=self.Flaechen_Normale)

    # show or hide normal curvature.
    @on_trait_change('Normalkruemmung')
    def update_normalkruemmung(self):
        self.myobj.normalkruemmung.set(visible=self.Normalkruemmung)

    # show or hide curvature.
    @on_trait_change('Kruemmung')
    def update_kruemmung(self):
        self.myobj.kruemmung.set(visible=self.Kruemmung)

    # show or hide geodetic curvature.
    @on_trait_change('geodaetische_Kruemmung')
    def update_geodaetischekruemmung(self):
        self.myobj.geodaetischekruemmung.set(
            visible=self.geodaetische_Kruemmung)

    # show or hide planes.
    @on_trait_change('Ebenen')
    def update_ebenen(self):
        self.myobj.normalebene.set(visible=self.Ebenen)
        self.myobj.schmiegebene.set(visible=self.Ebenen)
        self.myobj.rektifizierendeebene.set(visible=self.Ebenen)
        self.myobj.tangentialebene_f.set(visible=self.Ebenen)

    # show or hide osculating plane.
    @on_trait_change('Schmiegebene')
    def update_schmiegebene(self):
        self.myobj.schmiegebene.set(visible=self.Schmiegebene)

    # show or hide normal plane.
    @on_trait_change('Normalebene')
    def update_normalebene(self):
        self.myobj.normalebene.set(visible=self.Normalebene)

    # show or hide TODO:rectifying? plane.
    # (tangent + binormal + perpendicular to principal normal)
    @on_trait_change('rektifizierende_Ebene')
    def update_rektifizierende(self):
        self.myobj.rektifizierendeebene.set(
            visible=self.rektifizierende_Ebene)

    # show or hide tangent plane.
    @on_trait_change('Tangentialebene')
    def update_tangentialebene(self):
        self.myobj.tangentialebene_f.set(visible=self.Tangentialebene)

    # change the selected plot-point on the curve.
    @on_trait_change('Kurvenpunkt')
    def update_kurvenpunkt(self):
        # TODO find a better way to deal with this.
        if self.Kurvenpunkt is not None:
            punkt(self.myobj, self.Kurvenpunkt)
        else:
            print "Warning: Kurvenpunkt is None."

    #die bezeichnung der extra-gui.
    #die x_min, ... muessen anscheinend auch die variablennamen sein.
    view = View(Item(name='Flaechen',
                     label = 'Flächen'),
                Item(name='Skalierung',
                     label='Skalierung x,y,z'),
                Item(name='Flaeche',
                     label='Fläche'),
                Item(name='Flaeche_anzeigen',
                     label='Fläche anzeigen'),
                '_',
                Item(name='Kurve'),
                Item(name='Dreibein'),
                Item(name='Tangente'),
                Item(name='zweite_Ableitung',
                     label='zweite Ableitung'),
                Item(name='Hauptnormale'),
                Item(name='Binormale'),
                Item(name='Flaechen_Tangente_u',
                     label='Flächentangente u'),
                Item(name='Flaechen_Tangente_v',
                     label='Flächentangente v'),
                Item(name='Flaechen_Normale',
                     label='Flächennormale'),
                Item(name='Kruemmung',
                     label='Flächenkrümmung'),
                Item(name='Normalkruemmung',
                     label='Normalkrümmung'),
                Item(name='geodaetische_Kruemmung',
                     label='geodätische Krümmung'),
                '_',
                Item(name='Ebenen'),
                Item(name='Schmiegebene'),
                Item(name='Normalebene'),
                Item(name='rektifizierende_Ebene',
                     label='rektifizierende Ebene'),
                Item(name='Tangentialebene',
                     label='Tangentialebene der Fläche'),
                '_',
                'Kurvenpunkt',
                title='My GUI',
                resizable=True,)
