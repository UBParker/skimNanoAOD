# skimNanoAOD
For skimming nanoAOD with semi-leptonic TT selections (input to W-tag scalefactor fitters)

## installation instructions
Setup CMSSW and get nanoAOD packages
```
cmsrel CMSSW_9_4_1
cd CMSSW_9_4_1/src
cmsenv
git cms-merge-topic cms-nanoAOD:master
git checkout -b nanoAOD cms-nanoAOD/master
git clone https://github.com/cms-nanoAOD/nanoAOD-tools.git PhysicsTools/NanoAODTools
scram build
```

