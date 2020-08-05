#include <string>

void Contour(string file,string model){

  //SetBatch(True);

  //TCanvas *c1 = new TCanvas("c1", "c1",444,129,702,570);
  //TCanvas *c2 = new TCanvas("c2", "c2",444,129,702,570);
  TCanvas *c1 = new TCanvas("c1", "c1",0,0,800,700);
  TCanvas *c2 = new TCanvas("c2", "c2",0,0,800,700);
  
  TLatex latex;
  latex.SetTextSize(0.025);
  latex.SetTextAlign(12);

  gStyle->SetOptStat(0);
  gStyle->SetOptTitle(0);

  //the ntuple file
  TFile *f1 = new TFile(file.c_str());

  // Declaration of leaf types                                                            
  Float_t xsec;
  Float_t mdm;
  Float_t mhs;
  Float_t mzp;
  Float_t whs;
  Float_t wzp;
  
  // List of branches                                                                                                                                      
  TBranch *b_xsec;
  TBranch *b_mdm;
  TBranch *b_mhs;
  TBranch *b_mzp;
  TBranch *b_whs;
  TBranch *b_wzp;

  TTree *t1 = (TTree*)f1->Get("Physics");
  
  t1->SetBranchAddress("xsec" , &xsec , &b_xsec);
  t1->SetBranchAddress("mdm" , &mdm , &b_mdm);
  t1->SetBranchAddress("mhs" , &mhs , &b_mhs);
  t1->SetBranchAddress("mzp" , &mzp , &b_mzp);
  t1->SetBranchAddress("whs" , &whs , &b_whs);
  t1->SetBranchAddress("wzp" , &wzp , &b_wzp);

  //Characterising your bin label and content
  //phimass
  string Xbins[] = { "500" , "1000" , "1500" , "2000" , "2500"};
  Int_t SXbins[] = {500,1000,1500,2000,2500};
  //chimass
  string Ybins[] = { "50" , "100" , "150" , "200" , "250" , "300" , "400" };
  Int_t SYbins[] = {50,100,150,200,250,300,400};
  //string Ybins[] = { "50" , "150"};
  //Int_t SYbins[] = {50,150};

  Int_t  Xbinnum = sizeof(Xbins)/sizeof(Xbins[0]);
  Int_t  Ybinnum = sizeof(Ybins)/sizeof(Ybins[0]);

  //std::cout<<"Xbinnum = "<<Xbinnum<<std::endl;
  //std::cout<<"Ybinnum = "<<Ybinnum<<std::endl;

  TH2F *h = new TH2F("h","Parton-Level Cross Section for NLO zprime signal",Xbinnum ,0 ,Xbinnum ,Ybinnum ,0 ,Ybinnum );
  TH2F *hwid = new TH2F("hwid","Parton-Level Width for NLO zprime signal",Xbinnum ,0 ,Xbinnum ,Ybinnum ,0 ,Ybinnum );

  //LEAVE THIS UNTOUCH
  for (Int_t i=0 ; i< Xbinnum ; i++ ){
    h->GetXaxis()->SetBinLabel((i+1),Xbins[i].c_str());
    hwid->GetXaxis()->SetBinLabel((i+1),Xbins[i].c_str());
  } 
  for (Int_t i=0 ; i< Ybinnum ; i++ ){
    h->GetYaxis()->SetBinLabel((i+1),Ybins[i].c_str());
    hwid->GetYaxis()->SetBinLabel((i+1),Ybins[i].c_str());
  }

  gStyle->SetPalette(1);
  TGaxis::SetMaxDigits(3);
  //Customize the Maximum and Minimum range, min, max
  h->GetZaxis()->SetRangeUser(0.00001,0.001);
  h->GetZaxis()->SetTitle("Cross Section [pb]");
  //h->GetYaxis()->SetTitle("M_{#chi} [GeV]");
  h->GetYaxis()->SetTitle("M_{hs} [GeV]");
  h->GetXaxis()->SetTitle("M_{#Phi} [GeV]");
  
  //Customize the Maximum and Minimum range, min, max  
  hwid->GetZaxis()->SetRangeUser(0.0000001,0.0001);
  hwid->GetZaxis()->SetTitle("Width [GeV]");
  hwid->GetYaxis()->SetTitle("M_{#chi} [GeV]");
  hwid->GetXaxis()->SetTitle("M_{#Phi} [GeV]");

  Int_t nentries = (Int_t)t1->GetEntries();
  for (Int_t i=0;i<nentries;i++) {
    t1->GetEntry(i);
    for (Int_t j=0 ; j<Xbinnum ; j++){
      //if (i<2)
      //std::cout<<"med = "<<med<<" ; SXbins["<<j<<"] = "<<SXbins[j]<<std::endl;
      if( mzp == SXbins[j] ){
	//if (i<2)
	//std::cout<<"Its a match med==SXbins"<<std::endl;
	for (Int_t k=0 ; k<Ybinnum ; k++){
	  //if (i<2)
	  //std::cout<<"mdm = "<<mdm<<" ; SYbins["<<k<<"] = "<<SYbins[k]<<std::endl;

	  if( mdm == SYbins[k] ){ //varying dm mass
	  //if ( mhs == SYbins[k] ){ //varying hs mass
	    //if (i<2)
	    //std::cout<<"Its a match md==SYbins"<<std::endl;
	    h->SetBinContent(j+1,k+1,xsec);
	    //std::cout<<"The Xsec = "<<xsec<<std::endl;
	    hwid->SetBinContent(j+1,k+1,whs); //wzp
	    std::cout<<"whs = "<<whs<<std::endl;
	    //std::cout<<"Fill xsec = "<<xsec<<std::endl;
	    break;
	  }
	}
	break;
      }
    }
  }
  
  gStyle->SetPaintTextFormat(".2e");
  c1->cd();
  c1->SetGridx();
  c1->SetGridy();
  c1->SetLogz();
  //c1->SetTickx(1);
  //c1->SetTicky(1);
  h->Draw("colztext");
  
  //text1 = new TLatex(0.15,0.93,(model+" coupling").c_str());
  latex.DrawLatex(2,7.3,model.c_str());
  latex.DrawLatex(.2,7.3,"g_{q} = 0.25 ; g_{#chi} = 1.00"); 

  c1->Update();
  c1->SaveAs(("Xsec_"+model+".pdf").c_str());

  //gStyle->SetPaintTextFormat("3.1f");
  gStyle->SetPaintTextFormat(".2e");
  c2->cd();
  //c2->SetLogz();
  c2->SetGridx();
  c2->SetGridy();
  //c1->SetTickx(1);                                                                                                      
  //c1->SetTicky(1);                                                                                                                                                   
  hwid->Draw("colztext");

  latex.DrawLatex(2,7.3,model.c_str());
  latex.DrawLatex(.2,7.3,"g_{q} = 0.25 ; g_{#chi} = 1.00");

  c2->Update();
  c2->SaveAs(("Width_"+model+".pdf").c_str());

}
