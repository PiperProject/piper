#!/usr/bin/env python

# -------------------------------------- #

import os, sys

# -------------------------------------- #



###################
#  CHECK PY DEPS  #
###################
# check python package dependencies
def checkPyDeps() :

  print "*******************************"
  print "  CHECKING PYTHON DEPENDECIES  "
  print "*******************************"

  # pymongo
  import pymongo
  if pymongo.__name__ :
    print "pymongo...verified"

  # pickledb
  import pickledb
  if pickledb.__name__ :
    print "pickledb...verified"

  print "All python dependencies installed! Yay! =D"
  print "*******************************"
  print "*******************************"

  return None


##############################
#  UPDATE EXISTING PACKAGES  #
##############################
def updateExistingPackages() :

  print "*******************************"
  print "  UPDATING EXISTING PACKAGES"
  print "*******************************"

  # keep all submodules up-to-date
  os.system( "git pull --recurse-submodules" )
  os.system( "git submodule update --remote --recursive" )


##############################
#  MAIN THREAD OF EXECUTION  #
##############################
checkPyDeps()
updateExistingPackages()


#########
#  EOF  #
#########
