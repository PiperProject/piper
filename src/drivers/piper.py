#!/usr/bin/env python

import os, sys

PACKAGE_PATH   = os.path.abspath( __file__ + "/../../packages" )
CURR_PATH      = os.path.abspath( __file__ + "/.." )

# ------------------------------------------------------------------- #
#                      SUPPORTED PACKAGES                             #

URL_AGGSPACK   = "https://github.com/PiperProject/aggsPack.git"
URL_SIMPLEJOIN = "https://github.com/PiperProject/simpleJoin.git"

# ------------------------------------------------------------------- #

##########
#  MAIN  #
##########
def main() :
  packageList = sys.argv[2:]

  os.system( "python " + CURR_PATH + "/setup.py" )

  if sys.argv[1] == "install" :

    for p in packageList :
      if p == "aggsPack" :
        URL = URL_AGGSPACK
        os.system( "cd " + PACKAGE_PATH + "; git submodule add -f " + URL + ";" )
        os.system( "python " + CURR_PATH + "/setup.py" )
      elif p == "simpleJoin" :
        URL = URL_SIMPLEJOIN
        os.system( "cd " + PACKAGE_PATH + "; git submodule add -f " + URL + ";" )
        os.system( "python " + CURR_PATH + "/setup.py" )
      else :
        print "Package not recognized : " + p

  elif sys.argv[1] == "uninstall" :
    for p in packageList :
      if p == "aggsPack" :
        os.system( "cd " + PACKAGE_PATH + "; git rm --cached -f ./" + p + " ; rm -rf " + p + ";" )
      elif p == "simpleJoin" :
        os.system( "cd " + PACKAGE_PATH + "; git rm --cached -f ./" + p + " ; rm -rf " + p + ";" )
      else :
        print "Package not recognized : " + p

  elif sys.argv[1] == "update" :
    os.system( "python " + CURR_PATH + "/setup.py" )


##############################
#  MAIN THREAD OF EXECUTION  #
##############################
main()
