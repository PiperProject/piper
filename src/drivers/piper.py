#!/usr/bin/env python

import os, sys

PACKAGES_PATH  = os.path.abspath( __file__ + "/../../packages" )
URL_AGGSPACK   = "https://github.com/PiperProject/aggsPack.git"
URL_SIMPLEJOIN = ""

##########
#  MAIN  #
##########
def main() :
  packageList = argv[2:]

  if argv[1] == "install" :

    for p in packageList :
      if p == "aggsPack" :
        URL = URL_AGGSPACK
        os.system( "cd " + PACKAGE_PATH + "; git submodule add " + URL + ";" )
      elif p == "simpleJoin" :
        URL = URL_SIMPLEJOIN
        os.system( "cd " + PACKAGE_PATH + "; git submodule add " + URL + ";" )
      else :
        print "Package not recognized : " + p

  elif argv[1] == "uninstall" :
    for p in packageList :
      if p == "aggsPack" :
        os.system( "cd " + PACKAGE_PATH + "; git rm --cached ./" + p + " ; rm -rf " + p + ";" )
      elif p == "simpleJoin" :
        os.system( "cd " + PACKAGE_PATH + "; git rm --cached ./" + p + " ; rm -rf " + p + ";" )
      else :
        print "Package not recognized : " + p


##############################
#  MAIN THREAD OF EXECUTION  #
##############################
main()
