# A dialog to edit a range interactively and propagate it to the filter
#
# W:  2: Unused import Float
# W:  2: Unused import Instance
# W:  2: Unused import Int
#from traits.api import HasTraits, Range, Button, Bool, Enum, Array, Float, \
#    Int, Instance, on_trait_change
from traits.api import HasTraits, Range, Button, Bool, Enum, Array, \
    on_trait_change
from traitsui.api import View, Item
from myutil import punkt
# W:  6: Unused import tckp_berechnen
#from calculation import tckp_berechnen#, flaeche_berechnen, x_f, y_f, z_f
from numpy import array
# is this needed here when it is already in main.py?
# W: 10: Unused import mlab
#try:
#    from enthought.mayavi import mlab
#except ImportError:
#    from mayavi import mlab
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
    """ A dialog to graphical adjust the extents of a filter.
    """
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

    # TODO: Skalierung
    Skalierung = Array(float, (1, 3), array([[1, 1, 1]]))
    # this ill-named variable holds the "calculate" button.
    Flaeche = Button('berechnen')
    # Data extents
    Kurvenpunkt = Range(0, 100, 0)
    # Kurve berechnen (calculate curvature)
    Kurve = Button('berechnen')
    #Buttons sollen einen style='button', 'radio', 'checkbox'
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


    def __init__(self, myobj):
        self.myobj = myobj
        HasTraits.__init__(self)

    # curve
    @on_trait_change('Kurve')
    def update_kurve(self):
        # eigentlich sollte ich hier wahrscheinlich die 100 kurvenpunkte
        # berechnen lassen und die dazugehoerigen daten, wie tangente, ...
        self.myobj.fig.children[2:] = []
        self.myobj.kurve_berechnen()

    # extent/surface
    @on_trait_change('Flaeche')
    def update_flaeche(self):
        #diese if-abfrage brauch ich spaeter um zu differenzieren welche
        #flaeche angezeigt werden soll.
        self.myobj.fig.children[0:] = []
        ###########################################
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
        ###########################################
        self.myobj.flaeche_berechnen()
        self.Flaeche_anzeigen = bool('true')
        self.Kurvenpunkt = 0


    # show surface
    @on_trait_change('Flaeche_anzeigen')
    def update_flaeche_anzeigen(self):
        self.myobj.mesh.set(visible=self.Flaeche_anzeigen)

    # triad/tripod
    @on_trait_change('Dreibein')
    def update_dreibein(self):
        self.myobj.tangente.set(visible=self.Dreibein)
        self.myobj.hauptnormale.set(visible=self.Dreibein)
        self.myobj.binormale.set(visible=self.Dreibein)

    # tangent
    @on_trait_change('Tangente')
    def update_tangente(self):
        self.myobj.tangente.set(visible=self.Tangente)

    # second deduction
    @on_trait_change('zweite_Ableitung')
    def update_ableitung2(self):
        self.myobj.ableitung2.set(visible=self.zweite_Ableitung)

    # main/principal normal
    @on_trait_change('Hauptnormale')
    def update_hauptnormale(self):
        self.myobj.hauptnormale.set(visible=self.Hauptnormale)

    # binormal
    @on_trait_change('Binormale')
    def update_binormale(self):
        self.myobj.binormale.set(visible=self.Binormale)

    @on_trait_change('Flaechen_Tangente_u')
    def update_tangente_fu(self):
        self.myobj.tangente_fu.set(visible=self.Flaechen_Tangente_u)

    @on_trait_change('Flaechen_Tangente_v')
    def update_tangente_fv(self):
        self.myobj.tangente_fv.set(visible=self.Flaechen_Tangente_v)

    @on_trait_change('Flaechen_Normale')
    def update_normale_f(self):
        self.myobj.normale_f.set(visible=self.Flaechen_Normale)

    # normal curvature
    @on_trait_change('Normalkruemmung')
    def update_normalkruemmung(self):
        self.myobj.normalkruemmung.set(visible=self.Normalkruemmung)

    # curvature
    @on_trait_change('Kruemmung')
    def update_kruemmung(self):
        self.myobj.kruemmung.set(visible=self.Kruemmung)

    # geodetic curvature
    @on_trait_change('geodaetische_Kruemmung')
    def update_geodaetischekruemmung(self):
        self.myobj.geodaetischekruemmung.set(
            visible=self.geodaetische_Kruemmung)

    # planes
    @on_trait_change('Ebenen')
    def update_ebenen(self):
        self.myobj.normalebene.set(visible=self.Ebenen)
        self.myobj.schmiegebene.set(visible=self.Ebenen)
        self.myobj.rektifizierendeebene.set(visible=self.Ebenen)
        self.myobj.tangentialebene_f.set(visible=self.Ebenen)

    # osculating plane
    @on_trait_change('Schmiegebene')
    def update_schmiegebene(self):
        self.myobj.schmiegebene.set(visible=self.Schmiegebene)

    @on_trait_change('Normalebene')
    def update_normalebene(self):
        self.myobj.normalebene.set(visible=self.Normalebene)

    # TODO rectifying plane?
    # (tangent + binormal + perpendicular to principal normal)
    @on_trait_change('rektifizierende_Ebene')
    def update_rektifizierende(self):
        self.myobj.rektifizierendeebene.set(
            visible=self.rektifizierende_Ebene)

    # tangent plane
    @on_trait_change('Tangentialebene')
    def update_tangentialebene(self):
        self.myobj.tangentialebene_f.set(visible=self.Tangentialebene)

    # plot-point on the curve
    @on_trait_change('Kurvenpunkt')
    def update_kurvenpunkt(self):
        punkt(self.myobj, self.Kurvenpunkt)

    #die bezeichnung der extra-gui.
    #die x_min, ... muessen anscheinend auch die variablennamen sein.
    view = View(Item(name='Flaechen',
                     label = 'Flaechen'),
                Item(name='Skalierung',
                     label='Skalierung x,y,z'),
                Item(name='Flaeche',
                     label='Flaeche'),
                Item(name='Flaeche_anzeigen',
                     label='Flaeche anzeigen'),
                '_',
                Item(name='Kurve'),
                Item(name='Dreibein'),
                Item(name='Tangente'),
                Item(name='zweite_Ableitung',
                     label='zweite Ableitung'),
                Item(name='Hauptnormale'),
                Item(name='Binormale'),
                Item(name='Flaechen_Tangente_u',
                     label='Flaechentangente u'),
                Item(name='Flaechen_Tangente_v',
                     label='Flaechentangente v'),
                Item(name='Flaechen_Normale',
                     label='Flaechennormale'),
                Item(name='Kruemmung',
                     label='Flaechenkruemmung'),
                Item(name='Normalkruemmung'),
                Item(name='geodaetische_Kruemmung',
                     label='geodaetische Kruemmung'),
                '_',
                Item(name='Ebenen'),
                Item(name='Schmiegebene'),
                Item(name='Normalebene'),
                Item(name='rektifizierende_Ebene',
                     label='rektifizierende Ebene'),
                Item(name='Tangentialebene',
                     label='Tangentialebene der Flaeche'),
                '_',
                'Kurvenpunkt',
                title='My GUI',
                resizable=True)
