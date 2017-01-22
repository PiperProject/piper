#!/usr/bin/env python


# -------------------------------------- #
import os, sys
from pymongo import *

# adapter path
adaptersPath  = os.path.abspath( __file__ + "/.." )
sys.path.append( adaptersPath )
#from adapters import piper_mongodb
import piper_mongodb, piper_pickledb

# settings dir
settingsPath  = os.path.abspath( __file__ + "/../../core" )
sys.path.append( settingsPath )
import settings

# -------------------------------------- #

DEBUG = settings.DEBUG

class Adapter() :

  # ATTRIBUTES #
  nosql_type = ""

  # CONSTRUCTOR #
  def __init__(self, db_type):
    self.nosql_type = db_type

  # GET #
  # i == single identifer
  # c == cursor
  def get( self, i, c ) :
    if self.nosql_type == "mongodb" :
      return piper_mongodb.get( i, c )
    elif self.nosql_type == "pickledb" :
      return piper_pickledb.get( i, c )
