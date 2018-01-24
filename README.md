
### installation instructions ###
Setup CMSSW and get nanoAOD packages
```
cmsrel CMSSW_9_4_1
cd CMSSW_9_4_1/src
cmsenv
git cms-merge-topic cms-nanoAOD:master
git checkout -b nanoAOD cms-nanoAOD/master
(Eventually after our additions are merged) 
git clone https://github.com/cms-nanoAOD/nanoAOD-tools.git PhysicsTools/NanoAODTools
(For now)
git clone https://github.com/UBParker/nanoAOD-tools.git PhysicsTools/NanoAODTools
scram build

git clone git@github.com/UBParker/skimNanoAOD.git PhysicsTools/NanoAODTools/skimNanoAOD

cd PhysicsTools/NanoAODTools
(once)
bash standalone/env_standalone.sh  build
(every time)
source standalone/env_standalone.sh


```



### How to skim nanoAOD samples ###
#########################################

The selections are given in selectionModule.py. Additional cuts and input file is defined in process_nanoAOD.py
```
### Producing samples locally
cd skimNanoAOD
python process_nanoAOD.py fileToTest.root DirectorytoStore treeName 
```

```
### Running with CRAB3
### Change input sample and SE in crab_cfg.py. Selections and module in crab_script.py

cd crab/
voms-proxy-init -voms cms --valid 200:00
source /cvmfs/cms.cern.ch/crab3/crab.sh
python submit_all.py -f listOfDatasets.txt
```
