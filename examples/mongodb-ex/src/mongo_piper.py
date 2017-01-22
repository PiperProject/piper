#!/usr/bin/env python

# -------------------------------------- #
import os, pprint, sys, time
from pymongo import MongoClient

# import sibling packages HERE!!!
packagePath  = os.path.abspath( __file__ + "/../../../../src" )
sys.path.append( packagePath )

from adapters import piper_mongodb

AGGSPACK_PATH = os.path.abspath( __file__ + "/../../../../src/packages/aggsPack/packages" )
sys.path.append( AGGSPACK_PATH )

import count

# -------------------------------------- #

DBPATH = os.path.abspath( __file__ + "/../../dbtmp")
DEBUG  = True

if DEBUG :
  print "DBPATH = " + DBPATH

###############
#  CLEAN DIR  #
###############
def cleandir() :
  if os.path.exists( "./mongoid.txt" ) :
    os.system( "rm ./mongoid.txt" )

#####################
#  OPENING MESSAGE  #
#####################
def printOpening() :
  print ">>> *************************  <<<"
  print ">>>           PIPER            <<<"
  print ">>>                            <<<"
  print ">>> STARTING MONGO DB INSTANCE <<<"
  print ">>> *************************  <<<"
  print
  print

#####################
#  CLOSING MESSAGE  #
#####################
def printClosing() :
  print ">>> ************************* <<<"
  print ">>>           PIPER           <<<"
  print ">>>                           <<<"
  print ">>> CLOSING MONGO DB INSTANCE <<<"
  print ">>> ************************* <<<"
  print
  print

#####################
#  CREATE INSTANCE  #
#####################
def createInstance() :
  print "Creating mongo db instance at " + DBPATH + "\n\n"
  os.system( "mongod --dbpath " + DBPATH + " &" )

##########
#  MAIN  #
##########
def main() :

  # ---------------------------------------------------- #
  # prelims
  cleandir()
  printOpening()

  # ---------------------------------------------------- #
  # create mongo instance
  #thread.start_new_thread( createInstance, () )
  createInstance()
  time.sleep( 5 )

  # --------------------------------#
  # create db
  client = MongoClient()
  db = client.bookdb

  book1 = { "author" : "Katy Dee", "title" : "A History of Elsanna", "pubYear" : 2017, "numCopies" : 0, "categories" : ["fantasy"], "cost(Dollars)" : 0 }
  book2 = { "author" : "Katy Dee", "title" : "The LMR Guide to Frozen Fanfiction", "pubYear" : 2017, "numCopies" : 0, "categories" : ["fantasy"], "cost(Dollars)" : 0 }

  # insert data
  b    = db.bookdb
  bid1 = b.insert_one( book1 ).inserted_id
  bid2 = b.insert_one( book2 ).inserted_id

  # check mongo collections
  if DEBUG :
    print
    print "CHECKING COLLECTIONS :"
    print db.collection_names(include_system_collections=False)
    print
    print

  # check data
  print "bid1 = " + str(bid1)
  pprint.pprint( b.find_one( { "_id": bid1 } ) )
  print
  print "bid2 = " + str(bid2)
  pprint.pprint( b.find_one( { "_id": bid2 } ) )
  print
  print

  # agg ops
  print count.count( [ bid1, bid2 ], b, None )

  # ---------------------------------------------------- #
  # drop collections
  db.books.drop()
  db.bookdb.drop()

  # check mongo collections
  if DEBUG : 
    print
    print "CHECKING COLLECTIONS :"
    print db.collection_names(include_system_collections=False)
    print
    print

  # ---------------------------------------------------- #
  # close mongo db instance
  printClosing()

  client.close()

  # get instance id
  os.system( "pgrep mongod 2>&1 | tee dbid.txt" )
  fo     = open( "dbid.txt", "r" )
  dbid   = fo.readline()
  fo.close()

  if DEBUG :
    print "dbid = " + dbid

  os.system( "kill " + dbid )

##############################
#  MAIN THREAD OF EXECUTION  #
##############################
main()
