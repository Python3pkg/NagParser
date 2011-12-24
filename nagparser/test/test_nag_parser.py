# Some basic Nose tests....

import nagparser

basedir = './'
importantservicegroups = None
files = [basedir + 'test_objects.cache', basedir + 'test_status.dat']
config = {'importantservicegroups': importantservicegroups, 'files': files}



def test_nag_objcreation(config):
    '''Just create the nag object, fail on any exception'''
    nag = nagparser.parse(config)
    
    

def test_lastupdated_matches_testdata(config):
    '''Test to ensure the timestamp matches expected given test data'''
    nag = nagparser.parse(config)
    lastupdated = '2011-10-31 12:08:22'
    asert (nag.lastupdated == lastupdated)