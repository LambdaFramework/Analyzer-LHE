
NORM2AU=False

var2 =  [
    #Electron
    ["Elec1_Pt","L1[0].Pt()","abs(L1CH[0])==11",60, 0., 600., True, "P_{t}(e1) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dPt}",1],
    ["Elec1_Eta","L1[0].Eta()","abs(L1CH[0])==11",50, -5., 5., True, "#eta(e1)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#eta}",1],
    ["Elec1_Phi","L1[0].Phi()","abs(L1CH[0])==11",28 , 0. , 3.15, True, "#Phi(e1)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Phi}",1],

    ["Elec2_Pt","L2[0].Pt()","abs(L2CH[0])==11",60, 0., 600., True, "P_{t}(e2) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dPt}",1],
    ["Elec2_Eta","L2[0].Eta()","abs(L2CH[0])==11",50, -5., 5., True, "#eta(e2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#eta}",1],
    ["Elec2_Phi","L2[0].Phi()","abs(L2CH[0])==11",28 , 0. , 3.15, True, "#Phi(e2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Phi}",1],

    #Muon
    ["Mu1_Pt","L1[0].Pt()","abs(L1CH[0])==13",120, 0., 600., True, "P_{t}(mu1) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dPt}",1],
    ["Mu1_Eta","L1[0].Eta()","abs(L1CH[0])==13",50, -5., 5., True, "#eta(mu1)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#eta}",1],
    ["Mu1_Phi","L1[0].Phi()","abs(L1CH[0])==13",28 , 0. , 3.15, True, "#Phi(mu1)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Phi}",1],

    ["Mu2_Pt","L2[0].Pt()","abs(L2CH[0])==13",120, 0., 600., True, "P_{t}(mu2) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dPt}",1],
    ["Mu2_Eta","L2[0].Eta()","abs(L2CH[0])==13",50, -5., 5., True, "#eta(mu2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#eta}",1],
    ["Mu2_Phi","L2[0].Phi()","abs(L2CH[0])==13",28 , 0. , 3.15, True, "#Phi(mu2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Phi}",1],

    #electron neutrino
    ["ve1_Pt","v1[0].Pt()","abs(v1CH[0])==12",60, 0., 600., True, "P_{t}(ve1) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dPt}",1],
    ["ve1_Eta","v1[0].Eta()","abs(v1CH[0])==12",50, -5., 5., True, "#eta(ve1)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#eta}",1],
    ["ve1_Phi","v1[0].Phi()","abs(v1CH[0])==12",28 , 0. , 3.15, True, "#Phi(ve1)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Phi}",1],

    ["ve2_Pt","v2[0].Pt()","abs(v2CH[0])==12",60, 0., 600., True, "P_{t}(ve2) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dPt}",1],
    ["ve2_Eta","v2[0].Eta()","abs(v2CH[0])==12",50, -5., 5., True, "#eta(ve2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#eta}",1],
    ["ve2_Phi","v2[0].Phi()","abs(v2CH[0])==12",28 , 0. , 3.15, True, "#Phi(ve2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Phi}",1],

    #muon neutrino
    ["vmu1_Pt","v1[0].Pt()","abs(v1CH[0])==14",60, 0., 600., True, "P_{t}(vmu1) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dPt}",1],
    ["vmu1_Eta","v1[0].Eta()","abs(v1CH[0])==14",50, -5., 5., True, "#eta(vmu1)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#eta}",1],
    ["vmu1_Phi","v1[0].Phi()","abs(v1CH[0])==14",28 , 0. , 3.15, True, "#Phi(vmu1)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Phi}",1],

    ["vmu2_Pt","v2[0].Pt()","abs(v2CH[0])==14",60, 0., 600., True, "P_{t}(vmu2) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dPt}",1],
    ["vmu2_Eta","v2[0].Eta()","abs(v2CH[0])==14",50, -5., 5., True, "#eta(vmu2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#eta}",1],
    ["vmu2_Phi","v2[0].Phi()","abs(v2CH[0])==14",28 , 0. , 3.15, True, "#Phi(vmu2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Phi}",1],

    #Angular difference between e1 and ve1
    ["e1ve1_dPhi","deltaPhi(L1[0].Phi(),v1[0].Phi())" ,"abs(L1CH[0])==11 && abs(v1CH[0])==12",28 , 0. , 3.15 , True, "DeltaPhi(e1,ve1)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Delta#eta}",1],
    ["e1ve1_dR", "deltaR(L1[0].Phi(),L1[0].Eta(),v1[0].Phi(),v1[0].Eta())" ,"abs(L1CH[0])==11 && abs(v1CH[0])==12",60 , 0. , 5 , True, "DeltaR(e1,ve1)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#DeltaR}",1],

    #Angular difference between mu1 and vmu1
    ["mu1vmu1_dPhi","deltaPhi(L1[0].Phi(),v1[0].Phi())" ,"abs(L1CH[0])==13 && abs(v1CH[0])==14",28 , 0. , 3.15 , True, "DeltaPhi(mu1,vmu1)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Delta#eta}",1],
    ["mu1vmu1_dR", "deltaR(L1[0].Phi(),L1[0].Eta(),v1[0].Phi(),v1[0].Eta())" ,"abs(L1CH[0])==13 && abs(v1CH[0])==14",60 , 0. , 5 , True, "DeltaR(mu1,vmu1)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#DeltaR}",1],

    #Angular different between e2 and ve2
    ["e2ve2_dPhi","deltaPhi(L2[0].Phi(),v2[0].Phi())" ,"abs(L2CH[0])==11 && abs(v2CH[0])==12",28 , 0. , 3.15 , True, "DeltaPhi(e2,ve2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Delta#eta}",1],
    ["e2ve2_dR", "deltaR(L2[0].Phi(),L2[0].Eta(),v2[0].Phi(),v2[0].Eta())" ,"abs(L1CH[0])==11 && abs(v1CH[0])==12",60 , 0. , 5 , True, "DeltaR(e2,ve2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#DeltaR}",1],

    #Angular different between mu2 and vmu2
    ["mu2vmu2_dPhi","deltaPhi(L2[0].Phi(),v2[0].Phi())" ,"abs(L2CH[0])==13 && abs(v2CH[0])==14",28 , 0. , 3.15 , True, "DeltaPhi(mu2,vmu2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Delta#eta}",1],
    ["mu2vmu2_dR", "deltaR(L2[0].Phi(),L2[0].Eta(),v2[0].Phi(),v2[0].Eta())" ,"abs(L2CH[0])==13 && abs(v2CH[0])==14",60 , 0. , 5 , True, "DeltaR(mu2,vmu2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#DeltaR}",1],

    #Jet
    ["Jet1_Pt","quarks[0].Pt()","",40, 0., 600., True, "P_{t}(j1) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dPt}",1],
    ["Jet1_Eta","quarks[0].Eta()","",50, -5., 5., True, "#eta(j1)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#eta}",1],
    ["Jet1_Phi","quarks[0].Phi()","",28 , 0. , 3.15, True, "#Phi(j1)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Phi}",1],

    ["Jet2_Pt","quarks[1].Pt()","",40, 0., 600., True, "P_{t}(j2) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dPt}",1],
    ["Jet2_Eta","quarks[1].Eta()","",50, -5., 5., True, "#eta(j2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#eta}",1],
    ["Jet2_Phi","quarks[1].Phi()","",28 , 0. , 3.15, True, "#Phi(j2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Phi}",1],

    #Wboson
    ["W1_Pt","W1[0].Pt()","",40, 0., 600., True, "P_{t}(W1) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dPt}",1],
    ["W1_Eta","W1[0].Eta()","",50, -5., 5., True, "#eta(W1)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#eta}",1],
    ["W1_Phi","W1[0].Phi()","",28 , 0. , 3.15, True, "#Phi(W1)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Phi}",1],
    ["W1_M","W1[0].M()","",50, 0, 200, True, "M(W1)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dn}",1],

    ["W2_Pt","W2[0].Pt()","",40, 0., 600., True, "P_{t}(W2) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dPt}",1],
    ["W2_Eta","W2[0].Eta()","",50, -5., 5., True, "#eta(W2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#eta}",1],
    ["W2_Phi","W2[0].Phi()","",28 , 0. , 3.15, True, "#Phi(W2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Phi}",1],
    ["W2_M","W2[0].M()","",50, 0, 200, True, "M(W2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dn}",1],

    ["W3_Pt","W3[0].Pt()","",40, 0., 600., True, "P_{t}(W3) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dPt}",1],
    ["W3_Eta","W3[0].Eta()","",50, -5., 5., True, "#eta(W3)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#eta}",1],
    ["W3_Phi","W3[0].Phi()","",28 , 0. , 3.15, True, "#Phi(W3)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Phi}",1],
    ["W3_M","W3[0].M()","",50, 0, 200, True, "M(W3)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dn}",1],

    #Higgs
    ["H_Pt","Higgs[0].Pt()","",40, 0., 600., True, "P_{t}(h) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dPt}",1],
    ["H_Eta","Higgs[0].Eta()","",50, -5., 5., True, "#eta(h)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#eta}",1],
    ["H_Phi","Higgs[0].Phi()","",28 , 0. , 3.15, True, "#Phi(h)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Phi}",1],
    ["H_M","Higgs[0].M()","",50, 0, 200, True, "M(h)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dn}",1],

    #Composite objects
    ["Invjj_M","Invjj.M()","",50, 0, 200, True, "M(jj) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dn}",1],
    ["Invjj_Pt","Invjj.Pt()","",40, 0., 600., True, "P_{t}(jj) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dPt}",1],
    ["Invjj_Phi","Invjj.Phi()","",28 , 0. , 3.15, True, "#Phi(jj)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Phi}",1],
    ["Invleplep_M","InvLepLep.M()","",50, 0, 200, True, "M(lep1lep2) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dn}",1],
    ["Invleplep_Pt","InvLepLep.Pt()","",40, 0., 600., True, "P_{t}(lep1lep2) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dPt}",1],
    ["Invleplep_Phi","InvLepLep.Phi()","",28 , 0. , 3.15, True, "#Phi(lep1lep2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Phi}",1],
    ["InvLepjj_M","InvLepjj.M()","",50, 0, 200, True, "M(lep2jj) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dM}",1],
    ["InvLepjj_Pt","InvLepjj.Pt()","",40, 0., 600., True, "P_{t}(lep2jj) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dPt}",1],
    ["InvLepjj_Phi","InvLepjj.Phi()","",28 , 0. , 3.15, True, "#Phi(lep2jj)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Phi}",1],

    ## Angular difference between two lepton
    ["lep12_dPhi","deltaPhi(L1[0].Phi(),L2[0].Phi())" ,"abs(L1CH[0])+abs(L2CH[0])==24",28 , 0. , 3.15 , True, "DeltaPhi(lep1,lep2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Delta#eta}",1],
    ["lep12_dR", "deltaR(L1[0].Phi(),L1[0].Eta(),L2[0].Phi(),L2[0].Eta())" ,"abs(L1CH[0])+abs(L2CH[0])==24",60 , 0. , 5 , True, "DeltaR(lep1,lep2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#DeltaR}",1],

    ## Angular difference between two jet
    ["Jet12_dPhi","deltaPhi(quarks[0].Phi(),quarks[1].Phi())" ,"",28 , 0. , 3.15 , True, "DeltaPhi(j1,j2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #\frac{dN}{d#Delta#eta}",1],
    ["Jet12_dR", "deltaR(quarks[0].Phi(),quarks[0].Eta(),quarks[1].Phi(),quarks[1].Eta())" ,"",60 , 0. , 5 , True, "DeltaR(j1,j2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#DeltaR}",1],

    ## Angular difference between two legs W1 + H , higgstrahlung
    ["W1H_dPhi","deltaPhi(W1[0].Phi(),Higgs[0].Phi())" ,"",28 , 0. , 3.15 , True, "DeltaPhi(W1,Higgs)", "A.U." if NORM2AU else "#frac{1}{#sigma} #\frac{dN}{d#Delta#eta}",1],
    ["W1H_dR", "deltaR(W1[0].Phi(),W1[0].Eta(),Higgs[1].Phi(),Higgs[1].Eta())" ,"",60 , 0. , 5 , True, "DeltaR(W1,Higgs)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#DeltaR}",1],

    ## Angular difference between two leg
    ["L1InvL2jj_dPhi","deltaPhi(L1[0].Phi(),InvLepjj[0].Phi())" ,"",28 , 0. , 3.15 , True, "DeltaPhi(W1,h)", "A.U." if NORM2AU else "#frac{1}{#sigma} #\frac{dN}{d#Delta#eta}",1],
    ["L1InvL2jj_dR", "deltaR(L1[0].Phi(),L1[0].Eta(),InvLepjj[0].Phi(),InvLepjj[0].Eta())" ,"",60 , 0. , 5 , True, "DeltaR(W1,h)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#DeltaR}",1],

    ##reconstructed invW2W3, with neutrino 2
    ["InvW2W3_Pt","InvW2W3[0].Pt()","",40, 0., 600., True, "P_{t}(InvW2W3) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dPt}",1],
    ["InvW2W3_Eta","InvW2W3[0].Eta()","",50, -5., 5., True, "#eta(InvW2W3)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#eta}",1],
    ["InvW2W3_Phi","InvW2W3[0].Phi()","",28 , 0. , 3.15, True, "#Phi(InvW2W3)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Phi}",1],
    ["InvW2W3_M","InvW2W3[0].M()","",50 , 0. , 200, True, "#M(InvW2W3)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dM}",1],

    ["InvW2_Pt","InvW2[0].Pt()","",40, 0., 600., True, "P_{t}(InvW2) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dPt}",1],
    ["InvW2_Eta","InvW2[0].Eta()","",50, -5., 5., True, "#eta(InvW2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#eta}",1],
    ["InvW2_Phi","InvW2[0].Phi()","",28 , 0. , 3.15, True, "#Phi(InvW2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Phi}",1],
    ["InvW2_M","InvW2[0].M()","",50 , 0. , 200, True, "#M(InvW2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dM}",1],

    ["InvW3_Pt","InvW3[0].Pt()","",40, 0., 600., True, "P_{t}(InvW3) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dPt}",1],
    ["InvW3_Eta","InvW3[0].Eta()","",50, -5., 5., True, "#eta(InvW3)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#eta}",1],
    ["InvW3_Phi","InvW3[0].Phi()","",28 , 0. , 3.15, True, "#Phi(InvW3)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Phi}",1],
    ["InvW3_M","InvW3[0].M()","",50 , 0. , 200, True, "#M(InvW3)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dM}",1],

    ["W2W3_dPhi","deltaPhi(InvW2[0].Phi(),InvW3[0].Phi())" ,"",28 , 0. , 3.15 , True, "DeltaPhi(InvW2,InvW3)", "A.U." if NORM2AU else "#frac{1}{#sigma} #\frac{dN}{d#Delta#eta}",1],
    ["W2W3_dR", "deltaR(InvW2[0].Phi(),InvW2[0].Eta(),InvW3[0].Phi(),InvW3[0].Eta())" ,"",60 , 0. , 5 , True, "DeltaR(InvW2,InvW3)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#DeltaR}",1],

    ## W before higgstrahlung InvHW1
    ["InvHW1_Pt","InvHW1[0].Pt()","",40, 0., 600., True, "P_{t}(InvHW) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dPt}",1],
    ["InvHW1_Eta","InvHW1[0].Eta()","",50, -5., 5., True, "#eta(InvHW)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#eta}",1],
    ["InvHW1_Phi","InvHW1[0].Phi()","",28 , 0. , 3.15, True, "#Phi(InvHW)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{d#Phi}",1],
    ["InvHW1_M","InvHW1[0].M()","",50 , 0. , 200, True, "#M(InvHW)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dM}",1],

    #Jet multiplicity
    ["Njet","njet","",10, -0.5, 9.5, True, "Jet Multiplicity", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dn}",1],

    #Counter
    ["Nparticle","n_particles","",15, -0.5, 14.5, True, "Number of Particle in Events", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{dN}{dn}",1],

    #switches
    ["SSmumu","SSmumu","",2, -0.5, 1.5, True, "SSmumu", "A.U." if NORM2AU else "Events",1],
    ["OSmumu","OSmumu","",2, -0.5, 1.5, True, "OSmumu", "A.U." if NORM2AU else "Events",1],
    ["SSee","SSee","",2, -0.5, 1.5, True, "SSee", "A.U." if NORM2AU else "Events",1],
    ["OSee","OSee","",2, -0.5, 1.5, True, "OSee", "A.U." if NORM2AU else "Events",1],
    ["SSemu","SSemu","",2, -0.5, 1.5, True, "SSemu", "A.U." if NORM2AU else "Events",1],
    ["OSemu","OSemu","",2, -0.5, 1.5, True, "OSemu", "A.U." if NORM2AU else "Events",1],

    #2-Dimensional plots
    ["2D_W2W3_dPhi_W1Pt","deltaPhi(InvW2[0].Phi(),InvW3[0].Phi()):W1[0].Pt()" ,"",[28,40] , [0.,0.] , [3.15,600] , True, "deltaphi w2w3 : W1", "A.U." if NORM2AU else "#frac{1}{#sigma} #\frac{dN}{d#Delta#eta}",2],
    ["2D_lep1v1_dPhi_W1Pt","deltaPhi(L1[0].Phi(),v1[0].Phi()):W1[0].Pt()" ,"",[28,40] , [0.,0.] , [3.15,600] , True, "deltaphi lep1v1 : W1", "A.U." if NORM2AU else "#frac{1}{#sigma} #\frac{dN}{d#Delta#eta}",2],
    ["2D_W1pt_Hpt","W1[0].Pt():Higgs[0].Pt()" ,"",[40,40] , [0.,0.] , [600,600] , True, "W1[0].Pt():Higgs[0].Pt()", "A.U." if NORM2AU else "#frac{1}{#sigma} #\frac{dN}{d#Delta#eta}",2],
]

var = 
