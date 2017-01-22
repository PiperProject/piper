#!/usr/bin/env python

# -------------------------------------- #
import os, pprint, sys, time
from pymongo import MongoClient

AGGSPACK_PATH = os.path.abspath( __file__ + "/../../../../src/packages/aggsPack/packages" )
sys.path.append( AGGSPACK_PATH )
import count, sum_agg, average, min_agg, max_agg

SIMPLEJOIN_PATH = os.path.abspath( __file__ + "/../../../../src/packages/simpleJoin/src" )
sys.path.append( SIMPLEJOIN_PATH )
import simpleJoin

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

  book1 = { "author" : "Katy Dee", "title" : "A History of Elsanna", "pubYear" : 2018, "numCopies" : 0, "categories" : ["fantasy"], "cost(Dollars)" : 10 }
  book2 = { "author" : "Katy Dee", "title" : "The LMR Guide to Frozen Fanfiction", "pubYear" : 2017, "numCopies" : 0, "categories" : ["fantasy"], "cost(Dollars)" : 9.99 }
  book3 = { "author" : "Kat Green", "title" : "The LMR Guide to Frozen Fanfiction", "pubYear" : 2017, "numCopies" : 0, "categories" : ["fantasy", "scifi"], "cost(Dollars)" : 0 }

  # insert data
  b    = db.bookdb
  bid1 = b.insert_one( book1 ).inserted_id
  bid2 = b.insert_one( book2 ).inserted_id
  bid3 = b.insert_one( book3 ).inserted_id

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
  print count.count( [ bid1, bid2 ], b, "pubYear,>,2000" )
  print sum_agg.sum_agg( [ bid1, bid2 ], b, "pubYear,>,2000" )
  print average.average( [ bid1, bid2 ], b, "pubYear,>,2000" )
  print min_agg.min_agg( [ bid1, bid2 ], b, "pubYear,>,2000" )
  print max_agg.max_agg( [ bid1, bid2 ], b, "pubYear,>,2000" )

  # join
  res = simpleJoin.simpleJoin( b, [[bid1, bid2, bid3]], "pubYear", None )
  for i in res :
    print i

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
