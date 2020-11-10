vcode = '''
JS getArrayFrom: [ Station masterList ]
               for: "name,coords"
'''
result =  runvisionJSON(vcode)
print json.dumps(result,indent=1)
