from ROOT import *

eras = ["2016preVFP","2016postVFP","2017","2018"]
#eras = ["2017","2018"]

this_highpt_sf_file = []
this_highpt_sf_file.append(TFile.Open("/data6/Users/jihkim/tnp_tamsa/results/HNL_Config_El_MedCh/TightID_2016a/efficiency.root"))
this_highpt_sf_file.append(TFile.Open("/data6/Users/jihkim/tnp_tamsa/results/HNL_Config_El_MedCh/TightID_2016b/efficiency.root"))
this_highpt_sf_file.append(TFile.Open("/data6/Users/jihkim/tnp_tamsa/results/HNL_Config_El_MedCh/TightID_2017/efficiency.root"))
this_highpt_sf_file.append(TFile.Open("/data6/Users/jihkim/tnp_tamsa/results/HNL_Config_El_MedCh/TightID_2018/efficiency.root"))

this_lowpt_sf_file = []
this_lowpt_sf_file.append(TFile.Open("/data6/Users/jihkim/tnp_tamsa/results/HNL_Config_El_MedCh/TightID_LowPt_2016a/efficiency.root"))
this_lowpt_sf_file.append(TFile.Open("/data6/Users/jihkim/tnp_tamsa/results/HNL_Config_El_MedCh/TightID_LowPt_2016b/efficiency.root"))
this_lowpt_sf_file.append(TFile.Open("/data6/Users/jihkim/tnp_tamsa/results/HNL_Config_El_MedCh/TightID_LowPt_2017/efficiency.root"))
this_lowpt_sf_file.append(TFile.Open("/data6/Users/jihkim/tnp_tamsa/results/HNL_Config_El_MedCh/TightID_LowPt_2018/efficiency.root"))

POG_sf_file = []
POG_sf_file.append(TFile.Open("/data6/Users/jihkim/SKFlatAnalyzer/data/Run2UltraLegacy_v3/2016preVFP/ID/Electron/egammaEffi.txt_Ele_Tight_preVFP_EGM2D.root"))
POG_sf_file.append(TFile.Open("/data6/Users/jihkim/SKFlatAnalyzer/data/Run2UltraLegacy_v3/2016postVFP/ID/Electron/egammaEffi.txt_Ele_Tight_postVFP_EGM2D.root"))
POG_sf_file.append(TFile.Open("/data6/Users/jihkim/SKFlatAnalyzer/data/Run2UltraLegacy_v3/2017/ID/Electron/egammaEffi.txt_EGM2D_Tight_UL17.root"))
POG_sf_file.append(TFile.Open("/data6/Users/jihkim/SKFlatAnalyzer/data/Run2UltraLegacy_v3/2018/ID/Electron/egammaEffi.txt_Ele_Tight_EGM2D.root"))

out = TFile.Open("./comparison.root","recreate")
for iera in range(len(eras)):
  this_highpt_sf_hist = this_highpt_sf_file[iera].Get("sf")
  this_lowpt_sf_hist = this_lowpt_sf_file[iera].Get("sf")
  POG_sf_hist = POG_sf_file[iera].Get("EGamma_SF2D")
  
  #print this_highpt_sf_hist.GetNbinsX()
  #print this_highpt_sf_hist.GetNbinsY()
  #
  #print POG_sf_hist.GetNbinsX()
  #print POG_sf_hist.GetNbinsY()
 
  this_sf_hist = POG_sf_hist.Clone()
  for i in range(POG_sf_hist.GetNbinsX()):
    this_sf_hist.SetBinContent(i+1,1,this_lowpt_sf_hist.GetBinContent(i+1,1))
    this_sf_hist.SetBinError(i+1,1,this_lowpt_sf_hist.GetBinError(i+1,1))
    for j in range(this_highpt_sf_hist.GetNbinsY()):
      this_sf_hist.SetBinContent(i+1,j+2,this_highpt_sf_hist.GetBinContent(i+1,j+1))
      this_sf_hist.SetBinError(i+1,j+2,this_highpt_sf_hist.GetBinError(i+1,j+1))
  
  #for i in range(POG_sf_hist.GetNbinsX()):
  #  for j in range(POG_sf_hist.GetNbinsY()):
  #    print this_sf_hist.GetBinContent(i+1,j+1)
  #    if j==0: print this_lowpt_sf_hist.GetBinContent(i+1,1)
  #    else: print this_highpt_sf_hist.GetBinContent(i+1,j)
  
  this_sf_hist_comp = this_sf_hist.Clone()
  this_sf_hist_comp.Divide(POG_sf_hist)
  this_sf_hist_comp.SetNameTitle(eras[iera]+"_comparison","Reprod/POG")
  
  for i in range(this_sf_hist_comp.GetNbinsX()):
    for j in range(this_sf_hist_comp.GetNbinsY()):
      this_sf_hist_comp.SetBinError(i+1,j+1,abs(this_sf_hist.GetBinContent(i+1,j+1)-POG_sf_hist.GetBinContent(i+1,j+1))/POG_sf_hist.GetBinError(i+1,j+1))
  
  #print type(this_sf_hist)
  #for i in range(POG_sf_hist.GetNbinsX()):
  #  for j in range(POG_sf_hist.GetNbinsY()):
  #    print POG_sf_hist.GetBinError(i+1,j+1)
  
  this_sf_hist.SetName(eras[iera]+"_Reprod")
  this_sf_hist.Write()
  POG_sf_hist.SetName(eras[iera]+"_POG")
  POG_sf_hist.Write()
  this_sf_hist_comp.Write()

  #del this_sf_hist
  #del POG_sf_hist
  #del this_sf_hist_comp
