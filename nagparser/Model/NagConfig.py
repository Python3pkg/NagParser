import os
import types


class NagConfig(object):
    STALE_THRESHOLD = 240
    IGNORE_STALE_DATA = False
    NAGIOS_CMD_FILE = '/var/lib/nagios3/rw/nagios.cmd'
    IMPORTANTSERVICEGROUPS = {}
    basicAPIKEYS = []
    DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
    REQUIRE_HARD_SERVICE_STATUS = False

    def __init__(self, files):
        allfilesexist = True
        for temp in files:
            if not os.path.exists(temp):
                allfilesexist = False

        if allfilesexist:
            self.files = files
            self._set_getpermissionsfunction(basicgetpermissions)
        else:
            raise IOError('File(s) not found')

    def _set_getpermissionsfunction(self, function):
        self.getpermissions = function

    def _get_basicapikeys(self):
        return NagConfig.basicAPIKEYS

    def _set_basicapikeys(self, apikeys):
        if type(apikeys) is not types.ListType:
            apikeys = [apikeys]
        NagConfig.basicAPIKEYS = apikeys

    APIKEYS = property(_get_basicapikeys, _set_basicapikeys)


def basicgetpermissions(apikey):
    '''Basic apikey check function. Can be overridden to provide custody apikey validation functionality.
        Should return a list of permissions or an empty list of no permissions.
        Permissions are currently un-utilized but future versions of the NagCommands() will use them to
        restrict access etc...'''

    if apikey in NagConfig.basicAPIKEYS:
        return ['access granted']
    else:
        return []
