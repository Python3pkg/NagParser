from NagBase import NagBase
from NagList import NagList

from nagparser.Services.nicetime import getnicetimefromdatetime


class Host(NagBase):
    '''Host represents a host definition found in status.dat.'''

    def __init__(self, nag):
        super(Host, self).__init__(nag=nag)
        self.host_name = ''

    @property
    def services(self):
        return NagList([x for x in self.nag.services if x.host_name == self.host_name])

    @property
    def name(self):
        return self.host_name

    def laststatuschange(self, returntimesincenow=True):
        lastchange = max(self.services, key=lambda x: x.laststatuschange(returntimesincenow=False)). \
                        laststatuschange(returntimesincenow=False)

        if returntimesincenow:
            return getnicetimefromdatetime(lastchange)
        else:
            return lastchange
