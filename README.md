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

## Variables for Quark/Gluon Tagging 

## Event weights 
When producing histograms, the minimal set of weights to be considered are:
* The MC weight. This event is related to how the events are generated (specifically, it's realted to the sampling of the matrix element function).
To obtain meaningful distributions, you need to weight the events by the 
* The cross section weight. This number, which is the same for all events belonging to the same sample, is basically the ratio between the number of simulated MC events and the number of events that we expect to have in a certain amount of collected data, based on the cross section of the specific process.
Unlike the MC weight, if you are looking at events that belong to the same physical process and that have been generated with the same settings, you typically would obtain
distributions with the correct shape also without this weight (since, as mentioned before, it's the same for all the events in the same sample).
But using properly this weight is instead essential to understand **how many events** we expect form a certain process.

Therefore, it is an essential information also to compare the magniture 
To make a practical example, we can consider the 

## Example code 

## Tasks
Plot the distribution of the number of 
