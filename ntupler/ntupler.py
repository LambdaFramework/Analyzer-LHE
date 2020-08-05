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
from ROOT import TTree, TFile, TLorentzVector, addressof, gROOT

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

# ************************************************************************
# helper function

def getPt(TLorentzList):
    return TLorentzList.Pt()
def getPt1(TLorentzList):
    return TLorentzList[1].Pt()

def TLorentzOperation( TLorentzList , TLorentzVector, TLorentzVectorID=None ):
    TLorentzList.sort( key= getPt1 if TLorentzVectorID is not None  else getPt, reverse=True)
    if TLorentzVectorID is not None:
        for ivec in TLorentzList: TLorentzVectorID.push_back(ivec[0])
        for ivec in TLorentzList: TLorentzVector.push_back(ivec[1])
    else:
        for ivec in TLorentzList: TLorentzVector.push_back(ivec)

# ************************************************************************
# particle identification

Leptons=[11,-11,13,-13,15,-15]
Neutrinos=[12,-12,14,-14,16,-16]
Wbosons=[24,-24]
#Zboson=[23]
Higgs=[25]
Quarks=[21,1,2,3,4,-1,-2,-3,-4]
bQuarks=[-5,5]

# ************************************************************************
# branch declaration (vector)

leptons = r.vector('TLorentzVector')()
leptons_pdgId = r.vector('int')()
neutrinos = r.vector('TLorentzVector')()
wbosons = r.vector('TLorentzVector')()
higgs = r.vector('TLorentzVector')()
quarks = r.vector('TLorentzVector')()
radiations = r.vector('int')() # -1 , 1
bquarks = r.vector('TLorentzVector')()

output_tree.Branch("leptons",leptons)
output_tree.Branch("leptons_pdgId",leptons_pdgId)
output_tree.Branch("neutrinos",neutrinos)
output_tree.Branch("wbosons",wbosons)
output_tree.Branch("higgs",higgs)
output_tree.Branch("quarks",quarks)
output_tree.Branch("radiations",radiations)
output_tree.Branch("bquarks",bquarks)

# ************************************************************************
# branch declaration Create a struct which acts as the TBranch for non-vectors

gROOT.ProcessLine( "struct MyStruct{ Int_t njet; Int_t n_particles; Float_t xsec; Float_t xsec1; Float_t xsec2; Float_t xsec3; Float_t xsec_err ; Float_t xsec1_err; Float_t xsec2_err; Float_t xsec3_err; };" )

from ROOT import MyStruct
s = MyStruct()

# Assign the variables to the struct
output_tree.Branch( 'njet' , addressof( s , 'njet' ) , 'njet/I' )
output_tree.Branch( 'n_particles' , addressof( s , 'n_particles' ) , 'n_particles/I' )
output_tree.Branch( 'xsec' , addressof( s , 'xsec' ) , 'xsec/F' )
output_tree.Branch( 'xsec1' , addressof( s , 'xsec1' ) , 'xsec1/F' )
output_tree.Branch( 'xsec2' , addressof( s , 'xsec2' ) , 'xsec2/F' )
output_tree.Branch( 'xsec3' , addressof( s , 'xsec3' ) , 'xsec3/F' )
output_tree.Branch( 'xsec_err' , addressof( s , 'xsec_err' ) , 'xsec_err/F' )
output_tree.Branch( 'xsec1_err' , addressof( s , 'xsec1_err' ) , 'xsec1_err/F' )
output_tree.Branch( 'xsec2_err' , addressof( s , 'xsec2_err' ) , 'xsec2_err/F' )
output_tree.Branch( 'xsec3_err' , addressof( s , 'xsec3_err' ) , 'xsec3_err/F' )

# ************************************************************************
# initialization
particles = {}
skippedLines = []

leptons_=[]
neutrinos_=[]
higgs_=[]
wbosons_=[]
quarks_=[]
bquarks_=[]

### Loop parameters
in_ev = 0
s.xsec = 0.
s.xsec1 = 0.
s.xsec2 = 0.
s.xsec3 = 0.
s.xsec_err = 0.
s.xsec1_err = 0.
s.xsec2_err = 0.
s.xsec3_err = 0.
s.n_particles = 0
s.njet = 0

matching = False
initStart = False
eventStart = False

DEBUG=False

# ************************************************************************

if DEBUG: print "DEBUGGING MODE ENABLE"; print "++++++++++++++++++++++++++"

for line in input_file:

    spline = line.split()

    if 'add process' in line :
        print("matching detected")
        matching=True
        continue;

    # Some versions of les houches have a pdf line that we don't care about here
    if line.startswith("#pdf"): continue

    # step 0
    if line.startswith("<init>") :
        if DEBUG: print "Step0: Initialized with <init>"
        initStart=True
        continue;

    if initStart :
        if line.startswith("2212") : continue;
        elif line.startswith("<generator") : continue;
        elif line.startswith("</init>") :
            if DEBUG: print "Step0: End with </init>"
            initStart=False
            continue;
        else:
            if spline[-1] == "1" : s.xsec1 = float(spline[0]) ; s.xsec1_err = float(spline[1]) ;
            if spline[-1] == "2" : s.xsec2 = float(spline[0]) ; s.xsec2_err = float(spline[1]) ;
            if spline[-1] == "3" : s.xsec3 = float(spline[0]) ; s.xsec3_err = float(spline[1]) ;
            continue;
        
    # step 1
    if not initStart and line.startswith("<event>") :
        if DEBUG: print "Step1: Initialized with <event>"
        eventStart=True
        continue;

    if eventStart :
        s.n_particles = int(spline[0]) ; s.xsec = float(spline[1]) ; s.xsec_err = float(spline[2]) ;
        in_ev=1 ; npar=int(spline[0])
        eventStart=False
        continue

    # step 2
    if in_ev == 1 and npar!=0 :
        if DEBUG: print "Step2 : Looping on event contents"
        try:
            if str(spline[1]) in [ "-1" ] : npar-=1; continue;
        
            pdgid = int(spline[0]) ; state = int(spline[1]) ; mom1 = int(spline[2]) ; mom2 = int(spline[3])
	    p4 = TLorentzVector( float(spline[6]), float(spline[7]), float(spline[8]), float(spline[9]) )
        
	    if pdgid in Leptons :
                if abs(pdgid) == 11 : leptons_.append([ pdgid , p4])
                elif abs(pdgid) == 13 : leptons_.append([ pdgid , p4])
        
	    if pdgid in Neutrinos : neutrinos_.append(p4)
            if pdgid in Wbosons   : wbosons_.append(p4)
            if pdgid in Quarks    :
                s.njet+=1
                quarks_.append([ -1 if mom1 in [4,5,6] else 1 , p4] )
            if pdgid in Higgs     : higgs_.append(p4)
            if pdgid in bQuarks   : bquarks_.append(p4)
            npar-=1
            
        except:
            if line not in skippedLines:
                print "Problem with line: ", line.replace("\n","")
                print "Skipping..."
                skippedLines.append( line )
                exit()
                pass
            pass
        pass

    # step 3
    if in_ev == 1 and npar==0 and line.startswith('</event>'):
        if DEBUG: print "Step3 : End with </event>"
        
        # sort particle in descending pt order
        TLorentzOperation( leptons_ , leptons , leptons_pdgId )
        TLorentzOperation( neutrinos_ , neutrinos )
        TLorentzOperation( higgs_ , higgs )
        TLorentzOperation( wbosons_ , wbosons )
        TLorentzOperation( quarks_ , quarks , radiations )
        TLorentzOperation( bquarks_ , bquarks )
        
        output_tree.Fill()

        # reset
        s.xsec = 0.
        s.xsec_err = 0.
        s.xsec1 = 0.
        s.xsec2 = 0.
        s.xsec3 = 0.
        s.xsec1_err = 0.
        s.xsec2_err = 0.
        s.xsec3_err = 0.
        s.n_particles = 0
        s.njet =0
        
        leptons_=[]
        neutrinos_=[]
        higgs_=[]
        wbosons_=[]
        quarks_=[]
        bquarks_=[]
        
        leptons.clear()
        leptons_pdgId.clear()
        neutrinos.clear()
        higgs.clear()
        wbosons.clear()
        quarks.clear()
        radiations.clear()
        bquarks.clear()

        in_ev=0
        continue
    pass

output_tree.Write()
output_file.Close()
