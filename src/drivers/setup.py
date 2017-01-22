#!/usr/bin/env python

# -------------------------------------- #

import os, sys

# -------------------------------------- #

# keep all submodules up-to-date
os.system( "git pull --recurse-submodules" )
os.system( "git submodule update --remote --recursive" )

