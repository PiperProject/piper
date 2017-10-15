#!/usr/bin/env python


# -------------------------------------- #

# IMPORTS!!!

# <><><><><><><><> #
#   STD PACKAGES   #
# <><><><><><><><> #
import os, sys
from pymongo import *

# <><><><><><><><> #
#   adapter path   #
# <><><><><><><><> #
adaptersPath  = os.path.abspath( __file__ + "/.." )
sys.path.append( adaptersPath )
#from adapters import piper_mongodb
import piper_mongodb, piper_pickledb

# <><><><><><><><> #
#  settings file   #
# <><><><><><><><> #
settingsPath  = os.path.abspath( __file__ + "/../../core" )
sys.path.append( settingsPath )
import settings

# -------------------------------------- #

DEBUG = settings.DEBUG

class Adapter() :

  # ---------- # 
  # ATTRIBUTES #
  # ---------- # 
  nosql_type = ""

  # ----------- #
  # CONSTRUCTOR #
  # ----------- #
  # instantiate adapter with database type.
  def __init__(self, db_type):
    self.nosql_type = db_type

  # --- #
  # GET #
  # --- #
  # grab a python instance of the database type.
  # i == single identifer
  # c == cursor
  def get( self, i, c ) :

    # MONGODB
    if self.nosql_type == "mongodb" :
      return piper_mongodb.get( i, c )

    # PICKLEDB
    elif self.nosql_type == "pickledb" :
      return piper_pickledb.get( i, c )


#########
#  EOF  #
#########
