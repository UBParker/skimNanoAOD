
def getXsec(sample):
  if sample.find( "WJetsToQQ_HT"                           ) !=-1 : return 95.14;
  elif sample.find( "ZJetsToQQ_HT600toInf"                 ) !=-1 : return 41.34;
  elif sample.find( "QCD_Pt_170to300_"                     ) !=-1 : return 117276.;
  elif sample.find( "QCD_Pt_300to470_"                     ) !=-1 : return 7823.;                   
  elif sample.find( "QCD_Pt_470to600_"                     ) !=-1 : return 648.2;                  
  elif sample.find( "QCD_Pt_600to800_"                     ) !=-1 : return 186.9;                 
  elif sample.find( "QCD_Pt_800to1000_"                    ) !=-1 : return 32.293;               
  elif sample.find( "QCD_Pt_1000to1400_"                   ) !=-1 : return 9.4183; 
  elif sample.find( "QCD_Pt_1400to1800_"                   ) !=-1 : return 0.84265; 
  elif sample.find( "QCD_Pt_1800to2400_"                   ) !=-1 : return 0.114943; 
  elif sample.find( "QCD_Pt_2400to3200_"                   ) !=-1 : return 0.006830; 
  elif sample.find( "QCD_Pt_3200toInf_"                    ) !=-1 : return 0.000165445; 
  elif sample.find( "QCD_HT100to200"                       ) !=-1 : return 27990000;
  elif sample.find( "QCD_HT200to300"                       ) !=-1 : return 1712000.;
  elif sample.find( "QCD_HT300to500"                       ) !=-1 : return 347700.;
  elif sample.find( "QCD_HT500to700"                       ) !=-1 : return 32100.;
  elif sample.find( "QCD_HT700to1000"                      ) !=-1 : return 6831.;
  elif sample.find( "QCD_HT1000to1500"                     ) !=-1 : return 1207.;
  elif sample.find( "QCD_HT1500to2000"                     ) !=-1 : return 119.9;
  elif sample.find( "QCD_HT2000toInf"                      ) !=-1 : return 25.24;
  elif sample.find( "QCD_Pt-15to7000" ) !=-1 or sample.find( "QCD_Pt_15to7000" ) !=-1: return  2.022100000e+09*60.5387252324;
  elif sample.find( "TT_TuneCUETP8M2T4"                    ) !=-1 : return  831.76      ;
  elif sample.find( "TT_TuneEE5C_13TeV-powheg-herwigpp"    ) !=-1 : return  831.76      ;
  elif sample.find( "TT_"    							   ) !=-1 : return  831.76      ; #for testing
  elif sample.find( "TTJets_"                              ) !=-1 : return  831.76      ;
  elif sample.find("WJetsToLNu_HT-100To200"                ) !=-1 : return 1347*1.21    ;
  elif sample.find("WJetsToLNu_HT-200To400"                ) !=-1 : return 360*1.21     ;
  elif sample.find("WJetsToLNu_HT-400To600"                ) !=-1 : return 48.9*1.21    ;
  elif sample.find("WJetsToLNu_HT-600To800"                ) !=-1 : return 12.08*1.21   ;
  elif sample.find("WJetsToLNu_HT-800To1200"               ) !=-1 : return 5.26*1.21    ;
  elif sample.find("WJetsToLNu_HT-1200To2500"              ) !=-1 : return 1.33*1.21    ;
  elif sample.find("WJetsToLNu_HT-2500ToInf"               ) !=-1 : return 0.03089*1.21 ;
  elif sample.find( "WJetsToLNu_TuneCUETP8M1"              ) !=-1 : return 50380.0*1.22 ;
  elif sample.find( "W1JetsToLNu_TuneCUETP8M1"             ) !=-1 : return 9644.5*1.22 ;
  elif sample.find( "W2JetsToLNu_TuneCUETP8M1"             ) !=-1 : return 3144.5*1.22 ;
  elif sample.find( "W3JetsToLNu_TuneCUETP8M1"             ) !=-1 : return  954.8*1.22 ;
  elif sample.find( "W4JetsToLNu_TuneCUETP8M1"             ) !=-1 : return  485.6*1.22 ;
  elif sample.find("WW_TuneCUETP8M1"                       ) !=-1 : return 118.7        ;
  elif sample.find("WZ_TuneCUETP8M1"                       ) !=-1 : return 47.13        ;
  elif sample.find("ZZ_TuneCUETP8M1"                       ) !=-1 : return 16.5         ;
  elif sample.find("ST_s-channel_4f_leptonDecays"          ) !=-1 : return 11.36*0.3272 ;
  elif sample.find("ST_t-channel_top_4f_leptonDecays"      ) !=-1 : return 136.02*0.322 ;
  elif sample.find("ST_t-channel_antitop_4f_leptonDecays"  ) !=-1 : return 80.95*0.322  ;
  elif sample.find("ST_t-channel_antitop_4f_inclusiveDecays") !=-1 : return 136.02      ;
  elif sample.find("ST_t-channel_top_4f_inclusiveDecays"   ) !=-1 : return 80.95        ;
  elif sample.find("ST_tW_antitop_5f_inclusiveDecays"      ) !=-1 : return 35.6         ;
  elif sample.find("ST_tW_top_5f_inclusiveDecays_"         ) !=-1 : return 35.6         ;
  elif sample.find("SingleMuon")!=-1  or sample.find("SingleElectron") !=-1 or sample.find("JetHT") !=-1 : return 1.
  else:
	  print "Cross section not defined for this sample!!"
	  return 0

















