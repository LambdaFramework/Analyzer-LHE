#! /usr/bin/env python

import os, sys
import copy
import time
import math
import ROOT
from array import array
from ROOT import gROOT, gRandom, AddressOf
from ROOT import TFile, TTree, TCut, TH1F, THStack, TLeaf, TGraph, TH2F
from ROOT import TStyle, TCanvas, TPad
from ROOT import TLegend, TLatex, TText
import os, multiprocessing

cwd = os.getcwd()
inputs= "%s/../ntupler/Ntuples/" %cwd
output= "%s/plots/" %cwd

gROOT.Macro('functions.C')

#colour = [ 798, 418, 801, 881, 856, 6, 13, 46, 100, 7, 800 ]
colour = [8]

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


def plot( sample, n, v, sel, hbins, hmin, hmax, hlog, xlabel, ylabel, dim ):

    #hlog=False;

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
        file[s] = TFile( inputs + s + ".root" , "READ")
        tree[s] = file[s].Get("Physics")
        if dim==1:
            hist[s] = TH1F(s, ";"+v, hbins, hmin , hmax)
            tree[s].Project(s, v, "%s"%sel)

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
                
        elif dim==2:
            if len(hbins)!=2 or len(hmin)!=2 or len(hmax)!=2:
                print "dimension of hbins, hmin, hmax does not correspond to\
                2 dimensional histogram parameters."; exit;
            else:
                #X axis parameters follow by Y axis parameters
                hist[s] = TH2F( s, ";"+v, hbins[0], hmin[0] , hmax[0], hbins[1], hmin[1] , hmax[1] )
                # v in the form of x:y
                tree[s].Project(s, v, "%s"%sel,"colz")

                c1 = TCanvas("c1", "Gen", 1600, 1200)
                c1.cd()

                hist[s].Draw("COLZ")
                #if hlog:
                #    c1.GetPad(0).SetLogy()
                #    c1.GetPad(0).SetLogx()
        else:
            print "Unkown dimension"
            exit;

        #leg.Draw()
        c1.Update()

        drawlabel( 0.37 , 0.934 , "CMS Simulation" )

        output+="/"+sample[0]+"/"
        if not hlog:
            output+="Lin/"
        elif hlog:
            output+="Log/"
        
        if not os.path.exists(output):
            os.system('mkdir -p %s' %output)

        #c1.Print( output + n + ".pdf")
        c1.Print( output + n + ".png")
            
###################
