#! /usr/bin/env python

import os, sys
import copy
import time
import math
import ROOT
from array import array
from ROOT import gROOT, gRandom, AddressOf
from ROOT import TFile, TTree, TCut, TH1F, THStack, TLeaf, TGraph
from ROOT import TStyle, TCanvas, TPad
from ROOT import TLegend, TLatex, TText
import os, multiprocessing

gROOT.Macro('functions.C')

colour = [ 798, 418, 801, 881, 856, 6, 13, 46, 100, 7, 800 ]

dir=os.environ["ldir"]
input= dir + "/Ntuples/"
output= dir + "/Plots/"

def drawCMS(lumi, text, onTop=False):
    latex = TLatex()
    latex.SetNDC()
    latex.SetTextSize(0.04)
    latex.SetTextColor(1)
    latex.SetTextFont(42)
    latex.SetTextAlign(33)
    if not onTop: latex.SetTextAlign(11)
    if not onTop:
        latex.DrawLatex(0.12, 0.91 if len(text)>0 else 0.84, "Madgraph Simulation")
        if (type(lumi) is float or type(lumi) is int) and float(lumi) > 0: latex.DrawLatex(0.65, 0.91, "%s, %.1f fb^{-1} " % (text,float(lumi)/1000.))
        elif type(lumi) is str: latex.DrawLatex(0.65, 0.91, "%s, %s fb^{-1} " %(text,lumi))
    else:
        latex.DrawLatex(0.23, 0.94, "Madgraph Simulation")
        if (type(lumi) is float or type(lumi) is int) and float(lumi) > 0: latex.DrawLatex(0.65, 0.94, "%s, %.1f fb^{-1} " % (text,float(lumi)/1000.))
        elif type(lumi) is str: latex.DrawLatex(0.65, 0.94, "%s, %s fb^{-1} " %(text,lumi))

def drawlabel(xposition,yposition,text):
    latex = TLatex()
    latex.SetNDC()
    latex.SetTextSize(0.035)
    latex.SetTextColor(1)
    latex.SetTextFont(42)
    latex.SetTextAlign(33)
    latex.DrawLatex( float(xposition) , float(yposition) , text )


def plot(sample, n, v, hbins, hmin, hmax, hlog, xlabel, ylabel):

    global output
    file = {}
    tree = {}
    hist = {}
    leaf = {}
    xsec = {}
    
    max = 0
    min = 1e99

    ROOT.gStyle.SetOptStat(1111)
    ROOT.gROOT.SetBatch(True)

    for i, s in enumerate(sample):
        file[s] = TFile( input + s + ".root", "READ")
        tree[s] = file[s].Get("Physics")
        hist[s] = TH1F(s, ";"+v, hbins, hmin , hmax)
        tree[s].Project(s, v, "")
        
        leaf[s] = tree[s].GetLeaf("xsec1")
        leaf[s].GetBranch().GetEntry(1)
        xsec[s] = leaf[s].GetValue()
        hist[s].SetLineColor(colour[i])

        hist[s].SetLineWidth(2)#3                                                                                                                                                    
        hist[s].SetFillColorAlpha(colour[i],0.35)
        hist[s].SetFillStyle(3005)

        if hist[s].GetMaximum() > max: max = hist[s].GetMaximum()*6
        if hist[s].GetMinimum() < min: min = hist[s].GetMinimum()

        #leg = TLegend(0.4, 0.9-0.035*len(sample), 0.68, 0.89)

        c1 = TCanvas("c1", "Gen", 1600, 1200)
        c1.cd()

        hist[sample[0]].SetMaximum(max*1.2)
        hist[sample[0]].SetMinimum(min+1.e6)

        hist[sample[0]].GetXaxis().SetTitle("%s" %xlabel)
        hist[sample[0]].GetYaxis().SetTitle("%s" %ylabel)
        hist[sample[0]].SetTitle("%s" %n)

        if len(sample)>1:
            for i, s in enumerate(sample):
                hist[s].Draw("HIST" if i==0 else "HIST, SAME")
        else:
            hist[s].Draw("HIST")

        if hlog:
            c1.GetPad(0).SetLogy()

        #leg.Draw()
        #c1.Update()

        drawlabel( 0.37 , 0.934 , "CMS Simulation" )

        output+="VH/"
        if not os.path.exists(output):
            os.makedirs(output)
        c1.Print( output + n + ".pdf")
        c1.Print( output + n + ".png")
###################

#Variables
NORM2AU=False

var = [
    #lepton                                                                                                                                                                          
    ["lep1_Pt","leptons[0].Pt()", 40, 0., 600., True, "P_{t}(lep1) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dPt}"],
    ["lep1_Eta","leptons[0].Eta()",  50, -5., 5., True, "#eta(lep1) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{d#eta}"],
    ["lep1_Phi","leptons[0].Phi()", 28 , 0. , 3.15, True, "#Phi(lep1) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{d#Phi}"],
    
    ["lep2_Pt","leptons[1].Pt()", 40, 0., 600., True, "P_{t}(lep2) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dPt}"],
    ["lep2_Eta","leptons[1].Eta()",  50, -5., 5., True, "#eta(lep2) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{d#eta}"],
    ["lep2_Phi","leptons[1].Phi()", 28 , 0. , 3.15, True, "#Phi(lep2) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{d#Phi}"],

    ["lep3_Pt","leptons[2].Pt()", 40, 0., 600., True, "P_{t}(lep3) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dPt}"],
    ["lep3_Eta","leptons[2].Eta()",  50, -5., 5., True, "#eta(lep3) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{d#eta}"],
    ["lep3_Phi","leptons[2].Phi()", 28 , 0. , 3.15, True, "#Phi(lep3) [GeV]", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{d#Phi}"],

    ["lep_dPhi","deltaPhi(leptons[0].Phi(),leptons[1].Phi())" , 28 , 0. , 3.15 , True, "DeltaPhi(l1l2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{d#Delta#eta}" ],
    ["lep_dR", "deltaR(leptons[0].Phi(),leptons[0].Eta(),leptons[1].Phi(),leptons[1].Eta())" , 60 , 0. , 5 , True, "DeltaR(l1l2)", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{d#DeltaR}" ],

    #Jet multiplicity                                                                                                                                                                
    ["Njet","njet", 10, -0.5, 9.5, True, "Jet Multiplicity", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dn}"],
    
    #Counter                                                                                                                                                                         
    ["Nparticle","n_particles", 10, -0.5, 9.5, True, "Number of Particle in Events", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dn}"],

    #InvLepjj                                                                                                                                                                        
    ["InvLepjj","InvLepjj.M()", 50, 0, 200, True, "Invariant mass of lepton + j j ", "A.U." if NORM2AU else "#frac{1}{#sigma} #frac{d#sigma}{dn}"],
]

#Samples -> NAME.root
## Multiple Root file draw on same canvas
#WhWW=["wphwwlvjj","wmhwwlvjj"] #NAME
## Single Root file draw on same canvas
WhWW=["wphwwlvjj"]

for v in var:
    p = multiprocessing.Process( target=plot, args=(WhWW,v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7]) )
    p.start()
