import os
from drawer import *
from tdrstyle import *

NORM2AU=False
 
Lhefiles=[ 'hwplus_ss_012j.root' ]

# variables
var =[
    # Leptons kinematics
    ["Lepton1_Pt" ,"leptons.Pt()[0]" ,"1==1",60, 0., 600., True, "P_{t}(lepton1) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dPt}",1],
    ["Lepton1_Eta","leptons.Eta()[0]","1==1",50, -5., 5., True, "#eta(lepton1)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#eta}",1],
    ["Lepton1_Phi","leptons.Phi()[0]","1==1",28 , 0. , 3.15, True, "#Phi(lepton1)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Phi}",1],
    
    ["Lepton2_Pt" ,"leptons.Pt()[1]" ,"1==1",60, 0., 600., True, "P_{t}(lepton2) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dPt}",1],
    ["Lepton2_Eta","leptons.Eta()[1]","1==1",50, -5., 5., True, "#eta(lepton2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#eta}",1],
    ["Lepton2_Phi","leptons.Phi()[1]","1==1",28 , 0. , 3.15, True, "#Phi(lepton2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Phi}",1],

    ["lep12_dPhi","deltaPhi(leptons.Phi()[0],leptons.Phi()[1])" ,"1==1",28 , 0. , 3.15 , True, "DeltaPhi(lep1,lep2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Delta#phi}",1],
    ["lep12_dR", "deltaR(leptons.Phi()[0],leptons.Eta()[0],leptons.Phi()[1],leptons.Eta()[1])" ,"1==1",60 , 0. , 5 , True, "DeltaR(lep1,lep2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#DeltaR}",1],
    ["lep12_dEta","deltaEta(leptons.Eta()[0],leptons.Eta()[1])" ,"1==1",50 , 0. , 5 , True, "DeltaEta(lep1,lep2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Delta#eta}",1],

    # Neutrino kinematics
    ["neu1_Pt","neutrinos.Pt()[0]","1==1",60, 0., 600., True, "P_{t}(neutrino1) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dPt}",1],
    ["neu1_Eta","neutrinos.Eta()[0]","1==1",50, -5., 5., True, "#eta(neutrino1)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#eta}",1],
    ["neu1_Phi","neutrinos.Phi()[0]","1==1",28 , 0. , 3.15, True, "#Phi(neutrino1)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Phi}",1],

    ["neu2_Pt","neutrinos.Pt()[1]","1==1",60, 0., 600., True, "P_{t}(neutrino2) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dPt}",1],
    ["neu2_Eta","neutrinos.Eta()[1]","1==1",50, -5., 5., True, "#eta(neutrino2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#eta}",1],
    ["neu2_Phi","neutrinos.Phi()[1]","1==1",28 , 0. , 3.15, True, "#Phi(neutrino2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Phi}",1],

    ["neu12_dPhi","deltaPhi(neutrinos.Phi()[0],neutrinos.Phi()[1])" ,"1==1",28 , 0. , 3.15 , True, "DeltaPhi(neu1,neu2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Delta#phi}",1],
    ["neu12_dR", "deltaR(neutrinos.Phi()[0],neutrinos.Eta()[0],neutrinos.Phi()[1],neutrinos.Eta()[1])" ,"1==1",60 , 0. , 5 , True, "DeltaR(neu1,neu2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#DeltaR}",1],
    ["neu12_dEta","deltaEta(neutrinos.Eta()[0],neutrinos.Eta()[1])" ,"1==1",50 , 0. , 5 , True, "DeltaEta(neu1,neu2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Delta#eta}",1],

    # (lepton-neutrino) kinematics
    ["lep1_neu1_dPhi","deltaPhi(leptons.Phi()[0],neutrinos.Phi()[0])" ,"1==1",28 , 0. , 3.15 , True, "DeltaPhi(lep1,neu1)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Delta#phi}",1],
    ["lep1_neu1_dR", "deltaR(leptons.Phi()[0],leptons.Eta()[0],neutrinos.Phi()[0],neutrinos.Eta()[0])" ,"1==1",60 , 0. , 5 , True, "DeltaR(lep1,neu1)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#DeltaR}",1],
    ["lep1_neu1_dEta","deltaEta(leptons.Eta()[0],neutrinos.Eta()[0])" ,"1==1",50 , 0. , 5 , True, "DeltaEta(lep1,neu1)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Delta#eta}",1],

    ["lep2_neu2_dPhi","deltaPhi(leptons.Phi()[1],neutrinos.Phi()[1])" ,"1==1",28 , 0. , 3.15 , True, "DeltaPhi(lep2,neu2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Delta#phi}",1],
    ["lep2_neu2_dR", "deltaR(leptons.Phi()[1],leptons.Eta()[1],neutrinos.Phi()[1],neutrinos.Eta()[1])" ,"1==1",60 , 0. , 5 , True, "DeltaR(lep2,neu2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#DeltaR}",1],
    ["lep2_neu2_dEta","deltaEta(leptons.Eta()[1],neutrinos.Eta()[1])" ,"1==1",50 , 0. , 5 , True, "DeltaEta(lep2,neu2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Delta#eta}",1],

    # invariant mass of W1
    ["lep1_neu1_M","invariantMass(leptons.Pt()[0], leptons.Eta()[0] , leptons.Phi()[0] , leptons.M()[0] , neutrinos.Pt()[0] , neutrinos.Eta()[0] , neutrinos.Phi()[0] , neutrinos.M()[0])" ,"1==1",40 , 0. , 200 , True, "InvM(lep1,neu1)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{InvM}",1],

    # invariant mass of W2
    ["lep2_neu2_M","invariantMass(leptons.Pt()[1], leptons.Eta()[1] , leptons.Phi()[1] , leptons.M()[1] , neutrinos.Pt()[1] , neutrinos.Eta()[1] , neutrinos.Phi()[1] , neutrinos.M()[1])" ,"1==1",40 , 0. , 200 , True, "InvM(lep2,neu2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{InvM}",1],
    
    # Higgs
    ["Higgs_Pt" ,"higgs.Pt()[0]" ,"1==1",60, 0., 600., True, "P_{t}(higgs) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dPt}",1],
    ["Higgs_Eta","higgs.Eta()[0]","1==1",50, -5., 5., True, "#eta(higgs)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#eta}",1],
    ["Higgs_Phi","higgs.Phi()[0]","1==1",28 , 0. , 3.15, True, "#Phi(higgs)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Phi}",1],
    ["Higgs_M","higgs.M()[0]","1==1",40 , 0., 200. , True, "M(higgs)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dM}",1],

    ]

for lhe in Lhefiles:
    lhe = lhe.split('.')[0]
    for v in var:
        p = multiprocessing.Process( target=plot, args=([lhe],v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7],v[8],v[9]) )
        p.start()


