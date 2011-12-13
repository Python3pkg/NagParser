==============================
PLEASE READ THIS BEFORE USING
==============================

*This code is very raw, it has just been ripped out of a Operations Dashboard for which it was written, we need to do quite a bit of cleanup and refactoring on it to make it a standalone program. Though, the code is pretty stable and in our environment is run a few hundred thousand times a week on a fairly large nagios data set. But again this is a small part of that larger project and until have some time to refine this for general use, expect to find issues. It's here now just as a proof of concept only.  *


This project is a subset of scripts that were written to parse Nagios status data and integrate it into a real time 
Operations Dashboard. While most of the dashboard is proprietary we've decided to rip out this parser and offer it to
the Nagios community for use in your own projects.  This code is provided under GPLv3 (see LICENSE.txt). 

If you do make improvements, please contribute back to this project by submitting a pull request. Feel free to contact us if you have any questions, see AUTHORS.txt for contact info.



----------------------------

SAMPLE DATA: 
    We have not yet created a sample file for objects.cache or status.dat as these often have proprietary data in 
    them, but we plan to create a sanitized sample dataset soon. We also expect anyone downloading and trying 
    this probably has a nagios install the can grab the files from, why else would you want this? 

USAGE: 
    This parser can be used for a number of tasks, including building custom interfaces or integrating it into an existing internal website (i.e. operations dashboard). We have built xml and json export but have not yet committed those here.... soon. 

SETUP:
    The only 'setup' needed at this point is to edit the file paths to your nagios status.dat and objects.cache files at the top of parser.py. (this and other settings will be moved to a settings file soon
