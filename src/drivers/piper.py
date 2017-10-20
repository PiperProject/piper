#!/usr/bin/env python

import os, sys

PACKAGE_PATH   = os.path.abspath( __file__ + "/../../packages" )
SETUP_PATH     = os.path.abspath( __file__ + "/../../.." )

# ------------------------------------------------------------------- #
#                      SUPPORTED PACKAGES                             #

URL_AGGSPACK   = "https://github.com/PiperProject/aggsPack.git"
URL_SIMPLEJOIN = "https://github.com/PiperProject/simpleJoin.git"
URL_YPROV      = "https://github.com/PiperProject/yprov.git"
URL_DUB        = "https://github.com/PiperProject/dub.git"
URL_QUEST      = "https://github.com/PiperProject/quest.git"

# ------------------------------------------------------------------- #

##########
#  MAIN  #
##########
def main() :
  packageList = sys.argv[2:]

  if len( sys.argv ) > 2 :

    # --------------------------------- #
    #    INSTALL PACKAGES FROM INDEX    #
    # --------------------------------- #
    if sys.argv[1] == "install" :

      for p in packageList :

        # AGGSPACK
        if p == "aggsPack" :
          URL = URL_AGGSPACK
          os.system( "cd " + PACKAGE_PATH + "; git submodule add -f " + URL + ";" )
          os.system( "python " + SETUP_PATH + "/setup.py" )

        # SIMPLEJOIN
        elif p == "simpleJoin" :
          URL = URL_SIMPLEJOIN
          os.system( "cd " + PACKAGE_PATH + "; git submodule add -f " + URL + ";" )
          os.system( "python " + SETUP_PATH + "/setup.py" )

        # YPROV
        elif p == "yprov" :
          URL = URL_YPROV
          os.system( "cd " + PACKAGE_PATH + "; git submodule add -f " + URL + ";" )
          os.system( "python " + SETUP_PATH + "/setup.py" )

        # DUB
        elif p == "dub" :
          URL = URL_DUB
          os.system( "cd " + PACKAGE_PATH + "; git submodule add -f " + URL + ";" )
          os.system( "python " + SETUP_PATH + "/setup.py" )

        # QUEST
        elif p == "quest" :
          URL         = URL_QUEST
          QUEST_SETUP = PACKAGE_PATH + "/quest/setup.py"
          os.system( "cd " + PACKAGE_PATH + "; git submodule add -f " + URL + ";" )
          os.system( "python " + QUEST_SETUP )
          os.system( "python " + SETUP_PATH + "/setup.py" )

        # ERROR : UNKNOWN PACKAGE
        else :
          print "Package not recognized : " + p

    # --------------------------------- #
    #   UNINSTALL PACKAGES FROM INDEX   #
    # --------------------------------- #
    elif sys.argv[1] == "uninstall" :
      for p in packageList :

        # AGGSPACK
        if p == "aggsPack" :
          os.system( "cd " + PACKAGE_PATH + "; git rm --cached -f ./" + p + " ; rm -rf " + p + ";" )

        # SIMPLEJOIN
        elif p == "simpleJoin" :
          os.system( "cd " + PACKAGE_PATH + "; git rm --cached -f ./" + p + " ; rm -rf " + p + ";" )

        # YPROV
        elif p == "yprov" :
          os.system( "cd " + PACKAGE_PATH + "; git rm --cached -f ./" + p + " ; rm -rf " + p + ";" )

        # DUB
        elif p == "dub" :
          os.system( "cd " + PACKAGE_PATH + "; git rm --cached -f ./" + p + " ; rm -rf " + p + ";" )

        # QUEST
        elif p == "quest" :
          os.system( "cd " + PACKAGE_PATH + "; git rm --cached -f ./" + p + " ; rm -rf " + p + ";" )

        # ERROR : UNKNOWN PACKAGE
        else :
          print "Package not recognized : " + p

    # --------------------------------- #
    #   ERROR : PACKAGE NOT RECOGNIZED  #
    # --------------------------------- #
    else :
      sys.exit( "ERROR : unrecognized argument '" + sys.argv[1]  + "'. aborting..." )


  # ---------------------------------- #
  #   UPDATE ALL INSTALLED PACKAGES    #
  # ---------------------------------- #
  elif sys.argv[1] == "update" :
    os.system( "python " + SETUP_PATH + "/setup.py" )


  # --------------------------------- #
  #   ERROR : NO ARGUMENTS PROVIDED   #
  # --------------------------------- #
  else :
    sys.exit( "ERROR : must provide at least one of :\n{ 'install', 'uninstall', 'update' },\nwith appropriate corresponding additional arguments when calling the piper package index." )


##############################
#  MAIN THREAD OF EXECUTION  #
##############################
main()


#########
#  EOF  #
#########
