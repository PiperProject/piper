#!/usr/bin/env python


# -------------------------------------- #

import os, sys
from pymongo import *

# settings dir
settingsPath  = os.path.abspath( __file__ + "/../../core" )
sys.path.append( settingsPath )
import settings

# -------------------------------------- #

DEBUG = settings.DEBUG


#########
#  GET  #
#########
# get data on id
def get( ID, cursor ) :
  if DEBUG :
    print " >>> running piper_mongodb get "
  return cursor.find_one( { "_id" : ID } )


#########
#  EOF  #
#########
