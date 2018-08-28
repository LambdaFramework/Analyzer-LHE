import config
from plotCore import *
from variables import command

#ScanZp("BBbarDM400",50,200)
#ScanZp("BBbarDM",50,200)
#ScanZp("MonojetDM",50,200)
#ScanZp("HadronicDM",50,200)
#ScanZp("BBbarDM400Match1jet",50,200)
#ScanZp("DiJetsDM",50,200)

#samplesConfig=ScanZp("BBbarDM400",50,200)
#run(samplesConfig,command)

#for processes in [ "BBbarDM" , "BBbarDM400" , "MonojetDM" , "HadronicDM" , "BBbarDM400Match1jet" , "DiJetsDM" ]:
#    scanGrid=ScanZp("%s"%processes,50,200) #hs,dm
#    run(scanGrid,command)
#for processes in [ "BBbarDM" , "BBbarDM400" , "MonojetDM" , "HadronicDM" , "BBbarDM400Match1jet" , "DiJetsDM" ]:
#    scanGrid=ScanDM("%s"%processes,50,3000) #hs, zp
#    run(scanGrid,command)
    
for processes in [ "BBbarDM" , "BBbarDM400" , "MonojetDM" , "HadronicDM" , "BBbarDM400Match1jet" , "DiJetsDM" ]:
    scanGrid=Scanhs("%s"%processes,100,3000) #dm,zp
    run(scanGrid,command)
