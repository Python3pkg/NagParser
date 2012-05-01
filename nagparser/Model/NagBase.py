from NagCommands import NagCommands
from NagList import NagList

import time
from datetime import datetime

import types


class NagBase(object):
    '''This is the base class that all other 'Nag' objects inherit.  This class defines common functions and should not be directly instantiated. '''
    def getnowtimestamp(self):
        return time.time()

    def __init__(self, nag=None):
        if nag == None:
            self.nag = self
            self._nagcreated = datetime.now()
        else:
            self.nag = nag

    @property
    def commands(self):
        return NagCommands(self)

    @property
    def attributes(self):
        '''Returns a list of tuples with each tuple representing an attribute'''

        output = []
        for attr in self.__dict__:
            attrtype = type(self.__dict__[attr])
            if attrtype is not types.ListType and attrtype is not NagList and not issubclass(attrtype, NagBase):
                t = self.__dict__[attr]
                try:
                    t = int(str(t))
                except ValueError:
                    try:
                        t = float(str(t))
                    except ValueError:
                        pass

                output.append((attr, t))

        return output

    def getbad(self, objtype, items=None):
        if items == None:
            return NagList([x for x in getattr(self, self.classname(objtype) + 's') if int(x.__dict__['current_state']) > 0])
        else:
            return NagList([x for x in items if int(x.__dict__['current_state']) > 0])

    def getbadservices(self):
        return NagList([x for x in self.services if x.status[0] != 'ok'])

    def classname(self, classname=None):
        if classname:
            classbase = classname
        else:
            classbase = self.__class__

        parts = str(classbase).split("'")[1].lower().split('.')
        return parts[len(parts) - 1]

    def genoutput(self, outputformat='json', items=None):
        outputformat = outputformat.lower()

        #Setup
        output = {}
        if outputformat == 'json':
            output['objtype'] = self.classname()
            output['attributes'] = {}
        else:
            return 'Invalid Output'

        #Attributes
        for attr in self.attributes:
            if outputformat == 'json':
                if attr[1] is None:
                    output['attributes'][attr[0]] = 'none'
                else:
                    output['attributes'][attr[0]] = attr[1]

        order = ['host', 'service', 'servicegroup']
        if items is None:
            if order[0] == self.classname():
                items = getattr(self, order[1] + 's')
            else:
                try:
                    items = getattr(self, order[0] + 's')
                except Exception:
                    items = []

        for obj in items:
            temp = obj.genoutput(outputformat=outputformat, finaloutput=False)
            if outputformat == 'json':
                if obj.classname() + 's' not in output.keys():
                    output[obj.classname() + 's'] = []
                output[obj.classname() + 's'].append(temp)

        return output

    def getservice(self, service_description):
        try:
            return getattr(self.services, service_description)
        except AttributeError:
            return None

    def gethost(self, host_name):
        try:
            return getattr(self.hosts, host_name)
        except AttributeError:
            return None

    def getservicegroup(self, servicegroup_name):
        #Note: Using NagList to get the object an attribute is not possible because servicegroups set their name attribute
        # to their alias which is not an identifier of a unique service group (unlike Host and Service which are)
        try:
            return [x for x in self.nag.getservicegroups() if x.__dict__['servicegroup_name'] == servicegroup_name][0]
        except Exception:
            return None
