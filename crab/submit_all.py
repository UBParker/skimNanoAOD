#!/usr/bin/env python
"""
This is a small script that submits a config over many datasets
"""
import os
from optparse import OptionParser

def make_list(option, opt, value, parser):
    setattr(parser.values, option.dest, value.split(','))

def getOptions() :
    """
    Parse and return the arguments provided by the user.
    """
    usage = ('usage: python submit_all.py -c CONFIG -d DIR -f DATASETS_FILE')

    parser = OptionParser(usage=usage)    
    parser.add_option("-c", "--config", dest="cfg", default="crab_script.py",
        help=("The crab script you want to submit "),
        metavar="CONFIG")
    parser.add_option("-d", "--dir", dest="dir", default="NANO",
        help=("The crab directory you want to use "),
        metavar="DIR")
    parser.add_option("-f", "--datasets", dest="datasets",
        help=("File listing datasets to run over"),
        metavar="FILE")
    parser.add_option("-s", "--storageSite", dest="storageSite", default="T3_CH_PSI",
        help=("Site"),
        metavar="SITE")
    parser.add_option("-l", "--lumiMask", dest="lumiMask",
        help=("Lumi Mask JSON file"),
        metavar="LUMIMASK")

    (options, args) = parser.parse_args()

    if options.cfg == None or options.dir == None or options.datasets == None or options.storageSite == None:
        parser.error(usage)
    
    return options
    

def main():

    options = getOptions()

    from WMCore.Configuration import Configuration
    config = Configuration()

    from CRABAPI.RawCommand import crabCommand
    from httplib import HTTPException

        
    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
    config.section_("General")
    config.General.workArea = options.dir 
    config.General.transferLogs = True

    config.section_("JobType")
    config.JobType.pluginName = 'Analysis'
    #config.JobType.psetName = options.cfg
    
    config.section_("Data")
    config.Data.inputDataset = None
    config.Data.splitting = ''
    #config.Data.unitsPerJob = 1
    config.Data.ignoreLocality = False
    #config.Data.publication = True
        
    #config.Data.publishDBS = 'phys03'
   
    config.section_("Site")
    config.Site.storageSite = options.storageSite

    print 'Using config ' + options.cfg
    print 'Writing to directory ' + options.dir
    
    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException, hte:
            print 'Cannot execute command'
            print hte.headers

    #############################################################################################
    ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
    #############################################################################################


    #Taken from example here                                                       
    #https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#crab_submit_fails_with_Block_con                                                                    

    # this will use CRAB client API                                                
    from CRABAPI.RawCommand import crabCommand

    # talk to DBS to get list of files in this dataset                             
    from dbs.apis.dbsClient import DbsApi
    dbs = DbsApi('https://cmsweb.cern.ch/dbs/prod/phys03/DBSReader')

    datasetsFile = open( options.datasets )
    jobsLines = datasetsFile.readlines()
    jobs = []
    for ijob in jobsLines :
        s = ijob.rstrip()
        if (len(s)==0 or s[0][0]=='#'): continue
        s = ijob.rstrip()
        jobs.append( s )
        print '  --> added ' + s
        
    for ijob, job in enumerate(jobs) :

        ptbin = job.split('/')[1]
        cond = job.split('/')[2]
        datatier = job.split('/')[3]
        requestname = ptbin + '_' + cond
        if len(requestname) > 100: requestname = ''.join((requestname[:100-len(requestname)]).split('_')[:-1])
        print 'requestname = ', requestname
        config.General.requestName = requestname
        config.Data.outputDatasetTag = requestname
        if datatier == 'USER':

          config.JobType.psetName = 'PSet.py'
          print options.cfg[0:-2]+'sh'
          config.JobType.scriptExe = options.cfg[0:-2]+'sh'
          config.JobType.inputFiles = [options.cfg ,'haddnano.py'] #hadd nano will not be needed once nano tools are in cmssw                                                                                                                    
          config.JobType.sendPythonFolder  = True
          fileDictList = dbs.listFiles(dataset=job) 
          print ("dataset %s has %d files" % (job, len(fileDictList)))
          # DBS client returns a list of dictionaries, but we want a list of Logical File Names                   
          lfnList = [ dic['logical_file_name'] for dic in fileDictList ]
          # following 3 lines are the trick to skip DBS data lookup in CRAB Server                                               
          config.Data.userInputFiles = lfnList
          config.Data.splitting = 'FileBased'
          config.Data.unitsPerJob = 1          
          config.Data.publication =  False
          config.Site.whitelist = [options.storageSite]          
        if 'MINIAOD' in datatier :
          onfig.JobType.psetName = options.cfg
          config.Data.inputDataset = job
          config.Data.publication = True                                                                          
          config.Data.publishDBS = 'phys03'  
        if datatier == 'MINIAODSIM': 
          config.Data.splitting = 'FileBased'
          config.Data.unitsPerJob = 1
        elif datatier == 'MINIAOD': 
          config.Data.splitting = 'LumiBased'
          config.Data.lumiMask = options.lumiMask
          config.Data.unitsPerJob = 200
        print 'Submitting ' + config.General.requestName + ', dataset = ' + job
        print 'Configuration :'
        print config
        try :
            from multiprocessing import Process
            
            p = Process(target=submit, args=(config,))
            p.start()
            p.join()
            #submit(config)
        except :
            print 'Not submitted.'



if __name__ == '__main__':
    main()            
