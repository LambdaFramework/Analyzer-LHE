#! /usr/bin/env pythonAOAA

# Jim Henderson January 2013
# James.Henderson@cern.ch
#
# Usage:
# lhe2root.py <input_file.lhe> <OPTIONAL: output_file_name.root>
#
# PLEASE NOTE: This conversion was generated to convert les houches 1.0, it may not work on other versions
#              Please check the les houches version # at the top of the .lhe file

# shoh: check the condition begin and end

import os, sys, math
import ROOT as r
from ROOT import TTree, TFile, TLorentzVector, AddressOf, gROOT

DEBUG = False

# Get the input lhe file
if len(sys.argv) < 2:
    print "\nYou must enter the .lhe file you wish to convert as the first arguement. Exiting \n"
    sys.exit(1)

try:    input_file = file( sys.argv[1], 'r')
except:
    print "\nThe entered file cannot be opened, please enter a vaild .lhe file. Exiting. \n"
    sys.exit(1)
    pass

if len(sys.argv) > 2:    output_file_name = sys.argv[2]
else:                    output_file_name = "lhe.root"

try:    output_file = TFile(output_file_name, "RECREATE")
except:
    print "Cannot open output file named: " + output_file_name + "\nPlease enter a valid output file name as the 2nd arguement. Exiting"
    sys.exit(1)
    pass

output_tree = TTree("Physics", "Physics")
print "Setup complete \nOpened file " + str(sys.argv[1]) + "  \nConverting to .root format and outputing to " + output_file_name

# Setup output branches, a vector
leptons = r.vector('TLorentzVector')()
neutrinos = r.vector('TLorentzVector')()
quarks = r.vector('TLorentzVector')()
WBoson = r.vector('TLorentzVector')()
Higgs = r.vector('TLorentzVector')()

#tag objects
L1 = r.vector('TLorentzVector')()
v1 = r.vector('TLorentzVector')()
L2 = r.vector('TLorentzVector')()
v2 = r.vector('TLorentzVector')()
W1 = r.vector('TLorentzVector')()
W2 = r.vector('TLorentzVector')()
W3 = r.vector('TLorentzVector')()

#Charge
lepCH = r.vector('int')()
wCH = r.vector('int')()

L1CH=r.vector('int')()
v1CH=r.vector('int')()
L2CH=r.vector('int')()
v2CH=r.vector('int')()
W1CH= r.vector('int')()
W2CH= r.vector('int')()
W3CH= r.vector('int')()

#composite object
InvLepjj = r.vector('TLorentzVector')()
Invjj = r.vector('TLorentzVector')()
InvLepLep = r.vector('TLorentzVector')()
InvHW1 = r.vector('TLorentzVector')()
InvW2W3 = r.vector('TLorentzVector')()
InvW2 = r.vector('TLorentzVector')()
InvW3 = r.vector('TLorentzVector')()

output_tree.Branch("leptons",leptons)
output_tree.Branch("neutrinos",neutrinos)
output_tree.Branch("quarks",quarks)
output_tree.Branch("WBoson",WBoson)
output_tree.Branch("Higgs",Higgs)

output_tree.Branch("L1",L1)
output_tree.Branch("v1",v1)
output_tree.Branch("L2",L2)
output_tree.Branch("v2",v2)
output_tree.Branch("W1",W1)
output_tree.Branch("W2",W2)
output_tree.Branch("W3",W3)

#Charge
output_tree.Branch("lepCH",lepCH)
output_tree.Branch("wCH",wCH)

output_tree.Branch("L1CH",L1CH)
output_tree.Branch("v1CH",v1CH)
output_tree.Branch("L2CH",L2CH)
output_tree.Branch("v2CH",v2CH)
output_tree.Branch("W1CH",W1CH)
output_tree.Branch("W2CH",W2CH)
output_tree.Branch("W3CH",W3CH)

#composite object
output_tree.Branch("InvLepjj",InvLepjj)
output_tree.Branch("Invjj",Invjj)
output_tree.Branch("InvLepLep",InvLepLep)
output_tree.Branch("InvHW1",InvHW1)
output_tree.Branch("InvW2W3",InvW2W3)
output_tree.Branch("InvW2",InvW2)
output_tree.Branch("InvW3",InvW3)

#TLorentzVector
invlepjj = TLorentzVector()
invjj = TLorentzVector()
invleplep = TLorentzVector()
invhw1 = TLorentzVector()
invw2w3= TLorentzVector()
invw2 = TLorentzVector()
invw3 = TLorentzVector()

container=[]
lepton=[]
quark=[]
neutrino=[]
Wboson=[]

#Comparator
def getPt(TLorentzVector):
    return TLorentzVector[0].Pt()

############################################################################
# Create a struct which acts as the TBranch for non-vectors
gROOT.ProcessLine( "struct MyStruct{ Int_t n_particles; Double_t weight; Int_t njet; Float_t xsec1; Float_t xsec1_error; Float_t xsec2; Float_t xsec2_error; Int_t counter; Int_t SSmumu; Int_t OSmumu; Int_t SSee; Int_t OSee; Int_t SSemu; Int_t OSemu; };")
from ROOT import MyStruct

# Assign the variables to the struct
s = MyStruct()
output_tree.Branch('n_particles',AddressOf(s,'n_particles'),'n_particles/I')
output_tree.Branch('weight',AddressOf(s,'weight'),'weight/D') # exponential not working
output_tree.Branch('njet',AddressOf(s,'njet'),'njet/I')
output_tree.Branch('xsec1',AddressOf(s,'xsec1'),'xsec1/F')
output_tree.Branch('xsec1_error',AddressOf(s,'xsec1_error'),'xsec1_error/F')
output_tree.Branch('xsec2',AddressOf(s,'xsec2'),'xsec2/F')
output_tree.Branch('xsec2_error',AddressOf(s,'xsec2_error'),'xsec2_error/F')
output_tree.Branch('counter',AddressOf(s,'counter'),'counter/I')

#topology counter
output_tree.Branch('SSmumu',AddressOf(s,'SSmumu'),'SSmumu/I')
output_tree.Branch('OSmumu',AddressOf(s,'OSmumu'),'OSmumu/I')
output_tree.Branch('SSee',AddressOf(s,'SSee'),'SSee/I')
output_tree.Branch('OSee',AddressOf(s,'OSee'),'OSee/I')
output_tree.Branch('SSemu',AddressOf(s,'SSemu'),'SSemu/I')
output_tree.Branch('OSemu',AddressOf(s,'OSemu'),'OSemu/I')

############################################################################

particles = {}
skippedLines = []

### Loop parameters
in_ev = 0 # To know when to look for particles we must know when we are inside an event
in_ev_1 = 0 # The first line after <event> is information so we must skip that as well
s.n_particles = 0
s.njet = 0
s.weight = 0
s.xsec1 = 0
s.xsec1_error = 0
s.xsec2 = 0
s.xsec2_error = 0
s.counter = 0
s.SSmumu = 0
s.OSmumu = 0
s.SSee = 0
s.OSee = 0
s.SSemu = 0
s.OSemu = 0
xsec_start = False
xsec_count = 0
TotPart = 0
matching=False
##################

Leps=[11,-11,13,-13,15,-15]
Neus=[12,-12,14,-14,16,-16]
wb=[24,-24]
lightquarks=[21,1,2,3,4,-1,-2,-3,-4]
bquarks=[-5,5]

if DEBUG: print "DEBUGGING MODE ENABLE"; print "++++++++++++++++++++++++++"

for line in input_file:

    if 'add process' in line:
        matching=True
        continue

    #step 0
    if line.strip().startswith("<init>"):
        if DEBUG: print "Step0: Initialized with <init>"
        xsec_start=True
        continue

    if xsec_start:
        xsec_count+=1
        if matching:
            if xsec_count==2:
                s.xsec1 = float(line.split()[0])
                s.xsec1_error = float(line.split()[1])
                continue
            if xsec_count==3:
                s.xsec2 = float(line.split()[0])
                s.xsec2_error = float(line.split()[1])
                xsec_start=False
                continue
        else:
            if xsec_count==2:
                s.xsec1 = float(line.split()[0])
                s.xsec1_error = float(line.split()[1])
                xsec_start=False
                continue
        #return

    # step 2
    if in_ev_1 == 1:
        if DEBUG: print "Step2: Storing weight"
        in_ev_1 = 0
        s.weight = float( line.split()[2] )
        s.n_particles=int(line.split()[0])
        #print 'weight ',float( line.split()[2] )
        in_ev = 1
        continue

    # step 1
    if line.strip().startswith("<event>"):
        if DEBUG: print "Step1: Initialized with <event>"
        #in_ev_1 = 1
        jetiness = 0
        counter = 0
        headEve=True
        in_ev_1 = 1
        continue

    # Some versions of les houches have a pdf line that we don't care about here
    if line.startswith("#pdf"):
        continue

    # step 4
    if in_ev == 1 and (
        #line.split()[0].startswith("</event>")
        #line.split()[0].startswith("<rwgt>")
        line.split()[0].startswith("<mgrwt>") or
        line.split()[0].startswith("<scales") #match
        #line.split()[0].startswith("#aMCatNLO")
        #line.split()[0].startswith("#")
        ):
        if DEBUG: print "Step4: Finalizing variable storing"

        #sort jet in descending pt
        lepton.sort(key=getPt, reverse=True)
        neutrino.sort(key=getPt, reverse=True)
        quark.sort(key=getPt, reverse=True)
        Wboson.sort(key=getPt, reverse=True)

        #Composite object
        #invjj = quark[0][0]+quark[1][0]
        #invlepjj = invjj+lepton[1][0] #the second lepton
        #invleplep = lepton[0][0]+lepton[1][0]

        #Filling
        for ilep in lepton:
            leptons.push_back(ilep[0])
            lepCH.push_back(ilep[1])
        for ineutrino in neutrino:
            neutrinos.push_back(ineutrino[0])
        for iquark in quark:
            quarks.push_back(iquark[0])
        for iwboson in Wboson:
            WBoson.push_back(iwboson[0])
            wCH.push_back(iwboson[1])

        s.njet = jetiness

        ### Find mom
        for par in container:
            pdgId=par[0]; stat=par[1]; mother1=par[2]; mother2=par[3]; p4=par[4]

            if stat==-1: continue
            #Looking for W1, mother1==1 and mother2==2
            if abs(pdgId)==24 and mother1==1 and mother2==2:
                W1.push_back(p4); W1CH.push_back(pdgId)
            #Looking for lepton1, mother1==3 and mother2==3
            if mother1==3 and mother2==3:
                if pdgId in Leps:
                    L1.push_back(p4); L1CH.push_back(pdgId)
                if pdgId in Neus:
                    v1.push_back(p4); v1CH.push_back(pdgId)

            #Leptonic final state for W2
            if pdgId in Leps+Neus and mother1!=3 and mother2!=3:

                #On-shell W2
                if pdgId in Leps and container[mother1-1][0] in wb and container[mother1-1][2]==4:
                    L2.push_back(p4); L2CH.push_back(pdgId)
                    W2.push_back(container[mother1-1][4]); W2CH.push_back(container[mother1-1][0])
                if pdgId in Neus and container[mother1-1][0] in wb and container[mother1-1][2]==4:
                    v2.push_back(p4); v2CH.push_back(pdgId)

                #off-shell W2
                if pdgId in Leps and container[mother1-1][0]==25:
                    L2.push_back(p4); L2CH.push_back(pdgId)
                if pdgId in Neus and container[mother1-1][0]==25:
                    v2.push_back(p4); v2CH.push_back(pdgId)

            #Hadronic final state for W3
            if pdgId in lightquarks+bquarks:
                invjj+=p4
                #On-shell W3
                if container[mother1-1][0] in wb and container[mother1-1][2]==4:
                    W3.push_back(container[mother1-1][4]); W3CH.push_back(container[mother1-1][0])

                #Off-shell W3

        Invjj.push_back(invjj)
        invlepjj=L2[0]+invjj
        InvLepjj.push_back(invlepjj)
        invleplep=L1[0]+L2[0]
        InvLepLep.push_back(invleplep)
        invhw1=Higgs[0]+W1[0]
        InvHW1.push_back(invhw1)
        invw2w3=invlepjj+v2[0]
        InvW2W3.push_back(invw2w3)

        #reconstruct off-shell w
        invw2=L2[0]+v2[0]
        InvW2.push_back(invw2)
        invw3=invjj
        InvW3.push_back(invw3)

        #Topology survey
        ##same flavour, opposite sign
        if L1CH[0]+L2CH[0]==0:
            ## abs(13+13)
            if abs(L1CH[0])+abs(L2CH[0])==26:
                s.OSmumu = 1
            ## abs(11+11)
            if abs(L1CH[0])+abs(L2CH[0])==22:
                s.OSee = 1
        ## Opposite flavour, opp sign -11+13 = 2 ; 11-13 =-2
        elif L1CH[0]+L2CH[0] in [2,-2]: #and abs(L1CH[0])==11:
            s.OSemu = 1
        ## Opposite flavour, same sign -11-13=-24 ; 11+13=24
        elif L1CH[0]+L2CH[0] in [24,-24]: #and abs(L1CH[0])==11:
            s.SSemu = 1
        ##same flavour, same sign 13+13
        elif L1CH[0]+L2CH[0] in [26,-26]:
            s.SSmumu = 1
        elif L1CH[0]+L2CH[0] in [22,-22]:
            s.SSee = 1
        
        output_tree.Fill()

        # Reset variables
        s.n_particles = 0
        s.weight = 0
        s.njet = 0

        s.SSmumu = 0
        s.OSmumu = 0
        s.SSee = 0
        s.OSee = 0
        s.SSemu = 0
        s.OSemu = 0

        leptons.clear()
        neutrinos.clear()
        quarks.clear()
        WBoson.clear()
        Higgs.clear()
        lepCH.clear()
        wCH.clear()

        L1.clear()
        L2.clear()
        v1.clear()
        v2.clear()
        W1.clear()
        W2.clear()
        W3.clear()

        L1CH.clear()
        L2CH.clear()
        v1CH.clear()
        v2CH.clear()
        W1CH.clear()
        W2CH.clear()
        W3CH.clear()

        Invjj.clear()
        InvLepjj.clear()
        InvLepLep.clear()
        InvHW1.clear()
        InvW2W3.clear()
        InvW2.clear()
        InvW3.clear()
        
        invjj.SetPxPyPzE(0.,0.,0.,0.)
        invlepjj.SetPxPyPzE(0.,0.,0.,0.)
        invleplep.SetPxPyPzE(0.,0.,0.,0.)
        invhw1.SetPxPyPzE(0.,0.,0.,0.)
        invw2w3.SetPxPyPzE(0.,0.,0.,0.)
        invw2.SetPxPyPzE(0.,0.,0.,0.)
        invw3.SetPxPyPzE(0.,0.,0.,0.)

        del container[:]; del lepton[:]; del neutrino[:]; del quark[:]; del Wboson[:];
        in_ev = 0
        TotPart = 0
        continue

    # step 3
    if in_ev == 1:
        if DEBUG: print "step3: Looping on Events"
        # Check the status of this particle
        counter+=1
        try:
            if int(line.split()[1]) in [-1,1,2]: # particle status
                pdgid = int(line.split()[0]); state = int(line.split()[1]); mom1 = int(line.split()[2]); mom2 = int(line.split()[3])
                p = TLorentzVector( float(line.split()[6]), float(line.split()[7]), float(line.split()[8]), float(line.split()[9]) )
                container.append([pdgid,state,mom1,mom2,p])
                pair = [p,pdgid]

                if int(line.split()[1])==-1: continue

                if int(line.split()[0]) in Leps:
                    lepton.append(pair)
                if int(line.split()[0]) in Neus:
                    neutrino.append(pair)
                if int(line.split()[0]) in lightquarks:
                    jetiness+=1
                    quark.append(pair)
                if int(line.split()[0])==25:
                    Higgs.push_back(p)
                if int(line.split()[0]) in [24,-24]:
                    Wboson.append(pair)
                    pass
                pass
            pass
        except:
            #print line.strip()[0].startswith("#aMCatNLO ")
            if line not in skippedLines:
                print "Problem with line: ", line.replace("\n","")
                print "Skipping..."
                skippedLines.append( line )
                exit()
                pass
            pass
        pass
    pass

output_tree.Write()
output_file.Close()
