
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
import config
from LHEsamples import LHEs as sampleDict
from variables import command
#import CMS_lumi, tdrstyle

gROOT.Macro('functions.C')

colour = [ 798, 418, 801, 881, 856, 6, 13, 46, 100, 7, 800 ]
#colour = [ 2, 3, 801, 856, 1 ]
#colour = [ 830, 820, 416, 418, 850, 840, 433, 870, 860, 600, 602 ]
#colour = [ 826, 829, 414, 844, 861, 864, 852, 602, 890, 887, 883, 594 ]
dir=os.environ["ldir"]
input = "/" + dir[1:(dir.find("src"))] + "lhe2rootfiles/"

if config.manual:
    output = ""
else:
    output = "/" + dir[1:(dir.find("src"))] + "plots/"

#######################################################################

######################################################################

def drawCMS(lumi, text, onTop=False):
    latex = TLatex()
    latex.SetNDC()
    latex.SetTextSize(0.04)
    latex.SetTextColor(1)
    latex.SetTextFont(42)
    latex.SetTextAlign(33)
    #if (type(lumi) is float or type(lumi) is int) and float(lumi) > 0: latex.DrawLatex(0.95, 0.985, "%.1f fb^{-1}  (13 TeV)" % (float(lumi)/1000.))
    #elif type(lumi) is str: latex.DrawLatex(0.95, 0.985, "%s fb^{-1}  (13 TeV)" % lumi)
    #latex.DrawLatex(0.95, 0.985, "PDF %s" % lumi)

    #latex.DrawLatex(0.80, 0.91, "%s fb^{-1}" % lumi)
    if not onTop: latex.SetTextAlign(11)
    #latex.SetTextSize(0.05 if len(text)>0 else 0.06)
    if not onTop:
        latex.DrawLatex(0.12, 0.91 if len(text)>0 else 0.84, "Madgraph Simulation")
        if (type(lumi) is float or type(lumi) is int) and float(lumi) > 0: latex.DrawLatex(0.65, 0.91, "%s, %.1f fb^{-1} " % (text,float(lumi)/1000.))
        elif type(lumi) is str: latex.DrawLatex(0.65, 0.91, "%s, %s fb^{-1} " %(text,lumi))
        #latex.DrawLatex(0.65, 0.91 if len(text)>0 else 0.84, "%s , %s fb^{-1}" %(text,lumi)) 
    else:
        latex.DrawLatex(0.23, 0.94, "Madgraph Simulation")
        #latex.DrawLatex(0.65, 0.94, "%s , %s fb^{-1}" %(text,lumi))
        if (type(lumi) is float or type(lumi) is int) and float(lumi) > 0: latex.DrawLatex(0.65, 0.94, "%s, %.1f fb^{-1} " % (text,float(lumi)/1000.))
        elif type(lumi) is str: latex.DrawLatex(0.65, 0.94, "%s, %s fb^{-1} " %(text,lumi))
                
    #if not onTop: latex.DrawLatex(0.26, 0.91, text)
    #else: latex.DrawLatex(0.40, 0.98, text)
    #else: latex.DrawLatex(0.23, 0.94, text)

def drawlabel(xposition,yposition,text):
    latex = TLatex()
    latex.SetNDC()
    latex.SetTextSize(0.035)
    latex.SetTextColor(1)
    latex.SetTextFont(42)
    latex.SetTextAlign(33)
    #latex.SetTextAlign(11)
    #latex.DrawLatex(%f, %f, "%s" %(float(xposition),float(yposition),text))
    latex.DrawLatex( float(xposition) , float(yposition) , text )

def plot(sample, n, v, hbins, hmin, hmax, hlog, xlabel, ylabel, scanlabel, scantype):

    global output
    file = {}
    tree = {}
    hist = {}
    leaf = {}
    xsec = {}
    
    max = 0
    min = 1e99

    x, y = array( 'd' ), array( 'd' )
    graph = {}

################ aqui es el comienzo de las especificaciones de root
    if config.STATBOX:
        ROOT.gStyle.SetOptStat(1111)
    else:
        ROOT.gStyle.SetOptStat(0)

    ROOT.gROOT.SetBatch(True)
    
    ##DISCRETE ITERATION: CREATE HISTOGRAM
    for i, s in enumerate(sample):
        file[s] = TFile( input + s + ".root", "READ") 
        tree[s] = file[s].Get("Physics")
        hist[s] = TH1F(s, ";"+v, hbins, hmin , hmax)
        tree[s].Project(s, v, "")
        #Get Cross section from tree
        leaf[s] = tree[s].GetLeaf("xsec1")
        leaf[s].GetBranch().GetEntry(1)
        xsec[s] = leaf[s].GetValue()
        hist[s].SetLineColor(colour[i])
        hist[s].SetLineWidth(2)#3
        hist[s].SetFillColorAlpha(colour[i],0.35)
        hist[s].SetFillStyle(3005)
        if "Axial" in s or "Pseudo" in s:
            hist[s].SetLineStyle(2)
        #normalize to 1
        if config.NORM2AU:
            if hist[s].Integral()>0: hist[s].Scale(1./hist[s].Integral())
        else:
            #if hist[s].Integral()>0: 
            #hist[s].Scale(1./float(xsec[s]))
            hist[s].Scale( float(xsec[s]) )

        if hist[s].GetMaximum() > max: max = hist[s].GetMaximum()*6
        if hist[s].GetMinimum() < min: min = hist[s].GetMinimum()

    ################# Legend ########################
    if config.LEGEND or not config.manual:
        if config.STATBOX:
            leg = TLegend(0.4, 0.9-0.035*len(sample), 0.68, 0.89) # (x1,y1;x2,y2)
        else:
            leg = TLegend(0.5994437,0.7240964,0.8706537,0.8903614)
            #leg = TLegend(0.6, 0.9-0.035*len(sample), 0.88, 0.89) # (x1,y1;x2,y2)
            
        leg.SetBorderSize(0)
        leg.SetFillStyle(1) #1001
        leg.SetFillColor(0)

    ##DISCRETE ITERATION: CREATE LEGEND
    for i, s in enumerate(sample):

        #if LEGEND or manual:
        #    #compare different processes
        #    leg.AddEntry(hist[s], s, "l")
        name = s.split("_")[0]
        hzp = s.split("_")[2].split("-")[1]
        hdm = s.split("_")[3].split("-")[1]
        dm = s.split("_")[4].split("-")[1]
        
        if config.LEGEND:
            
            text=""

            if name == 'BBbarDM400Match1jet':
                if 'ScanZp' in scantype:
                    text+=" ; M_{Z'} = "
                    text+=hzp
                    text+=" GeV"
                elif 'ScanDM' in scantype:
                    text+=" ; M_{#chi} = "
                    text+=dm
		    text+=" GeV"
                elif 'Scanhs' in scantype:
                    text+=" ; M_{hs} = "
                    text+=hdm
                    text+=" GeV"

            elif name == 'BBbarDM400':
                if 'ScanZp' in scantype:
                    text+="M_{Z'} = "
                    text+=hzp
                    text+=" GeV"
                elif 'ScanDM' in scantype:
                    text+=" ; M_{#chi} = "                                                                           
                    text+=dm
                    text+=" GeV"
                elif 'Scanhs' in scantype:
                    text+=" ; M_{hs} = "
                    text+=hdm
                    text+=" GeV"


            elif name == 'BBbarDM':
                #text+="BBbarDM"
                if 'ScanZp' in scantype:
                    text+="M_{Z'} = "
                    text+=hzp
                    text+=" GeV"
                elif 'ScanDM' in scantype:
                    text+=" ; M_{#chi} = "
                    text+=dm
                    text+=" GeV"
                elif 'Scanhs' in scantype:
                    text+=" ; M_{hs} = "
                    text+=hdm
                    text+=" GeV"
                
            elif name == 'DiJetsDM':
                #text+="DiJetsDM"
                if 'ScanZp' in scantype:
                    text+="M_{Z'} = "
                    text+=hzp
                    text+=" GeV"
                elif 'ScanDM' in scantype:
                    text+=" ; M_{#chi} = "
                    text+=dm
                    text+=" GeV"
                elif 'Scanhs' in scantype:
                    text+=" ; M_{hs} = "
                    text+=hdm
                    text+=" GeV"
                
            elif 'MonojetDM' in s:
                #text+="MonojetDM"
                if 'ScanZp' in scantype:
                    text+="M_{Z'} = "
                    text+=hzp
                    text+=" GeV"
                elif 'ScanDM' in scantype:
                    text+=" ; M_{#chi} = "
                    text+=dm
                    text+=" GeV"
                elif 'Scanhs' in scantype:
                    text+=" ; M_{hs} = "
                    text+=hdm
                    text+=" GeV"

            elif 'HadronicDM' in s:
                #text+="HadronicDM"
                if 'ScanZp' in scantype:
                    text+="M_{Z'} = "
                    text+=hzp
                    text+=" GeV"
                elif 'ScanDM' in scantype:
                    text+=" ; M_{#chi} = "
		    text+=dm
                    text+=" GeV"
                elif 'Scanhs' in scantype:
                    text+=" ; M_{hs} = "
                    text+=hdm
                    text+=" GeV"

            #mpxsec.append([phi,xsec[s]])
            x.append( float(s.split("_")[2].split("-")[1]) )
            y.append( xsec[s] )

            leg.AddEntry(hist[s], text, "l")
    
    c1 = TCanvas("c1", "Gen", 1600, 1200) #1600,1200 Esto es el tamano de la imagen
    c2 = TCanvas("c2", "mpxsec", 1600, 1200)
    c1.cd()
    hist[sample[0]].SetMaximum(max*1.2)
    hist[sample[0]].SetMinimum(min+1.e6)
            
    hist[sample[0]].GetXaxis().SetTitle("%s" %xlabel)
    hist[sample[0]].GetYaxis().SetTitle("%s" %ylabel)
    hist[sample[0]].SetTitle("%s" %n)

    # DISCRETE ITERATION: PLOT AND DRAW
    for i, s in enumerate(sample):
        #hist[s].DrawClone("HIST" if i==0 else "HIST, SAME")
        hist[s].Draw("HIST" if i==0 else "HIST, SAME")
    if hlog:
        c1.GetPad(0).SetLogy()
    if config.LEGEND:
        leg.Draw()
        c1.Update()

    title=""
############################################

    drawlabel( 0.37 , 0.934 , "CMS Simulation" )
    drawlabel( 0.47 , 0.89 , "g_{#chi} = 1.00 ; g_{q} = 0.25 ; th = 0.01" )
    #if config.NORM2AU:
    drawlabel( 0.45 , 0.84 ,scanlabel)
    #drawlabel( 0.45 , 0.84 , "M_{Z'} = 2 TeV ; M_{#chi} = 100 GeV" )
    if 'BBbarDM' in s:
        if 'Match' in s:
            drawlabel( 0.40 , 0.77 , "p p #rightarrow hs(b#bar{b}) j + #chi#chi" )
        else:
            drawlabel( 0.40 , 0.77 , "p p #rightarrow hs(b#bar{b}) + #chi#chi" )
    elif 'DiJetsDM' in s:
        drawlabel( 0.40 , 0.77 , "p p #rightarrow Z^{'}(jj) + #chi#chi" )
    elif 'MonojetDM' in s:
        drawlabel( 0.40 , 0.77 , "p p #rightarrow j + #chi#chi" )
    elif 'HadronicDM' in s:
        drawlabel( 0.40 , 0.77 , "p p #rightarrow jj + b#bar{b}" )

    if "Axial" in s:
        output+="Axial_Zprime/"
        drawCMS(36000.,"Axial-Vector")
    elif "Vector" in s:
        output+="Vector_Zprime/"
        drawCMS(36000.,"Vector")

    if "Scalar" in s:
        output+="Scalar/"
        drawCMS(36000.,"Scalar")
    elif "Pseudo" in s:
        output+="Pseudo/"
        drawCMS(36000.,"Pseudo")

    #if singlefile==1:
    #    output+="Single_lhe/"
    #elif singlefile==0:
    #    output+="Combine_lhe/"

    #if not os.path.exists(output) and config.manual==0:
    #    os.makedirs(output)

    #Create output
    output+="%s/" %scantype
    
    if not os.path.exists(output):
        os.makedirs(output)
    #    output+="hs_50/"
    #elif "Mhs-70_" in s:
    #    output+="hs_70/"
    #elif "Mhs-90_" in s:
    #    output+="hs_90/"
        
    #if not os.path.exists(output):
    #    os.makedirs(output)
    #elif output=="Single_lhe/":
    #    print "folder Single_lhe is created"
    #elif output=="Combine_lhe/":
    #    print "folder Combine_lhe is created"

    if config.FPDF:
        c1.Print( output + title + n + ".pdf")
    if config.FPNG:
        c1.Print( output + title + n + ".png")

    if config.XSEC:
        
        c2.cd()
        if len(x) == len(y):
            gr = TGraph( len(x) , x , y )        
        
            gr.SetLineColor( 2 )
            gr.SetLineWidth( 3 )
            gr.SetMarkerColor( 4 )
            gr.SetMarkerStyle( 21 )
            gr.SetTitle( '#Phi Mass point VS Cross Section' )
            gr.GetXaxis().SetTitle( '#Phi Mass [GeV]' )
            gr.GetYaxis().SetTitle( 'Cross Section in pb' )
            gr.Draw( 'ACP' )
        
            c2.GetPad(0).SetLogy()
            
            if config.FPDF:
                c2.Print( output + "Xsec_vs_Masspoints.pdf")
            if config.FPNG:
                c2.Print( output + "Xsec_vs_Masspoints.png")

        else:
            print "Error, different size, x:%s ; y:%s" %(len(x),len(y))

        #### save root file for further process ####
        gROOT.ProcessLine( "struct MyStruct{ Float_t mp; Float_t genxsec; };")
        from ROOT import MyStruct
        output_file = TFile(output + "rootfile.root", "RECREATE")
        output_tree = TTree("tree", "tree")
        s = MyStruct()
        output_tree.Branch('mp',AddressOf(s,'mp'),'mp/F')
        output_tree.Branch('genxsec',AddressOf(s,'genxsec'),'genxsec/F')
        for i,j in zip(x,y):
            s.mp = i
            s.genxsec = j
            output_tree.Fill()
        output_tree.Write()
        output_file.Close()

def plot_xsec_contour(sample):
    output_file_name = "lhe.root"
    output_file = TFile(output_file_name, "RECREATE")
    output_tree = TTree("Physics", "Physics")
    gROOT.ProcessLine( "struct MyStruct{ Float_t xsec; Float_t mdm; Float_t mhs; Float_t mzp; Float_t whs; Float_t wzp; };")
    from ROOT import MyStruct
    s = MyStruct()
    output_tree.Branch('xsec',AddressOf(s,'xsec'),'xsec/F')
    output_tree.Branch('mdm',AddressOf(s,'mdm'),'mdm/F')
    output_tree.Branch('mhs',AddressOf(s,'mhs'),'mhs/F')
    output_tree.Branch('mzp',AddressOf(s,'mzp'),'mzp/F')
    output_tree.Branch('whs',AddressOf(s,'whs'),'whs/F')
    output_tree.Branch('wzp',AddressOf(s,'wzp'),'wzp/F')

    for i, su in enumerate(sample):
        s.xsec = 0.
        s.mdm = 0.
        s.mhs = 0.
        s.mzp = 0.
        s.whs = 0.
        s.wzp = 0.
        with open('../samples/'+su+'.lhe'        ,"rt") as fin:
            for line in fin:
                if "Integrated weight (pb)" in line:
                    #print line.split(' ')[-1]
                    s.xsec = float(line.split(' ')[-1])
                if "# mdm" in line:
                    #print line.split(' ')[-3]
                    s.mdm = float(line.split(' ')[-3])
                if "# mhs" in line:
                    #print line.split(' ')[-3]
                    s.mhs = float(line.split(' ')[-3])
                if "# mzp" in line:
                    #print line.split(' ')[-3]
                    s.mzp = float(line.split(' ')[-3])
                #hs
                if "DECAY  54" in line:
                    #print line.split(' ')[-1]
                    s.whs = float(line.split(' ')[-1])
                #zp
                if "DECAY  55" in line:
                    #print line.split(' ')[-1]
                    s.wzp = float(line.split(' ')[-1])
            output_tree.Fill()
    output_tree.Write()
    output_file.Close()

    #plot contour
    gROOT.Macro('Contour.C("lhe.root","BBbarDM_hs50")')
    #gROOT.Macro('Contour.C("lhe.root","DiJetDM_Mchi10")') 
    #os.remove('lhe.root')

########
def ScanZp(tag, fixhs, fixDM):

    samples=[]
    process=sampleDict['%s' %tag][0]
    hsList=sampleDict['%s' %tag][1]
    ZpList=sampleDict['%s' %tag][2]
    DMList=sampleDict['%s' %tag][3]

    if fixhs in hsList and fixDM in DMList:
        for zpp in ZpList:
            if 2*fixDM > zpp:
                print "DMSystem : ", 2*fixDM , " > ZP :", zpp
                continue
            proc = process.replace('[M]', "%s" %fixhs).replace('[O]', "%s" %fixDM).replace('[N]', "%s" %zpp)
            samples.append(proc)
    else:
        print "\n ScanZp ERROR on %s : Fix DM and Zp are not in mass grid\n" %tag

    sla="M_{hs} = %s GeV ; M_{#chi} = %s GeV" %(fixhs,fixDM)
    scantype="ScanZp/%s" %tag
    return [samples,sla,scantype]

def ScanDM(tag, fixhs, fixZp):

    samples=[]
    process=sampleDict['%s' %tag][0]
    hsList=sampleDict['%s' %tag][1]
    ZpList=sampleDict['%s' %tag][2]
    DMList=sampleDict['%s' %tag][3]

    if fixhs in hsList and fixZp in ZpList:
        for dm in DMList:
            if 2*dm > fixZp:
                print "DMsystem : ", 2*dm , " > ZP :", fixZp
                continue
            proc = process.replace('[M]', "%s" %fixhs).replace('[O]', "%s" %dm).replace('[N]', "%s" %fixZp)
            samples.append(proc)
    else:
        print "\n ScanDM ERROR on %s : Fix DM and Zp are not in mass grid\n" %tag

    sla="M_{hs} = %s GeV ; M_{Zp} = %s GeV" %(fixhs,fixZp)
    scantype="ScanDM/%s" %tag
    return [samples,sla,scantype]

def Scanhs(tag, fixDM, fixZp):

    samples=[]
    process=sampleDict['%s' %tag][0]
    hsList=sampleDict['%s' %tag][1]
    ZpList=sampleDict['%s' %tag][2]
    DMList=sampleDict['%s' %tag][3]

    if fixDM in DMList and fixZp in ZpList:
        for hhs in hsList:
            if 2*fixDM > fixZp:
                print "DMsystem : ", 2*dm , " > ZP :", fixZp
                continue
            proc = process.replace('[M]', "%s" %hhs).replace('[O]', "%s" %fixDM).replace('[N]', "%s" %fixZp)
            samples.append(proc)
    else:
        print "\n Scanhs ERROR on %s : Fix DM and Zp are not in mass grid\n" %tag

    sla="M_{Zp} = %s GeV ; M_{DM} = %s GeV" %(fixZp,fixDM)
    scantype="Scanhs/%s" %tag
    return [samples,sla,scantype]


def run(samples,command):
    print "BULK RUN"
    jobs=[]
    missing=[]
    #Check missing files
    for sab in samples[0]:
        if not os.path.exists("%s%s.root" %(input,sab)):
            missing.append(sab)
            samples[0].remove(sab)
        
    for v in command:
        p = multiprocessing.Process( target=plot, args=(samples[0],v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7],samples[1],samples[2]) )
        jobs.append(p)
        p.start()
    if not len (missing)==0:
        print "========================="
        print "MISSING ROOT FILE REPORT"
        print "========================="
        for each in missing:
            print each

if config.MASSGRIDXSEC:
    #print samples1
    print "Plotting cross section and width contour"
    plot_xsec_contour(samples1)
