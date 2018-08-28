#! /usr/bin/env python

import os, sys
from os import listdir
import copy
import time
import math
import ROOT
from array import array
from ROOT import gROOT, gRandom, AddressOf
from ROOT import TFile, TTree, TCut, TH1F, THStack, TLeaf, TGraph, TMultiGraph
from ROOT import TStyle, TCanvas, TPad
from ROOT import TLegend, TLatex, TText, TLegendEntry

gROOT.Macro('functions.C')


colour = [ 798, 801, 881, 856, 418, 6, 13, 46, 100, 7, 800 ]

dir=os.environ["ldir"]
input = "/" + dir[1:(dir.find("src"))] + "lhe2rootfiles/"
output = "/" + dir[1:(dir.find("src"))] + "plots/"

mchi = [1,10,100,150,200,300,400,500,600,700]
coupling = ["BBbarDM"] ######## Vector_Zprime or Axial_Zprime

file = {}
tree = {}
graph = {}

ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch(True)

for c in coupling:

    c1 = TCanvas("c1", "mpxsec", 1600, 1200)
    mg = TMultiGraph("mg","Inclusive #Phi Mass scan on Gen-Cross Section");
#leg = TLegend(0.64,0.7568421,0.85,0.87,"","brNDC")
    leg = TLegend(0.6, 0.9-0.035*len(mchi), 0.88, 0.89)
    leg.SetBorderSize(1)
    leg.SetFillStyle(1) #1001                                                                                                                                                                               
    leg.SetFillColor(0)
    leg.SetTextFont(132)

    for f,i in enumerate(mchi):
        
        file[f] = TFile( output + "%s/xd_%s/rootfile.root" %(c,i) , "READ")
        tree[f] = file[f].Get("tree")

        tree[f].Draw("genxsec:mp")
        graph[f] = TGraph( tree[f].GetSelectedRows(), tree[f].GetV2(), tree[f].GetV1()  )
        graph[f].SetLineColor(colour[f])
        graph[f].SetLineWidth(2)
        graph[f].SetMarkerStyle(20)
        graph[f].SetMarkerSize(1)
        
        mg.Add(graph[f])
        
    #leg = TLegend(0.64,0.7568421,0.85,0.87,"","brNDC");
        
        leg.SetBorderSize(1)
        leg.SetLineColor(colour[f])
        leg.SetLineStyle(1)
        leg.SetLineWidth(1)
        leg.SetFillColor(0)
        leg.SetFillStyle(1011)
        leg.AddEntry(graph[f],"M(#chi) = %s GeV" %i,"l")

    c1.cd()    
    mg.Draw("APC")
    c1.SetLogy()
    c1.Update()
    mg.GetYaxis().SetTitle("Cross Section (pb)")
    mg.GetXaxis().SetTitle("#Phi Mass [GeV]")
    leg.Draw()

    tex1 = TLatex(0.68,0.52,"%s" %c )
    tex1.SetNDC()
    tex1.SetTextAlign(13)
    tex1.SetTextFont(42)
    tex1.SetTextSize(0.03)
    tex1.SetLineWidth(2)
    tex1.Draw()
    
    tex2 = TLatex(0.68,0.47,"#sqrt{s} = 13 TeV");
    tex2.SetNDC()
    tex2.SetTextAlign(13)
    tex2.SetTextFont(42)
    tex2.SetTextSize(0.03)
    tex2.SetLineWidth(2)
    tex2.Draw()
    
    tex = TLatex(0.68,0.43,"g_{#chi}= 1.0 ; g_{q}=0.25");
    tex.SetNDC()
    tex.SetTextAlign(13)
    tex.SetTextFont(42)
    tex.SetTextSize(0.03)
    tex.SetLineWidth(2)
    tex.Draw()
    
    
    c1.Print(output + "%s/%s_Xsec_vs_Masspoints.pdf" %(c,c) )

