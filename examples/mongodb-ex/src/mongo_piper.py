#!/usr/bin/env python

# -------------------------------------- #
import os, sys
from pymongo import MongoClient
# -------------------------------------- #

DEBUG  = True

##########
#  MAIN  #
##########
def main() :
  client = MongoClient()
  db = client.test
  client.close()

##############################
#  MAIN THREAD OF EXECUTION  #
##############################
main()
