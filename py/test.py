print ("runvx")
print (runvx('Schema+showInheritance'))

print ("runvision")
query1 = {"expression" : "Schema showInheritance"}
response1 = runvision(query1)
print (response1)

print("runvisionJSON - subway")
query2 = {'expression' : open('./subwayJSON.vis','r').read()}
response2 = runvisionJSON(query2)
print("response3 type " , type(response2) )
print json.dumps(response3, indent=1)

result = runapp("ShowStations", {"line" : 7} )
print json.dumps(result, indent=1)
