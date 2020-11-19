# Analyzer-LHE
LHE Analyzer Padova

# Two steps
## Step1 making ntuple from LHE txt into root
```
export DIR=$PWD
cd ntupler
./makeTree.sh
```
## Step2 plot
```
cd $DIR
cd plotter
python run.py
```
