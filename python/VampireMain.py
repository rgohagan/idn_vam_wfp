#!/usr/bin/env python
"""
SYNOPSIS

    VampireMain [-h,--help] [-v,--verbose] [--version]

DESCRIPTION

    This script runs the VAMPIRE system. It takes a script file
    containing instructions.

EXAMPLES

    TODO: Show some examples of how to use this script.

EXIT STATUS

    TODO: List exit codes

AUTHOR

    Rochelle O'Hagan <spatialexplore@gmail.com>

LICENSE

    This script is in the public domain, free from copyrights or restrictions.

VERSION

    $Id$
"""

import time
import optparse
import sys, os, traceback
import configProcessor

if __name__ == '__main__':
    try:
        start_time = time.time()
        parser = optparse.OptionParser(formatter=optparse.TitledHelpFormatter(), usage=globals()['__doc__'], version='$Id$')
        parser.add_option ('-v', '--verbose', action='store_true', default=False, help='verbose output')
        parser.add_option ('-c', '--config', dest='config_file', action='store', help='config filename')
        (options, args) = parser.parse_args()
        if options.verbose: print time.asctime()
        config_f = ""
        if options.config_file:
            config_f = options.config_file
            print 'config file=', config_f
        configProcessor(config_f)
        if options.verbose: print time.asctime()
        if options.verbose: print 'TOTAL TIME IN MINUTES:',
        if options.verbose: print (time.time() - start_time) / 60.0
        sys.exit(0)
    except KeyboardInterrupt, e: # Ctrl-C
        raise e
    except SystemExit, e: # sys.exit()
        raise e
    except Exception, e:
        print 'ERROR, UNEXPECTED EXCEPTION'
        print str(e)
        traceback.print_exc()
        os._exit(1)
