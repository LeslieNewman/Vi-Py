#-----
#  Imports
#-----
import urllib, urllib2, json


#-----
#  getUrlPrefix   - returns the service access path
#  runvx(vision_expression) - pure vision, pass in a vision expression, do your own encoding
#  runvision ( {'expression' : vision_expression} ) - pass in a py dictionary that presents vision expression
#  runvisionJSON ({'expression' : vision_expression} ) - pass in a py dictionary, vision returns json object
#-----

#---  getUrlPrefix
def getUrlPrefix():
   return('http://YOUR_IP_ADDRESS_GOES_HERE:10000/vision/api')

#---  runvx("Schema+showInheritance")
def runvx(query):
   url=getUrlPrefix()
   request = url + '?expression=' + query
   response=urllib2.urlopen(request)
   return response.read().decode('ascii')

#--- runvision( {'expression' : 'Schema showInheritance'} )
#--- runvision ('Schema showInheritance')
def runvision(query):
   url=getUrlPrefix()
   if (type(query) is dict):
       exp = query
   else:
       exp = {'expression' : query}
   request=urllib2.Request(url,urllib.urlencode(exp).encode('ascii'))
   response=urllib2.urlopen(request)
   return response.read().decode('ascii')

#--- runvisionJSON( {'expression' : open('./examples/schema.vis','r').read()} )
#--- runvisionJSON( open('./examples/schema.vis','r').read())
def runvisionJSON(query):
     return json.loads(runvision(query))

#--- runapp ("appName", params={})
def runapp (appName, params={} ) :
   exp = 'Applay run: "' + appName + '"'
   params['expression'] = exp
   return runvisionJSON(params)

