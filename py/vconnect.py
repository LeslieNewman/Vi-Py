import requests as ur

def getUrlPrefix():
    return('http://YOUR_ADDRESS_GOES_HERE:10010/vision/api')

#--- runvget("Schema+showInheritance")
#---  do your own encoding
def runvget(query):
    url=getUrlPrefix()
    request = url + '?expression=' + query
    response = ur.get(request)
    return(response.text)

#--- runvpost("Schema showInheritance")
#---   returns object that reponds to text or json()
def runvpost(query):
    url=getUrlPrefix()
    if (type(query) is dict):
        exp = query
    else:
        exp = {'expression' : query}
    response = ur.post(url, json=exp)
    return(response)

#--  runvision("Schema showInheritance")
def runvision(query):
    return(runvpost(query).text)

#-- runvisionJSON('JS getArrayFrom: [ Currency masterList ] for: "name"')   
def runvisionJSON(query):
   return(runvpost(query).json())

#--- runapp ("appName", params={})
def runapp (appName, params={} ):
    exp = 'Applay run: "' + appName + '"'
    params['expression'] = exp
    return runvisionJSON(params)
