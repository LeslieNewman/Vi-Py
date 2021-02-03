import requests as ur

class VCconnection(object):
    """The VCconnection object contains the information needed to connect."""
    # Class Variables
    defaultUrl = 'http://visdevdb01.cts.fast-clientenv-aws.dev.us-east-1.aws.fdscloud.io:10010/vision/api'

    def __init__(self, url=defaultUrl):
        self.urlPrefix = url
    def __str__(self):
        return '{} for {} at 0x{:08x}'.format(self.__class__.__name__, self.urlPrefix, id(self))
    def setUrl(self, url):
        """The method sets the URL for the VCconnection."""
        self.urlPrefix = url
    def resetUrl(self):
        """The method resets the URL for the VCconnection."""
        self.url = defaultUrl

    #--- runvget("Schema+showInheritance")
    #---  do your own encoding
    def runvget(self, query):
        request = self.urlPrefix + '?expression=' + query
        response = ur.get(request)
        return(response.text)

    #--- runvpost("Schema showInheritance")
    def runvpost(self, query):
        """ Returns object that reponds to text or json()"""
        if (type(query) is dict):
            exp = query
        else:
            exp = {'expression' : query}
        response = ur.post(self.urlPrefix, json=exp)
        return(response)

    #--  runvision("Schema showInheritance")
    def runvision(self, query):
        return(self.runvpost(query).text)

    #-- runvisionJSON('JS getArrayFrom: [ Currency masterList ] for: "name"')   
    def runvisionJSON(self, query):
       return(self.runvpost(query).json())

    #--- runapp ("appName", params={})
    def runapp (self, appName, params={} ):
        exp = 'Applay run: "' + appName + '"'
        params['expression'] = exp
        return self.runvisionJSON(params)
