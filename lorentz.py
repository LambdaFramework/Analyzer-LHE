#! /usr/bin/env python

import ROOT

def lorentz():

    p= ROOT.TLorentzVector(1,2,3,5)
    print "legth of p (= Mass): "+str( p.Mag() )
    print "Angle of phi (in rad): "+str( p.Phi() )
    print "Angle of theta (in rad): "+str( p.Theta() )
    p3 = p.Vect()
    print "Magnitude of momentum "+str( p3.Mag() )
    print "E: "+str( p.E() )
    print "p_x: "+str( p.X() )
    print "p_y: "+str( p.Y() )
    print "p_z: "+str( p.Z() )
    beta = 0.95
    p.Boost(0, 0, beta)
    print "Masse after Boost: "+str( p.Mag() )
    print "E after Boost: "+str( p.E() )
    print "p_x after Boost: "+str( p.X() )
    print "p_y after Boost: "+str( p.Y() )
    print "p_z after Boost: "+str( p.Z() )
    p1 = ROOT.TLorentzVector(3, 2, 1, 5)
    print "Invariant Mass of two Particles "+str( (p+p1).Mag() )
pass

lorentz();
