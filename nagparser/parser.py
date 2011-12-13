#!/usr/bin/env python

import re
import string
from NagiosObj import Nagios

def NagiosParser(importantservicegroups = None):
    '''Parses the Nagios Status and Object cache files, returns nagios object'''

    #these will move to a config file
    statusfile = './status.dat'
    objectcache = './objects.cache'
    files = [statusfile, objectcache]


    tempobjs = []

    for filename in files:
        tempfile = open(filename)
        content = tempfile.read()
        tempfile.close

        if nagios == None:
            nagios = Nagios()

        sectionsnames = ['hoststatus','servicestatus','programstatus','define servicegroup']
        for section in sectionsnames:
            pat = re.compile(section +' \{([\S\s]*?)\}',re.DOTALL)

            for sectioncontent in pat.findall(content):
                if section == 'hoststatus':
                    temp = Nagios.Host(nagios)
                elif section == 'servicestatus':
                    temp = Nagios.Service(nagios)
                elif section == 'programstatus':
                    temp = nagios
                elif section == 'define servicegroup':
                    temp = Nagios.ServiceGroup(nagios)

                for attr in sectioncontent.splitlines():
                    attr = attr.strip()
                    if len(attr) == 0 or attr.startswith('#'):
                        pass
                    else:
                        if section == 'define servicegroup':
                            delim = '\t'
                        else:
                            delim = '='

                        shortattr = attr.split(delim)[0].lower()
                        value = attr.replace(shortattr+delim, '')
                        temp.__dict__[shortattr] = value
                tempobjs.append(temp)

    hosts = filter(lambda x: isinstance(x, Nagios.Host), tempobjs)
    services = filter(lambda x: isinstance(x, Nagios.Service), tempobjs)
    servicegroups = filter(lambda x: isinstance(x, Nagios.ServiceGroup), tempobjs)

    if importantservicegroups != None:
        servicegroups = filter(lambda x: string.find(str(importantservicegroups), x.servicegroup_name) >= 0, servicegroups)

    if len(hosts):
        nagios.hosts = hosts
    if len(services):
        nagios.services = services
    if len(servicegroups):
        nagios.servicegroups = servicegroups

    return nagios

if __name__ == "__main__":

    nagios = NagiosParser()

    print nagios.lastupdated

