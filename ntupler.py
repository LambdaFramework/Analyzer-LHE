#! /usr/bin/env pythonAOA

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
#InVhiggs = r.vector('TLorentzVector')()
InvLepjj = r.vector('TLorentzVector')()

output_tree.Branch("leptons",leptons)
output_tree.Branch("neutrinos",neutrinos)
output_tree.Branch("quarks",quarks)
output_tree.Branch("WBoson",WBoson)
output_tree.Branch("Higgs",Higgs)
#output_tree.Branch("InVhiggs",InVhiggs)
output_tree.Branch("InvLepjj",InvLepjj)

#TLorentzVector
#invhiggs = TLorentzVector()
invlepjj = TLorentzVector()
lepton=[]
quark=[]
neutrino=[]
Wboson=[]

#Comparator
def getPt(TLorentzVector):
    return TLorentzVector.Pt()

############################################################################
# Create a struct which acts as the TBranch for non-vectors
gROOT.ProcessLine( "struct MyStruct{ Int_t n_particles; Double_t weight; Int_t njet; Float_t xsec1; Float_t xsec1_error; Float_t xsec2; Float_t xsec2_error; Int_t counter; };")
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

############################################################################

particles = {}
skippedLines = []
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
xsec_start = False
xsec_count = 0
chi = 0
matching=False

Leps=[11,-11,13,-13,15,-15]
Neus=[12,-12,14,-14,16,-16]
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
        #print 'weight ',float( line.split()[2] ) 
        in_ev = 1
        #print line
        continue

    # step 1
    if line.strip().startswith("<event>"):        
        if DEBUG: print "Step1: Initialized with <event>"
        in_ev_1 = 1
        jetiness = 0
        counter = 0
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
        
        for ilepton in lepton:
            leptons.push_back(ilepton)
        for ineutrino in neutrino:
            neutrinos.push_back(ineutrino)
        for iquark in quark:
            quarks.push_back(iquark)
        for iwboson in Wboson:
            WBoson.push_back(iwboson)
            
        #Invariant
        invlepjj = quark[0]+quark[1]+lepton[1]
        #invhiggs  = Wboson[0]+Wboson[1]
        #InVhiggs.push_back(invhiggs)
        InvLepjj.push_back(invlepjj)
        s.njet = jetiness
        output_tree.Fill()
        # Reset variables
        s.n_particles = 0
        s.weight = 0
        s.njet = 0
        
        leptons.clear()
        neutrinos.clear()
        quarks.clear()
        WBoson.clear()
        Higgs.clear()
        InvLepjj.clear()
        #InVhiggs.clear()
        #invhiggs.SetPxPyPzE(0.,0.,0.,0.)
        invlepjj.SetPxPyPzE(0.,0.,0.,0.)
        del lepton[:];del neutrino[:];del quark[:];del Wboson[:]
        in_ev = 0
        continue

    # step 3
    if in_ev == 1:
        if DEBUG: print "step3: Looping on Events"
        # Check the status of this particle
        counter+=1
        s.n_particles+=1
        try:
            if line.split()[1] is "1" or line.split()[1] is "2": # particle status
                p = TLorentzVector( float(line.split()[6]), float(line.split()[7]), float(line.split()[8]), float(line.split()[9]) )

                if int(line.split()[0]) in Leps:
                    lepton.append(p)
                if int(line.split()[0]) in Neus:
                    neutrino.append(p)
                if int(line.split()[0]) in lightquarks:
                    jetiness+=1
                    quark.append(p)
                if int(line.split()[0])==25:
                    Higgs.push_back(p)
                if int(line.split()[0]) in [24,-24]:
                    Wboson.append(p)
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
