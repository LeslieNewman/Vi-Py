import pandas as pd
import os, sys, inspect

sourceDir = os.getenv('FDSBridgeArea') + "/scripts"
sys.path.append(sourceDir)
import vconnect

vc = vconnect.VCconnection()
vc.setUrl('http://visdevdb01.cts.fast-clientenv-aws.dev.us-east-1.aws.fdscloud.io:10010/vision/api')


#-- print (inspect.getsource(vc.runvision))
