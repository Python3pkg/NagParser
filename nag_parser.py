#!/usr/bin/env python

def examplegetpermissionssoverridefunction(apikey):
    print("I'm in coolbeans")
    return ['Cool Beans']

import nagparser

#Setup the config options
basedir = './nagparser/test/data/'
files = [basedir + 'test_objects.cache', basedir + 'test_status.dat']

config = nagparser.NagConfig(files = files)

#Extra config options
config.APIKEYS = ['test', 'hi']
config.NAGIOS_CMD_FILE = '/home/ARBFUND/mkennedy/nagios.cmd'

#config.getpermissions = examplegetpermissionssoverridefunction

#get the nag object
nag = nagparser.parse(config)

#Do something interesting

servicegroupstatuses = [x.status for x in nag.getservicegroups(onlyimportant = False)]
for status in list(set(servicegroupstatuses)):
    print(servicegroupstatuses.count(status))


#json = nag.genoutput('json', prittyprint = False)
#
#print nag.servicegroups[1].commands.scheduledowntime('user', 'now', '1h', 'Testing', apikey = 'hi', doappend = True)
#
##print json
#print json.keys()
#print json['hosts'][1]['attributes']['host_name']
#print json['hosts'][1]['services'][1]['attributes']
#print json['hosts'][1]['services'][1]['attributes']['plugin_output']

