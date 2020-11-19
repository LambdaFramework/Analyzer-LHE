import os
from drawer import *
from tdrstyle import *

NORM2AU=False
 
Lhefiles=[ 'hwplus_ss_012j.root' , 'hwminus_ss_012j.root' ]

# variables
var =[
    # Leptons kinematics
    ["Lepton1_Pt" ,"leptons.Pt()[0]" ,"1==1",60, 0., 600., True, "P_{t}(lepton1) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dPt}",1],
    ["Lepton1_Eta","leptons.Eta()[0]","1==1",50, -5., 5., True, "#eta(lepton1)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#eta}",1],
    ["Lepton1_Phi","leptons.Phi()[0]","1==1",28 , 0. , 3.15, True, "#Phi(lepton1)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Phi}",1],
    
    ]

for lhe in Lhefiles:
    lhe = lhe.split('.')[0]
    for v in var:
        p = multiprocessing.Process( target=plot, args=([lhe],v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7],v[8],v[9]) )
        p.start()


