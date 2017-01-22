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

def get( ID, cursor ) :
  if DEBUG :
    print " >>> running piper_pickledb get "
  return cursor.get( ID )
