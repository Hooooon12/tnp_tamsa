#include <iostream>

TString workdir = "/data6/Users/helee/working_HN_Plotter/";
TString tnpdir  = "/data6/Users/helee/MuonTnP/tnp_tamsa/";
TString filedir = "";
TString IDName  = "HNL_ULID";
TString tnpVersion = "v1";
TString dirName = "";
vector<TString> year = {"2016a", "2016b", "2017", "2018"};
vector<TString> luminosity = {"19.52", "16.81", "41.48", "59.83"};
//vector<TString> year = {"2016a"};
//vector<TString> luminosity = {"19.52"};

const int yearNumber = year.size();
const int etaNumber = 4;
double binContent = 0., binError = 0.;
double minRangeX = 0., maxRangeX = 0., minRangeY = 0., maxRangeY = 0.;


void makePlots_muonIDEff_era(TString objName, TString plotVersion){

  // Command : root -b -l -q 'makePlots_muonIDEff_era.C("ID", "all")'
  // objName = "ID", "Mu17", "Mu8"
  // plotVersion = "all", "barrel", "endcap"

  //==== obj-dependent variables
  vector<double> bin_pt = {10., 15., 20., 25., 30., 40., 50., 60., 120., 200.};
  dirName = "NUM_HNL_ULID_DEN_TrackerMuons";
  if(objName == "Mu17"){
    bin_pt = {10., 16., 18., 20., 25., 30., 40., 50., 100., 200.};
    dirName = "NUM_Mu17Leg1_DEN_HNL_ULID";
  }
  if(objName == "Mu8"){
    bin_pt = {10., 15., 20., 25., 30., 40., 50., 100., 200.};
    dirName = "NUM_Mu8Leg2_DEN_HNL_ULID";
  }

  const int binNumber = bin_pt.size()-1;
  double *bins = bin_pt.data();

  //==== Declare variables needed to make plots 
  TFile *f_eff[yearNumber];
  TH2D *h_Data[yearNumber], *h_MC[yearNumber], *h_SF2D[yearNumber];
  TH1D *h_eff1[etaNumber][yearNumber], *h_eff2[etaNumber][yearNumber], *h_ratio[etaNumber][yearNumber];
  TH1D *h_Eff[etaNumber][yearNumber], *h_SF[etaNumber][yearNumber];
  TCanvas *c1;
  TPad *c_up, *c_down;
  TLegend *lg;

  double eff_data = 0., err_data = 0., eff_mc = 0., err_mc = 0., eff_sf = 0., err_sf = 0.;

  //==== Year loop
  for(int it_y=0; it_y<year.size(); it_y++){

    filedir = "results/HNL_Muon_"+tnpVersion+"/"+dirName+"_"+year.at(it_y);

    //=========================================
    //==== Set input ROOT files
    //=========================================

    f_eff[it_y] = new TFile(tnpdir+filedir+"/efficiency.root");

    //=========================================
    //==== Get histograms
    //=========================================

    //==== DATA
    h_Data[it_y] = (TH2D*)f_eff[it_y]->Get("data");
    h_MC[it_y] = (TH2D*)f_eff[it_y]->Get("sim");
    h_SF2D[it_y] = (TH2D*)f_eff[it_y]->Get("sf");

    h_Data[it_y]->SetDirectory(0);
    h_MC[it_y]->SetDirectory(0);
    h_SF2D[it_y]->SetDirectory(0);

    f_eff[it_y]->Close();

    //=========================================
    //==== Make plots
    //=========================================

    //==== Make 1D histograms from 2D histograms

    for(int it_e=0; it_e<etaNumber; it_e++){

      h_eff1[it_e][it_y] = new TH1D("h_eff1_"+TString::Itoa(it_e, 10)+"_"+TString::Itoa(it_y, 10), "", binNumber, bins);
      h_eff2[it_e][it_y] = new TH1D("h_eff2_"+TString::Itoa(it_e, 10)+"_"+TString::Itoa(it_y, 10), "", binNumber, bins);
      h_ratio[it_e][it_y] = new TH1D("h_ratio_"+TString::Itoa(it_e, 10)+"_"+TString::Itoa(it_y, 10), "", binNumber, bins);

      for(int it_b=0; it_b<binNumber; it_b++){

        eff_data = h_Data[it_y]->GetBinContent(it_e+1, it_b+1);
        err_data = h_Data[it_y]->GetBinError(it_e+1, it_b+1);
        eff_mc = h_MC[it_y]->GetBinContent(it_e+1, it_b+1);
        err_mc = h_MC[it_y]->GetBinError(it_e+1, it_b+1);
        eff_sf = h_SF2D[it_y]->GetBinContent(it_e+1, it_b+1);
        err_sf = h_SF2D[it_y]->GetBinError(it_e+1, it_b+1);

        h_eff1[it_e][it_y]->SetBinContent(it_b+1, eff_data);
        h_eff1[it_e][it_y]->SetBinError(it_b+1, err_data);
        h_eff2[it_e][it_y]->SetBinContent(it_b+1, eff_mc);
        h_eff2[it_e][it_y]->SetBinError(it_b+1, err_mc);
        h_ratio[it_e][it_y]->SetBinContent(it_b+1, eff_sf);
        h_ratio[it_e][it_y]->SetBinError(it_b+1, err_sf);

      }

    }

    h_Eff[0][it_y] = (TH1D*)h_eff1[0][it_y]->Clone();
    h_Eff[1][it_y] = (TH1D*)h_eff1[1][it_y]->Clone();
    h_Eff[2][it_y] = (TH1D*)h_eff1[2][it_y]->Clone();
    h_Eff[3][it_y] = (TH1D*)h_eff1[3][it_y]->Clone();
    if(plotVersion == "barrel"){
      h_Eff[0][it_y] = (TH1D*)h_eff1[0][it_y]->Clone();
      h_Eff[1][it_y] = (TH1D*)h_eff2[0][it_y]->Clone();
      h_Eff[2][it_y] = (TH1D*)h_eff1[1][it_y]->Clone();
      h_Eff[3][it_y] = (TH1D*)h_eff2[1][it_y]->Clone();
    }
    if(plotVersion == "endcap"){
      h_Eff[0][it_y] = (TH1D*)h_eff1[2][it_y]->Clone();
      h_Eff[1][it_y] = (TH1D*)h_eff2[2][it_y]->Clone();
      h_Eff[2][it_y] = (TH1D*)h_eff1[3][it_y]->Clone();
      h_Eff[3][it_y] = (TH1D*)h_eff2[3][it_y]->Clone();
    }

    h_SF[0][it_y] = (TH1D*)h_ratio[0][it_y]->Clone();
    h_SF[1][it_y] = (TH1D*)h_ratio[1][it_y]->Clone();
    h_SF[2][it_y] = (TH1D*)h_ratio[2][it_y]->Clone();
    h_SF[3][it_y] = (TH1D*)h_ratio[3][it_y]->Clone();
    if(plotVersion == "barrel"){
      h_SF[0][it_y] = (TH1D*)h_ratio[0][it_y]->Clone();
      h_SF[1][it_y] = (TH1D*)h_ratio[1][it_y]->Clone();
      h_SF[2][it_y] = (TH1D*)h_ratio[0][it_y]->Clone();
      h_SF[3][it_y] = (TH1D*)h_ratio[1][it_y]->Clone();
    }
    if(plotVersion == "endcap"){
      h_SF[0][it_y] = (TH1D*)h_ratio[2][it_y]->Clone();
      h_SF[1][it_y] = (TH1D*)h_ratio[3][it_y]->Clone();
      h_SF[2][it_y] = (TH1D*)h_ratio[2][it_y]->Clone();
      h_SF[3][it_y] = (TH1D*)h_ratio[3][it_y]->Clone();
    }

    //==== CANVAS
    c1 = new TCanvas("c1", "", 1000, 1000);
    c1->cd();

    //==== PAD : drawing distribution
    c_up = new TPad("c_up", "", 0, 0.35, 1, 1);
    c_up->SetTopMargin(0.1);
    c_up->SetBottomMargin(0.017);
    c_up->SetLeftMargin(0.14);
    c_up->SetRightMargin(0.04);
    //c_up->SetLogx();
    c_up->Draw();
    c_up->cd();

    //==== Draw Data Efficiency
    h_Eff[0][it_y]->SetTitle("");
    h_Eff[0][it_y]->SetStats(0);
    h_Eff[0][it_y]->GetXaxis()->SetLabelSize(0.);
    h_Eff[0][it_y]->GetYaxis()->SetLabelSize(0.045);
    h_Eff[0][it_y]->GetYaxis()->SetTitle("Efficiency");
    h_Eff[0][it_y]->GetYaxis()->SetTitleSize(0.075);
    h_Eff[0][it_y]->GetYaxis()->SetTitleOffset(0.8);
    h_Eff[0][it_y]->GetXaxis()->SetRangeUser(minRangeX, maxRangeX);
    h_Eff[0][it_y]->SetMinimum(0.1);
    h_Eff[0][it_y]->SetMaximum(1.2);

    h_Eff[0][it_y]->SetMarkerStyle(20);
    h_Eff[0][it_y]->SetMarkerColor(kBlack);
    h_Eff[0][it_y]->SetLineColor(kBlack);
    h_Eff[0][it_y]->SetLineStyle(1);
    if(plotVersion == "endcap"){
      h_Eff[0][it_y]->SetMarkerStyle(20);
      h_Eff[0][it_y]->SetMarkerColor(kGray+1);
      h_Eff[0][it_y]->SetLineColor(kGray+1);
      h_Eff[0][it_y]->SetLineStyle(1);
    }
    h_Eff[0][it_y]->Draw("e1p");

    h_Eff[1][it_y]->SetMarkerStyle(20);
    h_Eff[1][it_y]->SetMarkerColor(kRed+1);
    h_Eff[1][it_y]->SetLineColor(kRed+1);
    h_Eff[1][it_y]->SetLineStyle(1);
    if(plotVersion == "barrel"){
      h_Eff[1][it_y]->SetMarkerStyle(24);
      h_Eff[1][it_y]->SetMarkerColor(kBlack);
      h_Eff[1][it_y]->SetLineColor(kBlack);
      h_Eff[1][it_y]->SetLineStyle(7);
    }
    if(plotVersion == "endcap"){
      h_Eff[1][it_y]->SetMarkerStyle(24);
      h_Eff[1][it_y]->SetMarkerColor(kGray+1);
      h_Eff[1][it_y]->SetLineColor(kGray+1);
      h_Eff[1][it_y]->SetLineStyle(7);
    }
    h_Eff[1][it_y]->Draw("e1p same");

    h_Eff[2][it_y]->SetMarkerStyle(20);
    h_Eff[2][it_y]->SetMarkerColor(kGray+1);
    h_Eff[2][it_y]->SetLineColor(kGray+1);
    h_Eff[2][it_y]->SetLineStyle(1);
    if(plotVersion == "barrel"){
      h_Eff[2][it_y]->SetMarkerStyle(20);
      h_Eff[2][it_y]->SetMarkerColor(kRed+1);
      h_Eff[2][it_y]->SetLineColor(kRed+1);
      h_Eff[2][it_y]->SetLineStyle(1);
    }
    if(plotVersion == "endcap"){
      h_Eff[2][it_y]->SetMarkerStyle(20);
      h_Eff[2][it_y]->SetMarkerColor(kAzure+2);
      h_Eff[2][it_y]->SetLineColor(kAzure+2);
      h_Eff[2][it_y]->SetLineStyle(1);
    }
    h_Eff[2][it_y]->Draw("e1p same");

    h_Eff[3][it_y]->SetMarkerStyle(20);
    h_Eff[3][it_y]->SetMarkerColor(kAzure+2);
    h_Eff[3][it_y]->SetLineColor(kAzure+2);
    h_Eff[3][it_y]->SetLineStyle(1);
    if(plotVersion == "barrel"){
      h_Eff[3][it_y]->SetMarkerStyle(24);
      h_Eff[3][it_y]->SetMarkerColor(kRed+1);
      h_Eff[3][it_y]->SetLineColor(kRed+1);
      h_Eff[3][it_y]->SetLineStyle(7);
    }
    if(plotVersion == "endcap"){
      h_Eff[3][it_y]->SetMarkerStyle(24);
      h_Eff[3][it_y]->SetMarkerColor(kAzure+2);
      h_Eff[3][it_y]->SetLineColor(kAzure+2);
      h_Eff[3][it_y]->SetLineStyle(7);
    }
    h_Eff[3][it_y]->Draw("e1p same");

    //==== Draw the legend
    lg = new TLegend(0.5, 0.15, 0.9, 0.4);
    if(plotVersion == "all"){
      lg->AddEntry(h_Eff[0][it_y], "Data (0.0 #leq |#eta| #leq 0.9)", "lep");
      lg->AddEntry(h_Eff[1][it_y], "Data (0.9 #leq |#eta| #leq 1.2)", "lep");
      lg->AddEntry(h_Eff[2][it_y], "Data (1.2 #leq |#eta| #leq 2.1)", "lep");
      lg->AddEntry(h_Eff[3][it_y], "Data (2.1 #leq |#eta| #leq 2.4)", "lep");
    }
    if(plotVersion == "barrel"){
      lg->AddEntry(h_Eff[0][it_y], "Data (0.0 #leq |#eta| #leq 0.9)", "lep");
      lg->AddEntry(h_Eff[1][it_y], "MC   (0.0 #leq |#eta| #leq 0.9)", "lep");
      lg->AddEntry(h_Eff[2][it_y], "Data (0.9 #leq |#eta| #leq 1.2)", "lep");
      lg->AddEntry(h_Eff[3][it_y], "MC   (0.9 #leq |#eta| #leq 1.2)", "lep");
    }
    if(plotVersion == "endcap"){
      lg->AddEntry(h_Eff[0][it_y], "Data (1.2 #leq |#eta| #leq 2.1)", "lep");
      lg->AddEntry(h_Eff[1][it_y], "MC   (1.2 #leq |#eta| #leq 2.1)", "lep");
      lg->AddEntry(h_Eff[2][it_y], "Data (2.1 #leq |#eta| #leq 2.4)", "lep");
      lg->AddEntry(h_Eff[3][it_y], "MC   (2.1 #leq |#eta| #leq 2.4)", "lep");
    }
    lg->SetBorderSize(0);
    lg->SetTextSize(0.05);
    lg->SetFillStyle(1001);
    lg->SetShadowColor(0);
    lg->Draw("same");

    //==== Add text
    TLatex txtCMS1;
    txtCMS1.SetNDC();
    txtCMS1.SetTextSize(0.06);
    txtCMS1.SetTextAlign(11);
    txtCMS1.SetTextFont(61);
    txtCMS1.DrawLatex(.15,.93, "CMS");

    TLatex txtCMS2;
    txtCMS2.SetNDC();
    txtCMS2.SetTextSize(0.048);
    txtCMS2.SetTextAlign(11);
    txtCMS2.SetTextFont(52);
    txtCMS2.DrawLatex(.24,.93, "Preliminary");

    TLatex txt;
    txt.SetNDC();
    txt.SetTextSize(0.06);
    txt.SetTextAlign(31);
    txt.SetTextFont(42);
    txt.DrawLatex(.95,.93, luminosity.at(it_y)+" fb^{-1} (13 TeV)");

    TLatex txt2;
    txt2.SetNDC();
    txt2.SetTextSize(0.06);
    txt2.SetTextAlign(12);
    txt2.SetTextFont(62);
    txt2.DrawLatex(.18,.83, objName);

    c1->cd();

    //==== PAD : drawing SF
    c_down = new TPad("c_down", "", 0, 0, 1, 0.35);
    c_down->SetTopMargin(0.03);
    c_down->SetBottomMargin(0.27);
    c_down->SetLeftMargin(0.14);
    c_down->SetRightMargin(0.04);
    //c_down->SetGridx();
    //c_down->SetGridy();
    //c_down->SetLogx();
    c_down->Draw();
    c_down->cd();

    //==== Draw SF histograms
    h_SF[0][it_y]->SetTitle("");
    h_SF[0][it_y]->SetStats(0);
    h_SF[0][it_y]->GetXaxis()->SetTitle("p_{T} (GeV)");
    h_SF[0][it_y]->GetYaxis()->SetTitle("#frac{Data}{MC}");
    h_SF[0][it_y]->GetXaxis()->SetRangeUser(minRangeX, maxRangeX);
    h_SF[0][it_y]->GetYaxis()->SetRangeUser(0.8, 1.2);
    h_SF[0][it_y]->GetXaxis()->SetLabelSize(0.1);
    h_SF[0][it_y]->GetYaxis()->SetLabelSize(0.08);
    h_SF[0][it_y]->GetXaxis()->SetTitleSize(0.11);
    h_SF[0][it_y]->GetYaxis()->SetTitleSize(0.1);
    h_SF[0][it_y]->GetXaxis()->SetTitleOffset(1.05);
    h_SF[0][it_y]->GetYaxis()->SetTitleOffset(0.6);
    //h_SF[0][it_y]->GetXaxis()->SetMoreLogLabels();
    //h_SF[0][it_y]->GetXaxis()->SetNoExponent();

    h_SF[0][it_y]->SetMarkerStyle(20);
    h_SF[0][it_y]->SetMarkerColor(kBlack);
    h_SF[0][it_y]->SetLineColor(kBlack);
    if(plotVersion == "endcap"){
      h_SF[0][it_y]->SetMarkerColor(kGray+1);
      h_SF[0][it_y]->SetLineColor(kGray+1);
    }
    h_SF[0][it_y]->Draw("e1p");

    h_SF[1][it_y]->SetMarkerStyle(20);
    h_SF[1][it_y]->SetMarkerColor(kRed+1);
    h_SF[1][it_y]->SetLineColor(kRed+1);
    if(plotVersion == "endcap"){
      h_SF[1][it_y]->SetMarkerColor(kAzure+2);
      h_SF[1][it_y]->SetLineColor(kAzure+2);
    }
    h_SF[1][it_y]->Draw("e1p same");

    h_SF[2][it_y]->SetMarkerStyle(20);
    h_SF[2][it_y]->SetMarkerColor(kGray+1);
    h_SF[2][it_y]->SetLineColor(kGray+1);
    if(plotVersion == "all") h_SF[2][it_y]->Draw("e1p same");

    h_SF[3][it_y]->SetMarkerStyle(20);
    h_SF[3][it_y]->SetMarkerColor(kAzure+2);
    h_SF[3][it_y]->SetLineColor(kAzure+2);
    if(plotVersion == "all") h_SF[3][it_y]->Draw("e1p same");

    TLine line(minRangeX, 1., maxRangeX, 1.);
    line.SetLineWidth(2);
    line.SetLineStyle(2);
    line.SetLineColor(1);
    line.Draw();

    c1->cd();

    //=========================================
    //==== Save plots
    //=========================================

    c1->SaveAs("./results/ULv3/plots/Efficiency/Muon/"+objName+"_"+plotVersion+"_"+year.at(it_y)+".png");

    delete c_up;
    delete c_down;

    c1->Close();

    delete c1;
    delete lg;
    delete f_eff[it_y];

    delete h_Data[it_y];
    delete h_MC[it_y];
    delete h_SF2D[it_y];
    for(int it_e=0; it_e<etaNumber; it_e++){
      delete h_eff1[it_e][it_y];
      delete h_eff2[it_e][it_y];
      delete h_ratio[it_e][it_y];
      delete h_Eff[it_e][it_y];
      delete h_SF[it_e][it_y];
    }

  }  // year
}
