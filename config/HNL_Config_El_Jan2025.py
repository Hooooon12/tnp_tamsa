from tnpConfig import tnpConfig

############## samples ################
samples={

    'data2016a':'/gv0/DATA/SKFlat/Run2UltraLegacy_v3/2016preVFP/DATA_SkimTree_EGammaTnP_HEEP/SingleElectron',
    'amc2016a':'/gv0/DATA/SKFlat/Run2UltraLegacy_v3/2016preVFP/MC_SkimTree_EGammaTnP_HEEP/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8',
    'mg2016a':'/gv0/DATA/SKFlat/Run2UltraLegacy_v3/2016preVFP/MC_SkimTree_EGammaTnP_HEEP/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
    'pwg2016a':'/gv0/DATA/SKFlat/Run2UltraLegacy_v3/2016preVFP/MC_SkimTree_EGammaTnP_HEEP/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos',

    'data2016b':'/gv0/DATA/SKFlat/Run2UltraLegacy_v3/2016postVFP/DATA_SkimTree_EGammaTnP_HEEP/SingleElectron',
    'amc2016b':'/gv0/DATA/SKFlat/Run2UltraLegacy_v3/2016postVFP/MC_SkimTree_EGammaTnP_HEEP/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8',
    'mg2016b':'/gv0/DATA/SKFlat/Run2UltraLegacy_v3/2016postVFP/MC_SkimTree_EGammaTnP_HEEP/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
    'pwg2016b':'/gv0/DATA/SKFlat/Run2UltraLegacy_v3/2016postVFP/MC_SkimTree_EGammaTnP_HEEP/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos',

    'data2017':'/gv0/DATA/SKFlat/Run2UltraLegacy_v3/2017/DATA_SkimTree_EGammaTnP_HEEP/SingleElectron',
    'amc2017':'/gv0/DATA/SKFlat/Run2UltraLegacy_v3/2017/MC_SkimTree_EGammaTnP_HEEP/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8',
    'mg2017':'/gv0/DATA/SKFlat/Run2UltraLegacy_v3/2017/MC_SkimTree_EGammaTnP_HEEP/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
    'pwg2017':'/gv0/DATA/SKFlat/Run2UltraLegacy_v3/2017/MC_SkimTree_EGammaTnP_HEEP/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos',
    'dataPOG2017':'/data6/Users/jihkim/tnp_tamsa/POG_tree/2017/SingleEle_RunBCDEF', # /eos/cms/store/group/phys_egamma/asroy/Tag-and-Probe_Tree/UL2017_MINIAOD_Nm1/
    'amcPOG2017':'/data6/Users/jihkim/tnp_tamsa/POG_tree/2017/DYJetsToLL_amcatnloFXFX',
    'mgPOG2017':'/data6/Users/jihkim/tnp_tamsa/POG_tree/2017/DYJetsToLL_madgraphMLM',

    'data2018':'/gv0/DATA/SKFlat/Run2UltraLegacy_v3/2018/DATA_SkimTree_EGammaTnP_HEEP/EGamma',
    'amc2018':'/gv0/DATA/SKFlat/Run2UltraLegacy_v3/2018/MC_SkimTree_EGammaTnP_HEEP/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8',
    'mg2018':'/gv0/DATA/SKFlat/Run2UltraLegacy_v3/2018/MC_SkimTree_EGammaTnP_HEEP/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
    'pwg2018':'/gv0/DATA/SKFlat/Run2UltraLegacy_v3/2018/MC_SkimTree_EGammaTnP_HEEP/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos',

}
############## binning ################
bin_POGID = [
    { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5, -2.,-1.566, -1.479, -0.8, 0., 0.8, 1.479,1.566, 2., 2.5], 'title':'#eta_{SC}' },
    { 'var' : 'el_pt_cor' , 'type': 'float', 'bins': [20, 35, 50, 100, 200, 500], 'title':'p_{T} [GeV]' },
]
bin_POGID_LowPt = [
    { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5, -2.,-1.566, -1.479, -0.8, 0., 0.8, 1.479,1.566, 2., 2.5], 'title':'#eta_{SC}' },
    { 'var' : 'el_pt_cor' , 'type': 'float', 'bins': [10, 20], 'title':'p_{T} [GeV]' },
]
bin_POGID_2016 = [
    { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5, -2.,-1.566, -1.479, -0.8, 0., 0.8, 1.479,1.566, 2., 2.5], 'title':'#eta_{SC}' },
    { 'var' : 'el_pt_cor' , 'type': 'float', 'bins': [20, 35, 50, 100, 500], 'title':'p_{T} [GeV]' },
]
bin_POGID_LowPt_2016 = [
    { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5, -2.,-1.566, -1.479, -0.8, 0., 0.8, 1.479,1.566, 2., 2.5], 'title':'#eta_{SC}' },
    { 'var' : 'el_pt_cor' , 'type': 'float', 'bins': [10, 20], 'title':'p_{T} [GeV]' },
]
bin_ID = [
    { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5, -2., -1.566, -1.4442, -0.8, 0.0, 0.8,  1.4442, 1.566, 2., 2.5], 'title':'#eta_{SC}' },
    { 'var' : 'el_pt_cor' , 'type': 'float', 'bins': [15, 20, 35, 50, 100, 150, 200, 500], 'title':'p_{T} [GeV]' },
]
bin_Ele23 = [
    #{ 'var' : 'el_abs_sc_eta' , 'type': 'float', 'bins': [0., 0.8, 1.4442, 1.566, 2., 2.5], 'title':'|#eta_{SC}|' },
    { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5, -2., -1.566, -1.4442, -0.8, 0.0, 0.8,  1.4442, 1.566, 2., 2.5], 'title':'#eta_{SC}' },
    { 'var' : 'el_pt_cor'     , 'type': 'float', 'bins': [25, 35, 50, 100, 150, 200, 500],         'title':'p_{T} [GeV]' },
]
bin_Ele12 = [
    #{ 'var' : 'el_abs_sc_eta' , 'type': 'float', 'bins': [0., 0.8, 1.4442, 1.566, 2., 2.5], 'title':'|#eta_{SC}|' },
    { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5, -2., -1.566, -1.4442, -0.8, 0.0, 0.8,  1.4442, 1.566, 2., 2.5], 'title':'#eta_{SC}' },
    { 'var' : 'el_pt_cor'     , 'type': 'float', 'bins': [15, 25, 35, 50, 100, 150, 200, 500],        'title':'p_{T} [GeV]' },
]


############### Expr ################
## selection
mcTrue='mcTrue'
mcTrue_dRp1='mcTrue && (el_eta-mc_probe_eta)*(el_eta-mc_probe_eta)+(el_phi-mc_probe_phi)*(el_phi-mc_probe_phi)<0.01'
medium_dRp1dPtRelp2='mcTrue && el_et/mc_probe_et>0.8 && el_et/mc_probe_et < 1.2 && (el_eta-mc_probe_eta)*(el_eta-mc_probe_eta)+(el_phi-mc_probe_phi)*(el_phi-mc_probe_phi)<0.01'

VetoGap      = ''
VetoGapTag   = ' && (abs(tag_sc_eta)<1.442 || abs(tag_sc_eta)>1.566)'
EtaTag       = ' && abs(tag_sc_eta) < 2.17 '
MTCutTag     = ' && sqrt( 2*event_met_pfmet*tag_Ele_pt_cor*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45'
MVATag       = ' && tag_Ele_IsoMVA94XV2 > 0.92'
TagHLTEle16  = ' && tag_passHltEle27WPTightGsf '
TagHLTEle17  = ' && tag_passHltEle32DoubleEGWPTightGsf && tag_passEGL1SingleEGOr '
TagHLTEle18  = ' && tag_passHltEle32WPTightGsf '
TagCutBase27 = 'tag_Ele_pt_cor>30 && el_q*tag_Ele_q<0  '+VetoGapTag + MTCutTag
TagCutBase32 = 'tag_Ele_pt_cor>35 && el_q*tag_Ele_q<0  '+VetoGapTag + MTCutTag
TightTagCutBase27 = 'tag_Ele_pt_cor>30 && el_q*tag_Ele_q<0  '+VetoGapTag +MTCutTag + MVATag
TightTagCutBase32 = 'tag_Ele_pt_cor>35 && el_q*tag_Ele_q<0  '+VetoGapTag +MTCutTag + MVATag
POGTagCutBase32 = 'tag_Ele_pt_cor>35 && el_q*tag_Ele_q<0  '+EtaTag # https://indico.cern.ch/event/879921/contributions/3825888/attachments/2022029/3381339/Approval_UL17_EleIDSFs_hjkwon.pdf --> no MTCut
POGTagCutBase32MVA = 'tag_Ele_pt_cor>35 && el_q*tag_Ele_q<0  '+EtaTag + MVATag # https://indico.cern.ch/event/879921/contributions/3825888/attachments/2022029/3381339/Approval_UL17_EleIDSFs_hjkwon.pdf --> no MTCut

#ID to test

#HNL_ULID   = 'passingHNLMVA ' +VetoGap
HNL_ULID   = 'passingHNLMVA_HighPt ' +VetoGap
HNTightV2  = 'passingHNTightV2 ' +VetoGap
MediumID   = 'passingCutBasedMedium94XV2 '+VetoGap
TightID   = 'passingCutBasedTight94XV2 '+VetoGap
 
HNL_ULID_CF  = 'passingHNLMVACF ' +VetoGap
HNL_ULID_CFT ='(scoreHNLMVACF > 0.5) ' +VetoGap
HNL_ULID_CFM ='(scoreHNLMVACF > 0.4) ' +VetoGap
HNL_ULID_CFL ='(scoreHNLMVACF > 0.3) ' +VetoGap
HNL_ULID_FAKE   = '(passingHNLMVAFake) ' +VetoGap
HNL_ULID_FAKEL = '(scoreHNLMVAFake > 0.2) ' +VetoGap
HNL_ULID_CONV  = '(passingHNLMVAConv) ' +VetoGap
HNL_ULID_CONVT ='(scoreHNLMVAConv > -0.7) ' +VetoGap
HNL_ULID_CONVM ='(scoreHNLMVAConv > -0.4) ' +VetoGap
HNL_ULID_CONVL ='(scoreHNLMVAConv > -0.2) ' +VetoGap

#HLT to test
HLTEl23 = 'passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1 && el_l1et > L1ThresholdHLTEle23Ele12CaloIdLTrackIdLIsoVL'
HLTEl12 = 'passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2'

## fits
fit_nominal = [
    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[0.1,0.1,4.0])",
    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[0.02,0.02,0.7])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "RooCMSShape::bkgPass(x, aCMSP[50.,40.,80.],bCMSP[0.1, 0.01,0.25],cCMSP[0.05, 0.0001,0.2],peakCMSP[90.0])",
    "RooCMSShape::bkgFail(x, aCMSF[50.,40.,80.],bCMSF[0.1, 0.01,0.25],cCMSF[0.05, 0.0001,0.2],peakCMSF[90.0])",

]

fit_altsig = [

    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
    "RooCBShape::sigResPass(x,meanP[-0.0,-5.0,5.0],sigmaP[1,0.5,10.0],alphaP[2.0,1.2,3.5],nP[3,-5,5])",
    "RooCBShape::sigResFail(x,meanF[-0.0,-5.0,5.0],sigmaF[1,0.3,10.0],alphaF[2.0,1.2,3.5],nF[3,-5,5])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    #"sigFracF[0.5, 0., 1.]",
    #"Gaussian::sigGaussFail(x,meanGF[80.,70.,100.],sigmaGF[15,5.,125.])",
    "RooCMSShape::bkgPass(x, aCMSP[60., 50.,80.],bCMSP[0.03, 0.01,0.05],cCMSP[0.1, -0.1,1.0],peakCMSP[90.0])",
    "RooCMSShape::bkgFail(x, aCMSF[61.5, 50.,80.],bCMSF[0.03, 0.01,0.05],cCMSF[0.03, -0.1,1.0],peakCMSF[90.0])",
]

fit_altbkg = [
    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[0.02,0.02,4.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "Exponential::bkgPass(x, alphaP[0.,-5.,5.])",
    "Exponential::bkgFail(x, alphaF[0.,-5.,5.])",
]

#fit_altbkg = [
#    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
#    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
#    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
#    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[3.,0.,10.0])",
#    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
#    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
#    "Exponential::bkgPass(x, alphaP[0.,-5.,5.])",
#    "Exponential::bkgFail(x, alphaF[-1.,-2.,2])",
#] # trial 1

#fit_altbkg = [
#    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
#    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
#    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
#    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[0.02,0.02,4.0])",
#    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
#    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
#    "Exponential::bkgPass(x, alphaP[0.,-5.,5.])",
#    "Exponential::bkgFail(x, alphaF[-1.,-2.,-0.04])",
#] # trial 2

#fit_altbkg = [
#    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
#    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
#    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
#    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[0.02,0.02,4.0])",
#    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
#    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
#    "Exponential::bkgPass(x, alphaP[0.,-5.,5.])",
#    "Exponential::bkgFail(x, alphaF[-1.,-5.,-0.05])",
#] # trial 3

#fit_altbkg = [
#    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
#    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
#    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
#    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[0.02,0.02,4.0])",
#    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
#    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
#    "Exponential::bkgPass(x, alphaP[0.,-5.,5.])",
#    "Exponential::bkgFail(x, alphaF[-1.,-5.,-0.06])",
#] # trial 4

#fit_altbkg = [
#    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
#    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
#    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
#    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[0.02,0.02,4.0])",
#    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
#    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
#    "Exponential::bkgPass(x, alphaP[0.,-5.,5.])",
#    "Exponential::bkgFail(x, alphaF[-1.,-5.,-0.042])",
#] # trial 5

#fit_altbkg = [
#    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
#    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
#    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
#    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[0.02,0.02,0.5])",
#    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
#    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
#    "Exponential::bkgPass(x, alphaP[0.,-5.,5.])",
#    "Exponential::bkgFail(x, alphaF[-1.,-5.,-0.042])",
#] # trial 6

#fit_altbkg = [
#    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
#    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
#    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
#    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[0.015,0.01,0.2])",
#    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
#    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
#    "Exponential::bkgPass(x, alphaP[0.,-5.,5.])",
#    "Exponential::bkgFail(x, alphaF[-1.,-5.,-0.042])",
#] # trial 7

#fit_altbkg = [
#    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
#    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
#    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
#    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[0.02,0.01,1.5])",
#    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
#    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
#    "Exponential::bkgPass(x, alphaP[0.,-5.,5.])",
#    "Exponential::bkgFail(x, alphaF[-1.,-5.,-0.042])",
#] # trial 8

#fit_altbkg = [
#    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
#    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
#    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
#    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[2,1.5,2.5])",
#    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
#    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
#    "Exponential::bkgPass(x, alphaP[0.,-5.,5.])",
#    "Exponential::bkgFail(x, alphaF[-1.,-5.,-0.042])",
#] # trial 9

#fit_altbkg = [
#    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
#    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
#    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
#    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[3,2.5,3.5])",
#    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
#    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
#    "Exponential::bkgPass(x, alphaP[0.,-5.,5.])",
#    "Exponential::bkgFail(x, alphaF[-1.,-5.,-0.042])",
#] # trial 10

#fit_altbkg = [
#    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
#    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
#    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
#    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[4,3.5,4.5])",
#    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
#    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
#    "Exponential::bkgPass(x, alphaP[0.,-5.,5.])",
#    "Exponential::bkgFail(x, alphaF[-1.,-5.,-0.042])",
#] # trial 11

#fit_altbkg = [
#    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
#    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
#    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
#    "RooCBShape::sigResFail(x,meanF[-0.0,-5.0,5.0],sigmaF[1,0.3,10.0],alpha_CB_F[2.0,1.2,3.5],nF[3,-5,5])",
#    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
#    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
#    "Exponential::bkgPass(x, alphaP[0.,-5.,5.])",
#    "Exponential::bkgFail(x, alphaF[0.,-5.,5.])",
#] # CB

#fit_altbkg = [
#    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
#    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
#    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
#    "RooCBShape::sigResFail(x,meanF[-0.0,-5.0,5.0],sigmaF[1,0.3,10.0],alpha_CB_F[2.0,1.2,3.5],nF[3,-5,5])",
#    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
#    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
#    "Exponential::bkgPass(x, alphaP[0.,-5.,5.])",
#    "RooCMSShape::bkgFail(x, aCMSF[50.,40.,80.],bCMSF[0.1, 0.01,0.25],cCMSF[0.05, 0.0001,0.2],peakCMSF[90.0])",
#] # Superior RooCMS

########### Configs ##############
Configs={}

#### 2016a
## ID
config=tnpConfig(
    data=samples['data2016a'],
    sim=samples['pwg2016a'],
    sim_weight='weight*PUweight*prefireweight',
    sim_maxweight=10000.,
    sim_genmatching=mcTrue_dRp1,
    sim_genmass="mcMass",
    tree='tnpEleIDs/fitter_tree',
    mass="pair_mass_cor",
    bins=bin_ID,
    expr='( '+POGTagCutBase32+TagHLTEle16+' )',
    test= HNL_ULID,
    hist_nbins=62,
    hist_range=(59,121),
    method="fit",
    fit_parameter=fit_nominal,
    fit_range=(60,120),
    systematic=[
      [{'title':'altbkg','fit_parameter':fit_altbkg}],
      [{'title':'altsig','fit_parameter':fit_altsig}],
      [{'title':'alttag','expr.replace':('tag_Ele_pt_cor>','tag_Ele_pt_cor>5+')}],
      [{'title':'altmc','sim.replace':('DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8','DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8')}],
      [{'title':'PUweight_up','sim_weight.replace':('PUweight','PUweight_up')},{'title':'PUweight_down','sim_weight.replace':('PUweight','PUweight_down')}],
      [{'title':'prefireweight_up','sim_weight.replace':('prefireweight','prefireweight_up')},{'title':'prefireweight_down','sim_weight.replace':('prefireweight','prefireweight_down')}],
      [{"title": "fitwindowup", "fit_range": (63, 123)}, {"title": "fitwindowdown", "fit_range": (57, 117)}],
    ],
    option="", #"fix_ptbelow20",
)
Configs['HNL_2016a']=config.clone(test=HNL_ULID,        bins=bin_ID)
Configs['HNTightV2_2016a']=config.clone(test=HNTightV2, bins=bin_ID)
Configs['HNL_CF_2016a']=config.clone(test=HNL_ULID_CF,  bins=bin_ID)
Configs['HNL_Conv_2016a']=config.clone(test=HNL_ULID_CONV, bins=bin_ID)
Configs['HNL_Fake_2016a']=config.clone(test=HNL_ULID_FAKE, bins=bin_ID)
Configs['MediumID_2016a']=config.clone(test=MediumID,      bins=bin_ID)
Configs['TightID_2016a']=config.clone(test=TightID,      bins=bin_POGID_2016)
Configs['TightID_LowPt_2016a']=config.clone(test=TightID,      bins=bin_POGID_LowPt_2016)
Configs['TightID_POGsample_2016a']=config.clone(test=TightID,      bins=bin_POGID_2016)
Configs['TightID_POGsample_LowPt_2016a']=config.clone(test=TightID,      bins=bin_POGID_LowPt_2016)

### trigger ###
config_trig=config.clone( tree='tnpEleTrig/fitter_tree' )
Configs['Ele23Leg1_HNL_ULID_2016a']=config_trig.clone(bins=bin_Ele23, test=HLTEl23,  expr='( '+POGTagCutBase32+TagHLTEle16+' && '+HNL_ULID+' )')
Configs['Ele12Leg2_HNL_ULID_2016a']=config_trig.clone(bins=bin_Ele12, test=HLTEl12,  expr='( '+POGTagCutBase32+TagHLTEle16+' && '+HNL_ULID+' )')
Configs['Ele23Leg1_HNTightV2_2016a']=config_trig.clone(bins=bin_Ele23, test=HLTEl23, expr='( '+POGTagCutBase32+TagHLTEle16+' && '+HNTightV2+' )')
Configs['Ele12Leg2_HNTightV2_2016a']=config_trig.clone(bins=bin_Ele12, test=HLTEl12, expr='( '+POGTagCutBase32+TagHLTEle16+' && '+HNTightV2+' )')
Configs['Ele23Leg1_MediumID_2016a']=config_trig.clone(bins=bin_Ele23, test=HLTEl23,  expr='( '+TagCutBase27+' && '+MediumID+' )')
Configs['Ele12Leg2_MediumID_2016a']=config_trig.clone(bins=bin_Ele12, test=HLTEl12,  expr='( '+TagCutBase27+' && '+MediumID+' )')



### 2016b, 2017, 2018 #################################################
Configs_2016b={}
Configs_2017 ={}
Configs_2018 ={}
for key in Configs:
  if not "_2016a" in key: continue

  Configs_2016b[key.replace("_2016a","_2016b")]=Configs[key].clone(data=samples["data2016b"],sim=samples["pwg2016b"])
  if 'Ele23Leg1_' in key or 'Ele12Leg2_' in key:
    Configs_2017[key.replace("_2016a","_2017" )]=Configs[key].clone(
       data=samples["data2017"],
       sim=samples["pwg2017"],
       expr='( '+POGTagCutBase32+TagHLTEle17+' && '+globals()[key.replace('_2016a','').replace('Ele23Leg1_','').replace('Ele12Leg2_','')]+')',
    )
    #print " "
    #print ('Configs_2017 exp = ' + TagCutBase32+TagHLTEle17+' && '+globals()[key.replace('_2016a','').replace('Ele23Leg1_','').replace('Ele12Leg2_','')])
    #print " "
    Configs_2018[key.replace("_2016a","_2018" )]=Configs[key].clone(
       data=samples["data2018"],
       sim=samples["pwg2018"],
       expr='( '+POGTagCutBase32+TagHLTEle18+' && '+globals()[key.replace('_2016a','').replace('Ele23Leg1_','').replace('Ele12Leg2_','')]+')',
    )
  elif 'TightID' in key: # POG reproduction
    if 'POGsample' in key: # only 2017 for now
      if 'LowPt' in key:
        Configs_2017[key.replace("_2016a","_2017" )]=Configs[key].clone(
								data=samples["dataPOG2017"],
								sim=samples["mgPOG2017"],
								bins=bin_POGID_LowPt,
								expr='('+POGTagCutBase32MVA+TagHLTEle17+')',
				)
      else:
        Configs_2017[key.replace("_2016a","_2017" )]=Configs[key].clone(
								data=samples["dataPOG2017"],
								sim=samples["mgPOG2017"],
								bins=bin_POGID,
								expr='('+POGTagCutBase32+TagHLTEle17+')')
    else:
      if 'LowPt' in key:
        Configs_2017[key.replace("_2016a","_2017" )]=Configs[key].clone(data=samples["data2017"], sim=samples["pwg2017"], bins=bin_POGID_LowPt, expr='('+POGTagCutBase32MVA+TagHLTEle17+')')
        Configs_2018[key.replace("_2016a","_2018" )]=Configs[key].clone(data=samples["data2018"], sim=samples["pwg2018"], bins=bin_POGID_LowPt, expr='('+POGTagCutBase32MVA+TagHLTEle18+')')
      else:
        Configs_2017[key.replace("_2016a","_2017" )]=Configs[key].clone(data=samples["data2017"], sim=samples["pwg2017"], bins=bin_POGID, expr='('+POGTagCutBase32+TagHLTEle17+')')
        Configs_2018[key.replace("_2016a","_2018" )]=Configs[key].clone(data=samples["data2018"], sim=samples["pwg2018"], bins=bin_POGID, expr='('+POGTagCutBase32+TagHLTEle18+')')
  else:
    Configs_2017[key.replace("_2016a","_2017" )]=Configs[key].clone(data=samples["data2017"], sim=samples["pwg2017"], expr='('+POGTagCutBase32+TagHLTEle17+')')
    Configs_2018[key.replace("_2016a","_2018" )]=Configs[key].clone(data=samples["data2018"], sim=samples["pwg2018"], expr='('+POGTagCutBase32+TagHLTEle18+')')

#print Configs_2018    
Configs.update(Configs_2016b)
Configs.update(Configs_2017)
Configs.update(Configs_2018)
#######################################################################



if __name__=="__main__":
    for key in sorted(Configs.keys()):
        print key
