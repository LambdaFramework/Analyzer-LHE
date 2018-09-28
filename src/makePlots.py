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

#Scaning on Zp mass across various process with FIX hs and FIX dm
for processes in [ "BBbarDM" , "BBbarDM400" , "MonojetDM" , "HadronicDM" , "BBbarDM400Match1jet" , "DiJetsDM" ]:
    scanGrid=ScanZp("%s"%processes,90,100) #FIX hs,FIX dm
    run(scanGrid,command)

#Scaning on DM mass across various process with FIX hs and FIX zp
#for processes in [ "BBbarDM" , "BBbarDM400" , "MonojetDM" , "HadronicDM" , "BBbarDM400Match1jet" , "DiJetsDM" ]:
#    scanGrid=ScanDM("%s"%processes,50,3000) #FIX hs, FIX zp
#    run(scanGrid,command)

#Scaning on HS mass across various process with FIX dm and FIX zp
#for processes in [ "BBbarDM" , "BBbarDM400" , "MonojetDM" , "HadronicDM" , "BBbarDM400Match1jet" , "DiJetsDM" ]:
#    scanGrid=Scanhs("%s"%processes,100,3000) #FIX dm,FIX zp
#    run(scanGrid,command)
