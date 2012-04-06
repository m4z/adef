from myobject import myobject
from numpy import sin, cos, pi, mgrid, zeros_like, ones_like

class Ellipsoid(myobject):
    def __init__(self, rx, ry, rz):
        myobject.__init__(self)
        ################################################################
        #parameter fuer die flaeche
        self.u_f, self.v_f = mgrid[0:pi:180j, 0:2*pi:180j]
        #alle funktionen fuer die flaeche
        self.x = lambda u, v: rx*cos(u)*sin(v)
        self.y = lambda u, v: ry*sin(u)*sin(v)
        self.z = lambda u, v: rz*cos(v)
        ################################################################
        #x,y,z sind die Koordinaten im dreidimensionalem euklidischen Raum
        #TODO: ueberlegung, ob ich die brauche oder x_f,y_f,z_f reichen
        #zeros_like = einfach die arraywerte in 0 umschreiben.
        #ones_like = einfach die arraywerte in 1 umschreiben.
        #dxu,dxv sind die Werte der ersten Patielenableitung
        self.dxu = lambda u, v: rx*(-sin(u))*sin(v)
        self.dxv = lambda u, v: rx*cos(u)*cos(v)
        
        self.dyu = lambda u, v: ry*cos(u)*sin(v)
        self.dyv = lambda u, v: ry*sin(u)*cos(v)
        
        self.dzu = lambda u, v: zeros_like(u)
        self.dzv = lambda u, v: rz*(-sin(v))
        
        self.dxuu = lambda u, v: rx*(-cos(u))*sin(v)
        self.dxvu = lambda u, v: rx*(-sin(u))*cos(v)
        self.dxuv = lambda u, v: rx*(-sin(u))*cos(v)
        self.dxvv = lambda u, v: rx*cos(u)*(-sin(v))
        
        self.dyuu = lambda u, v: ry*(-sin(u))*sin(v)
        self.dyvu = lambda u, v: ry*cos(u)*cos(v)
        self.dyuv = lambda u, v: ry*cos(u)*cos(v)
        self.dyvv = lambda u, v: ry*sin(u)*(-sin(v))
        
        self.dzuu = lambda u, v: zeros_like(u)
        self.dzvu = lambda u, v: zeros_like(u)
        self.dzuv = lambda u, v: zeros_like(v)
        self.dzvv = lambda u, v: rz*(-cos(v))
