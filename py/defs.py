#-----
#  Imports
#-----

import urllib.request as ur
import urllib.parse as up
import json


#-----
#  getUrlPrefix   - returns the service access path
#  runvx(vision_expression) - pure vision, pass in a vision expression, do your own encoding
#  runvision ('vision_expreesion') - converts to dictionary that encodes vision expression into {'expression' : encodedExpression}
#  runvisionJSON ('vision_expression') - converts to dictionary that encodes vision expression and returns JSON object
#-----

#---  getUrlPrefix
def getUrlPrefix():
   return('http://YOUR_IP_ADDRESS:10100/vision/api')

#---  runvx("Schema+showInheritance")
def runvx(query):
   url=getUrlPrefix()
   request = url + '?expression=' + query
  # response=urllib2.urlopen(request)
   response=ur.urlopen(request)
   return response.read().decode('ascii')

#--- runvision( {'expression' : 'Schema showInheritance'} )
#--- runvision ('Schema showInheritance')
def runvision(query):
   url=getUrlPrefix()
   if (type(query) is dict):
       exp = query
   else:
       exp = {'expression' : query}
   request=ur.Request(url,up.urlencode(exp).encode('ascii'))
   response=ur.urlopen(request)
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
