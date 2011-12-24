#!/usr/bin/env python

import nagparser

basedir = './nagparser/test/'
importantservicegroups = None
files = [basedir + 'test_objects.cache', basedir + 'test_status.dat']
config = {'importantservicegroups': importantservicegroups, 'files': files}
nag = nagparser.parse(config)

print nag.lastupdated

