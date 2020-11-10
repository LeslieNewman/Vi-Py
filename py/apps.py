app = {'expression' : open('apps.vis','r').read()}
runvision ( app )
print json.dumps (runapp("ShowStations", {"line" : 7}), indent=1)
