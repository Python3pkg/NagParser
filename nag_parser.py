#!/usr/bin/env python

import nagparser

basedir = './'
importantservicegroups = None
files = [basedir + 'objects.cache', basedir + 'status.dat']
config = {'importantservicegroups': importantservicegroups, 'files': files}
nag = nagparser.parse(config)

