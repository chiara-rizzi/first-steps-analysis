# First steps in the analysis
Instructions for the first steps needed to produce studies with the ntuples produced with FactoryTools

In this repo you can find 
* Information about the ntuples needed to get started with quark-gluon tagging 
* Description of the basic steps 

## Intruduction about the signal model

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
than that. This is because, in order to be written into this ROOT files, the
events need to pass a first preselection (requiring highly energetic events that
also fire the trigger that we want -- described later).

To open the ROOT files you can do e.g.:
```
root -l GG_rpv_UDS_900.root
```


## Quark/gluon tagging

In signal events, there are many jets: the ones originating from the gluinos decay, but also extra jets from radiation.
We are currently working at integrating into the analysis a so called “quark-gluon tagger”,
an algorithm developed to try to distinguish between jets originating from a quark and jets originating from a gluon.
This algorithm uses jet substructure variables (even though in this case they are applied to
jets with R=0.4, and not only to large-R jets).
This algorithm will help the analysis in two ways:
* Counting the number of jets tagged as quarks could be a possible extra handle to suppress the multijet background
* If we can identify which jets in the event come from quarks and not from gluons, we have greater chances of reconstructing the signal
events properly (i.e. identify which jets come from which gluino, since those quark jets and not gluon jets).
This way, if a signal exists, we will be able to reconstruct and identify it also in data. 

## Variables for Quark/Gluon Tagging 

## Event weights 
When producing histograms, the minimal set of weights to be considered are the Monte Carlo (MC) weight, and the cross-section weight.

#### Monte Carlo weight

This event weight is related to how the events are generated (specifically, it's realted to the sampling of the matrix element function).
To obtain meaningful distributions, you need to weight the events by the MC weight.
Depending on which generator has been used for each sample, it is possible that this weight takes the value of 1 for all the events in the
sample (i.e. the events have been generated un-weighted). In this case, the value stored in the ntuples would be 1, so it is still safe
to use this weight in your code. When this weight is not needed, you will just pick up the default value of 1, which does not
change anything in your distributions. 

#### Cross-section weight

This number, which is the same for all events belonging to the same sample, is basically the ratio between the number of simulated MC events and the number of events that we expect to have in a certain amount of collected data, based on the cross section of the specific process.
Unlike the MC weight, if you are looking at events that belong to the same physical process and that have been generated with the same settings, you typically would obtain
distributions with the correct shape also without this weight (since, as mentioned before, it's the same for all the events in the same sample).
But using properly this weight is instead essential to understand **how many events** we expect form a certain process.

Therefore, it is an essential information also to compare the magniture 
To make a practical example, we can consider the 

## Example code 

## Tasks
Plot the distribution of the number of 
