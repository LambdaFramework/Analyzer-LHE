from config import *
from plotCore import *

command = [

    #lepton
    ["lep1_Pt","lep1.Pt()", 40, 0., 600., True, "P_{t}(lep1) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dPt}"],
    ["lep1_Eta","lep1.Eta()",  50, -5., 5., True, "#eta(lep1) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{d#eta}"],
    ["lep1_Phi","lep1.Phi()", 28 , 0. , 3.15, True, "#Phi(lep1) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{d#Phi}"],

    ["lep2_Pt","lep2.Pt()", 40, 0., 600., True, "P_{t}(lep2) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dPt}"],
    ["lep2_Eta","lep2.Eta()",  50, -5., 5., True, "#eta(lep2) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{d#eta}"],
    ["lep2_Phi","lep2.Phi()", 28 , 0. , 3.15, True, "#Phi(lep2) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{d#Phi}"],

    ["lep_dPhi","deltaPhi(lep1.Phi(),lep2.Phi())" , 28 , 0. , 3.15 , True, "DeltaPhi(l1l2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{d#Delta#eta}" ],
    ["lep_dR", "deltaR(lep1.Phi(),lep1.Eta(),lep2.Phi(),lep2.Eta())" , 60 , 0. , 5 , True, "DeltaR(l1l2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{d#DeltaR}" ],

    #Jet multiplicity
    ["Njet","njet", 10, -0.5, 9.5, True, "Jet Multiplicity", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dn}"],

    #Counter
    ["Nparticle","n_particles", 10, -0.5, 9.5, True, "Number of Particle in Events", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dn}"],
]
