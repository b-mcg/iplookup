#!/usr/bin/env python2

# Imports
from contextlib import closing
import sys

try:
    from bs4 import BeautifulSoup
    import requests

except ImportError:
    print '\n\nError: Requires: bs4(BeautifulSoup), requests\n\n'
    sys.exit(1)


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



class IP_Lookup(object):
    """
    Parses http://www.db-ip.com/
    for IP address information
    and prints it to screen.

    """

    def __init__(self, ip):
        """
        Create attribute with
        URL including the IP address
        to look up.

        ip  :   IP address to lookup

        """
        self.url   =       'http://www.db-ip.com/{0}'.format(ip)

    def find_ip_info(self):
        """
        Parse html returned from
        request and build list
        of IP address information.

        """
        print '\n\niplookup {0} by: {1} running...\n\n'.format(VERSION, __Author__)

        # Create header dictionary to make the request look like it's from a web browser just incase there's query limiting
        headers     =       {
                            'Host'              :   'db-ip.com',
                            'User-Agent'        :   'Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101 Firefox/28.0',
                            'Accept'            :   'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                            'Accept-Language'   :   'en-US,en;q=0.5',
                            'Accept-Encoding'   :   'gzip, deflate',
                            'DNT'               :   1,
                            'Connection'        :   'keep-alive',
                            'Cache-Control'     :   'max-age=0'
                            }

        # Check for possible errors and parse html returned from get request if no errors are found
        with closing(requests.get(self.url, headers=headers)) as res:

            if res.status_code == 404:
                print 'Error: 404 returned: Check IP address given\n\n'
                sys.exit(2)

            soup            =       BeautifulSoup(res.content)

        # Grab relevant html tags using new line as a separator
            self.ip_info    =       [tag.get_text(separator='\n') for tag in soup.findChildren('tr')] 

            if len(self.ip_info) is 0:
                print 'Error: Nothing returned from get request: Check IP address given\n\n'
                sys.exit(2)
                
        # Reiterate through list of html data, creating new list of key/value tuple pairs and convert to dictionary
            self.ip_info    =       dict([(temp.split('\n')[0], temp.split('\n')[1]) if len(temp.split('\n')) > 1 \
                                            else (temp.split('\n')[0], None) for temp in self.ip_info])

    def display_info(self):
        """
        Iterate IP address info list
        and print to screen.

        """
        self.find_ip_info()

        for k, v in self.ip_info.iteritems():

            try:
                print '{0:>30}: {1:<30}'.format(k.encode('utf-8', 'ignore'), v.encode('utf8', 'ignore'))

            except AttributeError:
                print '{0:>30}: {1:<30}'.format(k.encode('utf-8', 'ignore'), v)

        print '\n'

