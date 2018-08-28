from config import *
from plotCore import *

command = [
    
    #zp
    ["zp_mass","zp.M()", 100, 0., 5000., True,"Inv_M(zp) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dM_{Z'}}"],
    ["zp_Pt","zp.Pt()", 60, 0., 1500., True,"P_{t}(zp) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dPt}"],
    ["zp_Rapidity","zp.Rapidity()", 50, -5., 5., True, "#eta(zp)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dy}"],

     #hs
    ["hs_mass","hs.M()", 50, 0., 200., True,"Inv_M(hs) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dM_{hs}}"],
    ["hs_Pt","hs.Pt()", 60, 0., 1500., True,"P_{t}(hs) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dPt}"],
    ["hs_Rapidity","hs.Rapidity()", 50, -5., 5., True, "#eta(hs)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dy}"],

    #dmsystem
    ["DMsystem_mass","DMsystem.M()", 100, 0., 5000.,True,"Inv_M(#chi#chi) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dM_{DM}}"],
    ["DMsystem_Pt","DMsystem.Pt()", 60, 0., 1500, True, "P_{t}(#chi#chi) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dPt}"],
    ["DMsystem_Rapidity","DMsystem.Rapidity()", 50, -5., 5., True, "#eta(#chi#chi)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dy_{DM}}"],
    ["DMSystem_Phi","DMsystem.Phi()", 28 , 0. , 3.15 , True,"#phi(DMsystem)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{d#phi_{DM}}"],
    ["DMSystem_dPhi","deltaPhi(chi_plus.Phi(), chi_minus.Phi())" , 28 , 0. , 3.15 , True, "dPhi(#chi#chi)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{d#Delta#phi}" ],
    
    #dijet
    ["Dijet_mass","dijet12.M()", 20, 0., 500.,True,"Inv_M(jj) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dM_{dijet}}"],
    ["Dijet_Pt","dijet12.Pt()", 60, 0., 1500., True, "P_{t}(jj) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dPt}"],
    ["Dijet_Rapidity","dijet12.Rapidity()", 50, -5., 5., True, "#eta(jj)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dy}"],
    
    #lightjet1
    ["lightjet1_Pt","lightjet1.Pt()", 40, 0., 600., True, "P_{t}(j1) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dPt}"],
    ["lightjet1_Eta","lightjet1.Eta()", 50, -5., 5., True, "#eta(j1)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{d#eta}"],
    
    ["jet_dPhi","deltaPhi(lightjet1.Phi(),lightjet2.Phi())" , 28 , 0. , 3.15 , True, "DeltaPhi(j1j2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{d#Delta#eta}" ],
    ["jet_dR", "deltaR(lightjet1.Phi(),lightjet1.Eta(),lightjet2.Phi(),lightjet2.Eta())" , 60 , 0. , 5 , True, "DeltaR(j1j2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{d#DeltaR}" ],
    
    #lightjet2
    ["lightjet2_Pt","lightjet2.Pt()", 40, 0., 600., True, "P_{t}(j2) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dPt}"],
    ["lightjet2_Eta","lightjet2.Eta()", 50, -5., 5., True, "#eta(j2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{d#eta}"],
    
    #lightjet3
    ["lightjet3_Pt","lightjet3.Pt()", 40, 0., 600., True, "P_{t}(j3) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dPt}"],
    ["lightjet3_Eta","lightjet3.Eta()", 50, -5., 5., True, "#eta(j3)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{d#eta}"],
    
    #bjet1
    ["bjet1_Pt","bjet1.Pt()", 40, 0., 600., True, "P_{t}(bj1) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dPt}"],
    ["bjet1_Eta","bjet1.Eta()", 50, -5., 5., True, "#eta(bj1)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{d#eta}"],
    ["bjet_dPhi","deltaPhi(bjet1.Phi(),bjet2.Phi())" , 28 , 0. , 3.15 , True, "DeltaPhi(bj1,bj2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{d#Delta#eta}" ],
    ["bjet_dR", "deltaR(bjet1.Phi(),bjet1.Eta(),bjet2.Phi(),bjet2.Eta())" , 60 , 0. , 5 , True, "DeltaR(bj1,bj2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{d#DeltaR}" ],

    #bjet2
    ["bjet2_Pt","bjet2.Pt()", 40, 0., 600., True, "P_{t}(bj2) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dPt}"],
    ["bjet2_Eta","bjet2.Eta()", 50, -5., 5., True, "#eta(bj2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{d#eta}"],

    #bjet3
    ["bjet3_Pt","bjet3.Pt()", 40, 0., 600., True, "P_{t}(bj3) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dPt}"],
    ["bjet3_Eta","bjet3.Eta()", 50, -5., 5., True, "#eta(bj3)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{d#eta}"],
    
    #di b jets
    ["DiBjet_mass","dibjet12.M()", 20, 0., 500.,True,"Inv_M(bjbj) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dM_{dijet}}"],
    ["DiBjet_Pt","dibjet12.Pt()", 40, 0., 600., True, "P_{t}(bjbj) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dPt}"],
    ["DiBjet_Rapidity","dibjet12.Rapidity()", 50, -5., 5., True, "#eta(bjbj)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dy}"],

    #Jet multiplicity
    ["Njet","njet", 10, -0.5, 9.5, True, "Jet Multiplicity", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dn}"],

    #Counter
    ["Nparticle","n_particles", 10, -0.5, 9.5, True, "Number of Particle in Events", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dn}"],
]
