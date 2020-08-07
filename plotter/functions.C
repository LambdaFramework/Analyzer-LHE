void functions(){
  cout<<"load some functions.."<<endl;
}

float deltaPhi(float phi1, float phi2) {
  float PHI = fabs(phi1-phi2);
  if (PHI<=3.14159265)
    return PHI;
  else
    return 2*3.14159265-PHI;
}

float boostToMomPhi(float p1_pt, float p1_eta, float p1_phi, float p1_mass, float p2_pt, float p2_eta, float p2_phi, float p2_mass){
  TLorentzVector p1; p1.SetPtEtaPhiM(p1_pt, p1_eta, p1_phi, p1_mass);
  TLorentzVector p2; p2.SetPtEtaPhiM(p2_pt, p2_eta, p2_phi, p2_mass);  //boost to this frame (mother when its moving)
  TVector3 p3; p3 = p2.BoostVector();
  p1.Boost(p3);
  return p1.Phi();
}

float boostToMomTheta(float p1_pt, float p1_eta, float p1_phi, float p1_mass, float p2_pt, float p2_eta, float p2_phi, float p2_mass){
  TLorentzVector p1; p1.SetPtEtaPhiM(p1_pt, p1_eta, p1_phi, p1_mass);
  TLorentzVector p2; p2.SetPtEtaPhiM(p2_pt, p2_eta, p2_phi, p2_mass);  //boost to this frame (mother when its moving) 
  TVector3 p3; p3 = p2.BoostVector();
  p1.Boost(p3);
  return p1.Theta();
}

float boostToMomEta(float p1_pt, float p1_eta, float p1_phi, float p1_mass, float p2_pt, float p2_eta, float p2_phi, float p2_mass){
  TLorentzVector p1; p1.SetPtEtaPhiM(p1_pt, p1_eta, p1_phi, p1_mass);
  TLorentzVector p2; p2.SetPtEtaPhiM(p2_pt, p2_eta, p2_phi, p2_mass);  //boost to this frame (mother when its moving)
  TVector3 p3; p3 = p2.BoostVector();
  p1.Boost(p3);
  return p1.Eta();
}

float boostToMomPt(float p1_pt, float p1_eta, float p1_phi, float p1_mass, float p2_pt, float p2_eta, float p2_phi, float p2_mass){
  TLorentzVector p1; p1.SetPtEtaPhiM(p1_pt, p1_eta, p1_phi, p1_mass);
  TLorentzVector p2; p2.SetPtEtaPhiM(p2_pt, p2_eta, p2_phi, p2_mass);  //boost to this frame (mother when its moving) 
  TVector3 p3; p3 = p2.BoostVector();
  p1.Boost(p3);
  return p1.Pt();
}


float deltaR(float phi1, float eta1, float phi2, float eta2) {
  return sqrt( (eta2-eta1)*(eta2-eta1) + deltaPhi(phi1,phi2)*deltaPhi(phi1,phi2) );
}

float deltaEta(float eta1 , float eta2){
  return fabs(eta1-eta2);
}

float invariantMass(float p1_pt, float p1_eta, float p1_phi, float p1_mass, float p2_pt, float p2_eta, float p2_phi, float p2_mass) {
  if(p1_pt<0. || p2_pt<0.) return -1.;
  TLorentzVector p1;
  TLorentzVector p2;
  p1.SetPtEtaPhiM(p1_pt, p1_eta, p1_phi, p1_mass);
  p2.SetPtEtaPhiM(p2_pt, p2_eta, p2_phi, p2_mass);
  return (p1+p2).M();
}

float invariantMassPt(float p1_pt, float p1_eta, float p1_phi, float p1_mass, float p2_pt, float p2_eta, float p2_phi, float p2_mass) {
  if(p1_pt<0. || p2_pt<0.) return -1.;
  TLorentzVector p1;
  TLorentzVector p2;
  p1.SetPtEtaPhiM(p1_pt, p1_eta, p1_phi, p1_mass);
  p2.SetPtEtaPhiM(p2_pt, p2_eta, p2_phi, p2_mass);
  return (p1+p2).Pt();
}


float vectorSumPhi(float px1, float py1, float px2, float py2){
  float phi = atan((py1+py2)/(px1+px2));
  if ((px1+px2)>0) return phi;
  else if ((py1+py2)>0) return phi + 3.14159265;
  else return phi - 3.14159265;
}


float vectorSumPt(float pt1, float phi1, float pt2, float phi2){
  return sqrt( pow(pt1*cos(phi1) + pt2*cos(phi2),2) +
	       pow(pt1*sin(phi1) + pt2*sin(phi2),2) );
}

float vectorSum3Pt(float pt1, float phi1, float pt2, float phi2,float pt3, float phi3){
  return sqrt( pow(pt1*cos(phi1) + pt2*cos(phi2) + pt3*cos(phi3),2) +
	       pow(pt1*sin(phi1) + pt2*sin(phi2) + pt3*sin(phi3),2) );
}

float vectorSumMass(float px1, float py1, float pz1, float px2, float py2, float pz2) {
  //double E1 = sqrt(px1**2 + py1**2 + pz1**2);
  //double E2 = sqrt(px2**2 + py2**2 + pz2**2);
  double E1 = sqrt(px1*2 + py1*2 + pz1*2);
  double E2 = sqrt(px2*2 + py2*2 + pz2*2);
  double cosTheta = (px1*px2 + py1*py2 + pz1*pz2)/ (E1*E2);
  return sqrt(2*E1*E2*(1-cosTheta));
}

float transverseMass(float lepPt, float lepPhi, float met,  float metPhi) {
  double cosDPhi = cos(deltaPhi(lepPhi,metPhi));
  return sqrt(2*lepPt*met*(1-cosDPhi));
}

float caloMet1l(float pt, float phi, float met, float metPhi){
  return sqrt( pow(pt*cos(phi) + met*cos(metPhi),2) +
	       pow(pt*sin(phi) + met*sin(metPhi),2));
}

float caloMet2l(float pt1, float phi1, float pt2, float phi2, float met, float metPhi){
  return sqrt( pow(pt1*cos(phi1) + pt2*cos(phi2) + met*cos(metPhi),2) +
	       pow(pt1*sin(phi1) + pt2*sin(phi2) + met*sin(metPhi),2));
}

float A_tmass(float met_pt, float met_phi, float j_pt, float j_eta, float j_phi, float j_mass) {
  TLorentzVector h, Z;
  h.SetPtEtaPhiM(j_pt, j_eta, j_phi, j_mass);
  Z.SetPtEtaPhiM(met_pt, 0., met_phi, 0.);
  return TMath::Sqrt( 2.*h.Energy()*met_pt*(1.-TMath::Cos( h.DeltaPhi(Z) )) );
}

float A_cmass(float met_pt, float met_phi, float j_pt, float j_eta, float j_phi, float j_mass) {
  TLorentzVector h, Z;
  h.SetPtEtaPhiM(j_pt, j_eta, j_phi, j_mass);
  Z.SetPtEtaPhiM(met_pt, -j_eta, met_phi, 91.18);
  //Z.SetPz(-h.Pz());
  return (h+Z).M();
}
