#!/usr/bin/env python

# -------------------------------------- #

import os, sys

# -------------------------------------- #

PACKAGE = "aggsPack"
PACKAGE_PATH = os.path.abspath( __file__ + "/../src/packages" )

if PACKAGE :
  if PACKAGE == "aggsPack" :
    URL = "https://github.com/PiperProject/aggsPack.git"
    os.system( "cd " + PACKAGE_PATH + "; git submodule add " + URL + ";" )

# keep all submodules up-to-date
os.system( "git pull --recurse-submodules" )
os.system( "git submodule update --remote --recursive" )

