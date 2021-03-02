import ROOT

ROOT.gROOT.SetBatch(True)

file_name = 'GG_rpv_UDS_1600.root'
f = ROOT.TFile.Open(file_name,'READ')
t = f.Get('trees_SRRPV_')

h_quarks = ROOT.TH1F('h_quarks', 'h_quarks', 30, -0.5, 29.5)
t.Draw('jet_QGTagger_NTracks >> h_quarks', '((jet_PartonTruthLabelID<5)*(normweight*mcEventWeight))', 'goff')

# here: same for gluons

# here: 

c = ROOT.TCanvas()
c.cd()
h_quarks.SetLineColor(ROOT.kPink)
# here: name axis

h_quarks.Draw('hist')
# here: same for gluons
# remember to add also the option 'same' when drawing

# here: add legend

c.SaveAs('ntracks.png')
