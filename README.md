---
layout: post
title:  "First steps in the analysis"
permalink: index.html
---

Instructions for the first studies with the ntuples for the gluino RPV multijet analysis. 

In this repo you can find 
* Introduction about the signal model
* Information about the ntuples needed to get started with quark-gluon tagging 
* Description of the tasks and examples

The questions marked with the grern square (![#1589F0](https://via.placeholder.com/15/c5f015/000000?text=+))
are meant to test your understanding while you read. 

## Signal model

The specific analysis we are going to look at is a search for gluino pair production (decaying through R-parity violating couplings), in all-hadronic final states (i.e. only hadronic jets, no leptons).
To have an idea of the type of signal we are looking at, you can take a look at the [paper](https://arxiv.org/pdf/1804.03568.pdf) of the previous iteration of the analysis. 
If you look at Figure 1 in the paper, you can see a diagram of the two signal models we are looking at.
In the first one (which I’ll refer to as “6-jets signal”), each gluino decays directly into three quarks. In the second one (10-jets signal), the gluino decays into two quarks and an intermediate neutralino, which in turn decays into three quarks. 
For the moment, we are focusing on the first signal. 

## Signal ntuples

At [this link](https://cernbox.cern.ch/index.php/s/ZeihGpj2O8v1ZVa)
(password protected, get in touch for the password)
you can find three ROOT files that you can download (total size: 38 M):
```
GG_rpv_UDS_900.root
GG_rpv_UDS_1600.root
GG_rpv_UDS_2400.root
```
Each file corresponds to a gluino signal (6-jets model) with a different gluino mass.
For each of these signals we have generated 10000 simulated events, although you
will notice that the number of events contained in the files is slightly lower
than that. This is because, in order to be written into these ROOT files, the
events need to pass a first preselection (requiring highly energetic events that
also fire the trigger that we want -- described later).

To open the ROOT files you can do e.g.:
```
root -l GG_rpv_UDS_900.root
```

The name of the TTree is `trees_SRRPV_`, so e.g. to check the number of events
stored in the TTree you can do:
```
trees_SRRPV_->GetEntries()
```

![#1589F0](https://via.placeholder.com/15/c5f015/000000?text=+)
**Question**: in the three signal files, is the number of entries the same? Can you guess why?

To see the branches of the TTree, you can do:
```
trees_SRRPV_->Show(1)
```

This will display the list of branches and
their value in the first event:

<details>
  <summary>Click to expand the list of branches!</summary>

```
 NPV             = 20
 TriggerDecisions = (vector<int>*)0x15ed400
 actualInteractionsPerCrossing = 46.5
 averageInteractionsPerCrossing = 46.5
 bcid            = 1905
 eventNumber     = 20160
 jet_PartonTruthLabelID = (vector<int>*)0x1d729e0
 jet_QGTagger_NTracks = (vector<int>*)0x1d2e6e0
 jet_QGTagger_TracksC1 = (vector<float>*)0x1d66fb0
 jet_QGTagger_TracksWidth = (vector<float>*)0x15c0e30
 jet_QGTagger_bdt = (vector<float>*)0x14c47b0
 jet_QGTagger_tagged_WPg50 = (vector<int>*)0x15bc9d0
 jet_QGTagger_tagged_WPg80 = (vector<int>*)0x14885c0
 jet_QGTagger_tagged_WPg90 = (vector<int>*)0x1c14f90
 jet_QGTagger_tagged_WPq50 = (vector<int>*)0x15d1c30
 jet_QGTagger_tagged_WPq80 = (vector<int>*)0xee5ed0
 jet_QGTagger_tagged_WPq90 = (vector<int>*)0x1d33150
 jet_QGTagger_truthjet_eta = (vector<float>*)0x1487bc0
 jet_QGTagger_truthjet_nCharged = (vector<int>*)0x14de270
 jet_QGTagger_truthjet_pt = (vector<float>*)0x1d61be0
 jet_bTag        = (vector<int>*)0x1d665d0
 jet_deltaR0.20_matched_truth_particle_barcode = (vector<double>*)0x1d5d4f0
 jet_e           = (vector<double>*)0x15ec4b0
 jet_eta         = (vector<double>*)0x15b76a0
 jet_isSig       = (vector<int>*)0x15b3fa0
 jet_passOR      = (vector<int>*)0x15bcf50
 jet_phi         = (vector<double>*)0x1d6d470
 jet_pt          = (vector<double>*)0x1c15b90
 lumiBlock       = 47
 mcChannelNumber = 504549
 mcEventWeight   = 5.29637e-05
 pass_HLT_ht1000_L1J100 = 1
 pass_HLT_ht700_L1J75 = 1
 pileupReweightHash = 0
 pileupWeight    = 0
 runNumber       = 310000
 truth_QuarkFromGluino_ParentBarcode = (vector<int>*)0x1c21260
 truth_QuarkFromGluino_barcode = (vector<int>*)0x1be1ce0
 truth_QuarkFromGluino_charge = (vector<double>*)0x1dc5920
 truth_QuarkFromGluino_e = (vector<double>*)0xb0ca40
truth_QuarkFromGluino_eta = (vector<double>*)0x1c1af50
 truth_QuarkFromGluino_pdgID = (vector<int>*)0x1d92d50
 truth_QuarkFromGluino_phi = (vector<double>*)0x1be64c0
 truth_QuarkFromGluino_pt = (vector<double>*)0x15ccae0
 truth_jet_e     = (vector<double>*)0xee6af0
 truth_jet_eta   = (vector<double>*)0x137f000
 truth_jet_phi   = (vector<double>*)0x1d2bfe0
 truth_jet_pt    = (vector<double>*)0x1c24d30
 truth_parent__charge = (vector<double>*)0xb11f90
 truth_parent_barcode = (vector<int>*)0x1563250
 truth_parent_e  = (vector<double>*)0x1d5e4e0
 truth_parent_eta = (vector<double>*)0x1d64de0
 truth_parent_m  = (vector<double>*)0x1c20bc0
 truth_parent_pdgId = (vector<int>*)0x1c1fbe0
 truth_parent_phi = (vector<double>*)0x1d7e0d0
 truth_parent_pt = (vector<double>*)0x1d29c20
 normweight      = 0.000267946
```
</details>

In general we can divide the branches into the ones that contain a single value
(e.g. `eventNumber`, `mcEventWeight`, `normweight`,...) and the ones that are
vectors and therefore contain multiple values (e.g. `jet_pt`, `truth_QuarkFromGluino_pt`,
`truth_jet_pt`,...).
The vectorial branches contain quantities related to objects in the event.
For example `jet_pt` contains the transverse momentum of the jets in the event;
the first position in the vector contains the pT of the leading jet, the second
position the pT of the sub=leading jet, and so on.
The variables that start with `jet_` are related to the reco-level jets (R=0.4 PFlow jets),
while we also have information about truth-level quantities:
`truth_jet` are the truth-level jets, `truth_QuarkFromGluino` the quarks which
originate from gluinos and `truth_parent` the particles that are identified as
"interesting" parent particles (in the case of this signal, the gluinos themselves).

## Event weights 
When producing histograms, the minimal set of weights to be considered are the Monte Carlo (MC) weight, and the cross-section weight.

#### Monte Carlo weight

This event weight is related to how the events are generated (specifically, it's related to the sampling of the matrix element function).
To obtain meaningful distributions, you need to weight the events by the MC weight.
Depending on which generator has been used for each sample, it is possible that this weight takes the value of 1 for all the events in the
sample (i.e. the events have been generated un-weighted). In this case, the value stored in the ntuples would be 1, so it is still safe
to use this weight in your code. When this weight is not needed, you will just pick up the default value of 1, which does not
change anything in your distributions. 

In the ROOT files, this weight is stored in the variable `mcEventWeight`.

#### Cross-section weight

This number, which is the same for all events belonging to the same sample, is basically the ratio between the number of simulated MC events and the number of events that we expect to have in a certain amount of collected data, based on the cross section of the specific process.
Unlike the MC weight, if you are looking at events that belong to the same physical process and that have been generated with the same settings, you typically would obtain
distributions with the correct shape also without this weight (since, as mentioned before, it's the same for all the events in the same sample).
But using properly this weight is instead essential to understand **how many events** we expect form a certain process.
Therefore, it is 
a piece of essential information 
also to compare how many events we expect e.g. for different signals, or for a specific signal and a 
background process. 

In the ROOT files, this weight is stored in the variable `normweight`. 
If you use this weight to build your histograms, your histograms will be normalized to `1 pb^{-1}`. 

![#1589F0](https://via.placeholder.com/15/c5f015/000000?text=+)
**Question**: If you want to normalize your histograms to e.g. 139 fb^{-1}, 
by which factor do you need to scale your histograms? 


## Quark/gluon tagging

In signal events, there are many jets: the ones originating from the gluinos decay, but also extra jets from radiation.
We are currently working at integrating into the analysis a so-called “quark-gluon tagger”,
an algorithm developed to try to distinguish between jets originating from a quark and jets originating from a gluon.
This algorithm uses jet substructure variables (even though in this case they are applied to
jets with R=0.4, and not only to large-R jets).
This algorithm will help the analysis in two ways:
* Counting the number of jets tagged as quarks could be a possible extra handle to suppress the multijet background
* If we can identify which jets in the event come from quarks and not from gluons, we have greater chances of reconstructing the signal
events properly (i.e. identify which jets come from which gluino, since those quark jets and not gluon jets).
This way, if a signal exists, we will be able to reconstruct and identify it also in data. 

Some information about quark-gluon tagging:
* [ATLAS 2014 paper](https://arxiv.org/pdf/1405.6583v3.pdf)
* [ATLAS Note](http://cdsweb.cern.ch/record/2263679/files/ATL-PHYS-PUB-2017-009.pdf) using the number of tracks as discriminant

## Variables for Quark/Gluon Tagging 

The tagger used in this study is a boosted decision tree (BDT, for an introduction to what a BDT is
see e.g. [here](https://indico.fnal.gov/event/15356/contributions/31377/attachments/19671/24560/DecisionTrees.pdf)).
It takes as input three jet substructure variables:
* The number of tracks. This is stored into the variable `jet_QGTagger_NTracks`
* The width of the jet. This is stored into the variable `jet_QGTagger_TracksWidth`
* The two-point energy correlation. This is stored into the variable `jet_QGTagger_TracksC1`

The meaning of the variables is discussed in the [reference](https://arxiv.org/pdf/1405.6583v3.pdf)
mentioned above. 

![#1589F0](https://via.placeholder.com/15/c5f015/000000?text=+)
**Question**: after reading the introduction of [ATLAS Note](http://cdsweb.cern.ch/record/2263679/files/ATL-PHYS-PUB-2017-009.pdf)
referenced above, would you be able to explain why the number of tracks provides discrimination between jets originating from
quarks and jets originating from gluons? 

In order to observe differences between the jets originating from quarks and the jets originating from gluons,
we first of all need to be able to plot the two categories separately.
A clear division into two separate samples is of course possible only in the MC simulated events,
where we can access the truth information.
The variable `jet_PartonTruthLabelID` stores the truth category to which the jet belongs.
In particular, the following values are of interest for this study:
* `jet_PartonTruthLabelID < 5`: the jet originates from a light quark
* `jet_PartonTruthLabelID = 21`: the jet originates from a gluon 

## Tasks

#### First task 

Plot the distribution of the number of tracks in jets originating from quarks and in jets originating from gluons,
looking at the jets from the signal with m(gluino) = 1600 GeV.
The plot should: 
* Show two histograms (with different colors) corresponding to the distribution of the number of
tracks for jets in the two categories
* Be normalized to 139 fb^{-1}
* Have a legend
* Have axes names

A skeleton with some instructions that can be helpful to carry out this task 
is available in [shape_comparison/skeleton.py](https://github.com/chiara-rizzi/first-steps-analysis/blob/main/shape_comparison/skeleton.py). 
The example is already running and it produces a plot, but it will need to
be modified in order to complete fully the task (the comments in the
example indicate where these modifications can be added). 

You can run the example with:
```
cd shape_comparison
python skeleton.py
```

You can copy the skeleton into a new file, modify it, and
push it to the same repository. 

![#1589F0](https://via.placeholder.com/15/c5f015/000000?text=+)
**Question**: how does the distribution of the number of tracks compare
for quarks and gluons? Is this expected? 

#### Second task

Following the example of the first task, you should plot also the 
distribution of the jet width and of the two-point energy correlation. 

#### Third task

Reproduce the same plots as above, but requiring that the
jets you select satisfy the definition of signal jets.
This is stored in the variable `jet_isSig`, which takes
the value 1 for signal jets and 0 for jets that fail the
definition of signal jets. The definition of signal jet
requires, on top of the definition of a baseline jet:
* To pass the overlap removal
* To pass the JVT selection
* To have an absolute value of the pseudorapidity < 2.8

In practice, you can do it by modifying the selection string.
E.g. in the case of quark jets, from:
```
'((jet_PartonTruthLabelID<5)*(normweight*mcEventWeight))'
```
to:
```
'(((jet_PartonTruthLabelID<5)*(jet_isSig>0))*(normweight*mcEventWeight))'
```

![#1589F0](https://via.placeholder.com/15/c5f015/000000?text=+)
**Question**: do you see any change in the distributions with respect
using baseline jets?


#### Fourth task

Reproduce the sampel plots as above, for signal jet, but divided into
"pT slices". This means that you will have different groups of plots,
each group selecting jets only in a certain pT range.
This way you are sure that, when looking at each plot, you are comparing
jets with similar energy.

To start, you can use the following binning: 20-40 GeV, 40-60 GeV,
60-100 GeV, 100-150 GeV, 150-200 GeV, 200-300 GeV, 300-500 GeV, >500 GeV.
But please feel free to adapt it if while doing the exercise you realize it
is not appropriate (e.g. you don't have enough statistics in one bin).

This means that, for each pT range you want to consider, you will add to your selection
the selection on the jet pT. E.g. for the first bin:

```
'(((jet_PartonTruthLabelID<5)*(jet_isSig>0)*(jet_pt>=20 && jet_pt<40))*(normweight*mcEventWeight))'
```                                                     
                                                       
Please add also some text on the plot to include which pT range you are considering
(you can use TLatex for this, see e.g. [this tutorial](https://root.cern.ch/doc/master/zdemo_8py_source.html)).

**Suggestion**: you might want to consider adapting your script to handle all of the
pT ranges together in a `for` loop, so that you don't have to manually change
the selection, the text for the plot and the name of the output file every time. 

Note: if you want to remove the title of the histogram and the stat box from your plots, you can
so so with:
```
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptTitle(0)
```



