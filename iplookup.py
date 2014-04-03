#!/usr/bin/env python2

# Imports
from iplookup.ip_lookup import IP_Lookup
import sys


# Author and licensing
__Author__      =       "b-mcg"
__Email__       =       "bmcg0890@gmail.com"
__License__     =       """
Copyright (C) 2014-2016  b-mcg   <bmcg0890@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

# Version number
VERSION         =       'v0.0.1'




def main():
    """
    main()

    """
    usage       =       '\nUsage: ip_lookup.py [IP_Address] [--help]\nip_lookup.py: Error: too few arguments\n'

    try:

        if sys.argv[1] == '--help':
            print usage[:43]

        else:
            IP_Lookup(sys.argv[1]).display_info()

    except IndexError:
        print usage
        sys.exit(2)



if __name__ ==  '__main__':
    main()
