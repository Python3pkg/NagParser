#!/usr/bin/env python

import nagparser

basedir = './nagparser/test/data/'
importantservicegroups = None
files = [basedir + 'test_objects.cache', basedir + 'test_status.dat']
config = {'importantservicegroups': importantservicegroups, 'files': files}
nag = nagparser.parse(config)

json = nag.genoutput('json', prittyprint = False)

print json
print json.keys()
print json['hosts'][1]['attributes']['host_name']
print json['hosts'][1]['services'][1]['attributes']
print json['hosts'][1]['services'][1]['attributes']['plugin_output']
