# is this needed here when it is already in main.py?
try:
    from enthought.mayavi import mlab
except ImportError:
    from mayavi import mlab
from numpy import array

def ebene(x, y, z, u1, v1, w1, u2, v2, w2, rgb, ii, myname):
    px1, py1, pz1 = [u1[ii]+u2[ii]+x[ii], x[ii]], \
                    [v1[ii]+v2[ii]+y[ii], y[ii]], \
                    [w1[ii]+w2[ii]+z[ii], z[ii]]
    px2, py2, pz2 = [u1[ii]-u2[ii]+x[ii], x[ii]], \
                    [v1[ii]-v2[ii]+y[ii], y[ii]], \
                    [w1[ii]-w2[ii]+z[ii], z[ii]]
    px3, py3, pz3 = [-u1[ii]-u2[ii]+x[ii], x[ii]], \
                    [-v1[ii]-v2[ii]+y[ii], y[ii]], \
                    [-w1[ii]-w2[ii]+z[ii], z[ii]]
    px4, py4, pz4 = [-u1[ii]+u2[ii]+x[ii], x[ii]], \
                    [-v1[ii]+v2[ii]+y[ii], y[ii]], \
                    [-w1[ii]+w2[ii]+z[ii], z[ii]]
    px = array([px1, px2, px3, px4, px1])
    py = array([py1, py2, py3, py4, py1])
    pz = array([pz1, pz2, pz3, pz4, pz1])
    return mlab.mesh(px, py, pz, color=rgb, opacity=0.5, name=myname)

def punkt(myobj, ii):
    #Alle Vektoren
    myobj.tangente.mlab_source.set(x=myobj.xnew[ii],
                                   y=myobj.ynew[ii],
                                   z=myobj.znew[ii],
                                   u=myobj.a_n[ii],
                                   v=myobj.b_n[ii],
                                   w=myobj.c_n[ii])
    myobj.ableitung2.mlab_source.set(x=myobj.xnew[ii],
                                     y=myobj.ynew[ii],
                                     z=myobj.znew[ii],
                                     u=myobj.d_n[ii],
                                     v=myobj.e_n[ii],
                                     w=myobj.f_n[ii])
    myobj.hauptnormale.mlab_source.set(x=myobj.xnew[ii],
                                       y=myobj.ynew[ii],
                                       z=myobj.znew[ii],
                                       u=myobj.j_n[ii],
                                       v=myobj.k_n[ii],
                                       w=myobj.l_n[ii])
    myobj.binormale.mlab_source.set(x=myobj.xnew[ii],
                                    y=myobj.ynew[ii],
                                    z=myobj.znew[ii],
                                    u=myobj.g_n[ii],
                                    v=myobj.h_n[ii],
                                    w=myobj.i_n[ii])
    myobj.tangente_fu.mlab_source.set(x=myobj.xnew[ii],
                                      y=myobj.ynew[ii],
                                      z=myobj.znew[ii],
                                      u=myobj.u1_n[ii],
                                      v=myobj.u2_n[ii],
                                      w=myobj.u3_n[ii])
    myobj.tangente_fv.mlab_source.set(x=myobj.xnew[ii],
                                      y=myobj.ynew[ii],
                                      z=myobj.znew[ii],
                                      u=myobj.v1_n[ii],
                                      v=myobj.v2_n[ii],
                                      w=myobj.v3_n[ii])
    myobj.normale_f.mlab_source.set(x=myobj.xnew[ii],
                                    y=myobj.ynew[ii],
                                    z=myobj.znew[ii],
                                    u=myobj.uv1_n[ii],
                                    v=myobj.uv2_n[ii],
                                    w=myobj.uv3_n[ii])
    myobj.normalkruemmung.mlab_source.set(x=myobj.xnew[ii],
                                          y=myobj.ynew[ii],
                                          z=myobj.znew[ii],
                                          u=myobj.kn_nf[0][ii],
                                          v=myobj.kn_nf[1][ii],
                                          w=myobj.kn_nf[2][ii],
                                          scale_factor=myobj.k_nf[ii])
    myobj.geodaetischekruemmung.mlab_source.set(x=myobj.xnew[ii],
                                                y=myobj.ynew[ii],
                                                z=myobj.znew[ii],
                                                u=myobj.kg[0][ii],
                                                v=myobj.kg[1][ii],
                                                w=myobj.kg[2][ii])
    #Alle Ebenen
    #pxn[..., 0] = pxn[:, :, 0] = pxn.T[0].T
    myobj.normalebene.mlab_source.set(x=myobj.epxn[..., ii],
                                      y=myobj.epyn[..., ii],
                                      z=myobj.epzn[..., ii])
    myobj.schmiegebene.mlab_source.set(x=myobj.epxs[..., ii],
                                       y=myobj.epys[..., ii],
                                       z=myobj.epzs[..., ii])
    myobj.rektifizierendeebene.mlab_source.set(x=myobj.epxr[..., ii],
                                               y=myobj.epyr[..., ii],
                                               z=myobj.epzr[..., ii])
    myobj.tangentialebene_f.mlab_source.set(x=myobj.epxt[..., ii],
                                            y=myobj.epyt[..., ii],
                                            z=myobj.epzt[..., ii])
