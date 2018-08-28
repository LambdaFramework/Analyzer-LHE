#! /usr/bin/env pythonOA

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

if len(sys.argv) > 2:    output_file_name = "../lhe2rootfiles/" + sys.argv[2]
else:                    output_file_name = "lhe.root"

try:    output_file = TFile(output_file_name, "RECREATE")
except:
    print "Cannot open output file named: " + output_file_name + "\nPlease enter a valid output file name as the 2nd arguement. Exiting"
    sys.exit(1)
    pass

output_tree = TTree("Physics", "Physics")
print "Setup complete \nOpened file " + str(sys.argv[1]) + "  \nConverting to .root format and outputing to " + output_file_name
'''
def sortpt1(TLV1,TLV2):
    list=[]
    if TLV1.Pt() > TLV2.Pt():
        list.append(TLV1.Eta())
        list.append(TLV2.Eta())
    if TLV1.Pt() < TLV2.Pt():
        list.append(TLV2.Eta())
        list.append(TLV1.Eta())
    return list

def sortpt2(TLV1,TLV2):
    list=[]
    if TLV1.Pt() > TLV2.Pt():
        list.append(TLV1.Rapidity())
        list.append(TLV2.Rapidity())
    if TLV1.Pt() < TLV2.Pt():
        list.append(TLV2.Rapidity())
        list.append(TLV1.Rapidity())
    return list

def sortpt3(TLV1,TLV2):
    list=[]
    if TLV1.Pt() > TLV2.Pt():
        list.append(TLV1.Phi())
        list.append(TLV2.Phi())
    if TLV1.Pt() < TLV2.Pt():
        list.append(TLV2.Phi())
        list.append(TLV1.Phi())
    return list
'''
# Setup output branches, a vector
zp = r.vector('TLorentzVector')()
hs = r.vector('TLorentzVector')()
chi_plus = r.vector('TLorentzVector')()
chi_minus = r.vector('TLorentzVector')()
DMsystem = r.vector('TLorentzVector')()
lightjet1 = r.vector('TLorentzVector')()
lightjet2 = r.vector('TLorentzVector')()
lightjet3 = r.vector('TLorentzVector')()
bjet1 = r.vector('TLorentzVector')()
bjet2 = r.vector('TLorentzVector')()
bjet3 = r.vector('TLorentzVector')()
dijet12 = r.vector('TLorentzVector')()
dibjet12 = r.vector('TLorentzVector')()

output_tree.Branch("zp",zp)
output_tree.Branch("hs",hs)
output_tree.Branch("chi_plus",chi_plus)
output_tree.Branch("chi_minus",chi_minus)
output_tree.Branch("DMsystem",DMsystem)
output_tree.Branch("lightjet1",lightjet1)
output_tree.Branch("lightjet2",lightjet2)
output_tree.Branch("lightjet3",lightjet3)
output_tree.Branch("bjet1",bjet1)
output_tree.Branch("bjet2",bjet2)
output_tree.Branch("bjet3",bjet3)
output_tree.Branch("dijet12",dijet12)
output_tree.Branch("dibjet12",dibjet12)

#TLorentzVector
DM = TLorentzVector()
DIJET = TLorentzVector()
DIBJET = TLorentzVector()
#vector dummy
#DUMMY = r.vector('TLorentzVector')()
DUMMY=[]
BDUMMY=[]

#Comparator
def getPt(TLorentzVector):
    return TLorentzVector[0].Pt()

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
        DUMMY.sort(key=getPt, reverse=True)
        #BDUMMY.sort(key=getPt, reverse=True)

        #if jetiness>1 and DUMMY[0][1] is in lightquarks:
        #    lightjet1.push_back(DUMMY[0][0])
        #if jetiness==2 and DUMMY[1][1] is in lightquarks:
        #    lightjet2.push_back(DUMMY[1][0])
        #if jetiness==3 and DUMMY[2][1] is in lightquarks:
        #    lightjet3.push_back(DUMMY[2][0])

        #    DIJET= DUMMY[0][0]+ DUMMY[1][0]
        #    dijet12.push_back( DIJET )
        b1isfilled=False
        lj1isfilled=False
        for jetty in range(0,len(BDUMMY)):
            if BDUMMY[jetty][1] in bquarks:
                if not b1isfilled:
                    bjet1.push_back(BDUMMY[jetty][0])
                    DIBJET=BDUMMY[jetty][0]
                    b1isfilled=True
                elif b1isfilled:
                    bjet2.push_back(BDUMMY[jetty][0])
                    DIBJET+=BDUMMY[jetty][0]
                    dibjet12.push_back( DIBJET )
                if jetty==2:
                    bjet3.push_back(BDUMMY[jetty][0])
            elif BDUMMY[jetty][1] in lightquarks:
                if not lj1isfilled:
                    lightjet1.push_back(BDUMMY[jetty][0])
                    DIJET=BDUMMY[jetty][0]
                    lj1isfilled=True
                elif lj1isfilled:
                    lightjet2.push_back(BDUMMY[jetty][0])
                    DIJET+=BDUMMY[jetty][0]
                    dijet12.push_back( DIJET )
                if jetty==2:
                    lightjet3.push_back(BDUMMY[jetty][0])
                
        DMsystem.push_back( DM )
        s.njet = jetiness
        output_tree.Fill()
        # Reset variables
        s.n_particles = 0
        s.weight = 0
        s.njet = 0
        zp.clear()
        hs.clear()
        chi_plus.clear()
        chi_minus.clear()
        DMsystem.clear()
        dijet12.clear()
        dibjet12.clear()
        lightjet1.clear()
        lightjet2.clear()
        lightjet3.clear()
        bjet1.clear()
        bjet2.clear()
        bjet3.clear()
        DM.SetPxPyPzE(0.,0.,0.,0.)
        DIJET.SetPxPyPzE(0.,0.,0.,0.)
        DIBJET.SetPxPyPzE(0.,0.,0.,0.)
        del DUMMY[:]
        del BDUMMY[:]
        in_ev = 0
        chi = 0
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
                
                if int(line.split()[0]) == 55: zp.push_back( p ); #zp
                if int(line.split()[0]) == 54: hs.push_back( p ); #hs
                if int(line.split()[0]) == 52: 
                    chi+=1
                    if chi==1:
                        chi_plus.push_back( p )
                    elif chi==2:
                        chi_minus.push_back( p )
                    DM+=p

                if int(line.split()[0]) in lightquarks or int(line.split()[0]) in bquarks:
                    jetiness+=1
                    if int(line.split()[0]) in lightquarks or int(line.split()[0]) in bquarks:
                        BDUMMY.append( [p,int(line.split()[0])] )
                    #if jetiness==1:
                    #    lightjet1.push_back( p ); DIJET+=p
                    #if jetiness==2:
                    #    lightjet2.push_back( p ); DIJET+=p
                    #if jetiness==3:
                    #    lightjet3.push_back( p )
                    #    pass
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
