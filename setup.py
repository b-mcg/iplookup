# Imports
from distutils.core import setup
from shutil import copyfile, rmtree
import os
import iplookup



pathname        =       os.getcwd()

copyfile('iplookup.py', 'iplookup/iplookup')

packages        =       ['iplookup']

setup(  name            =       'iplookup',
        version         =       '0.0.1',
        description     =       'IP address information lookup utility.',
        author          =       'b-mcg',
        author_email    =       'bmcg0890@gmail.com',
        url             =       'https://www.github.com/b-mcg/iplookup',
        packages        =       packages,
        package_dir     =       {'iplookup' : os.path.abspath(os.path.join(pathname, 'iplookup/'))},
        scripts         =       ['iplookup/iplookup'], 
        data_files      =       [('share/iplookup', ['README.md', 'LICENSE'])] 
    )



try:

    os.remove(os.path.abspath(os.path.join(pathname, 'iplookup/iplookup')))

except:
    pass


try:

    rmtree(os.path.abspath(os.path.join(pathname, 'build/')))

except:

    pass
