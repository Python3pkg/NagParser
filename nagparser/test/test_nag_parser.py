# Some basic Nose tests....
from nose.tools import *
import nagparser



class test_nagparser():
    def setup(self):
        basedir = './'
        importantservicegroups = None
        files = [basedir + 'test_objects.cache', basedir + 'test_status.dat']
        self.config = {'importantservicegroups': importantservicegroups, 'files': files}    
        self.lastupdated = '2011-10-31 12:08:22'
        
    def test_nag_objcreation(self):
        '''Just create the nag object, fail on any exception'''
        nag = nagparser.parse(self.config)
        
    
    def test_lastupdated_matches_testdata(self):
        '''Test to ensure the timestamp matches expected given test data'''
        nag = nagparser.parse(self.config)
        asert (nag.lastupdated == self.lastupdated)