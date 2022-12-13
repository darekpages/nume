#!/usr/bin/en python3
#-----------------------------------------------------------
# Script to specify the run or import path
# modules during prototyping in the console or IDLE.
# The script must run in the folder where
# there is another script.
#
a= '16.09.2022 (C) DAREKPAGES'
#-----------------------------------------------------------
import sys

def pathsys():
    platf= sys.platform
    scie= sys.path[0]
    print('\n'+'System:', platf)
    print('Launch path:', scie)

print('\t'+'Defining the script run path'+'\n\t'+
      'Copyright '+a[6:])
pathsys()
