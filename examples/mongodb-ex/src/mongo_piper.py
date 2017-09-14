#!/usr/bin/env python

# -------------------------------------- #
import os, pprint, sys, time
from pymongo import MongoClient

CURR_PATH = os.path.abspath( __file__ + "/..")

# settings
SETTINGS_PATH = os.path.abspath( __file__ + "/../../../../src/core")
sys.path.append( SETTINGS_PATH )
import settings

AGGSPACK_PATH = os.path.abspath( __file__ + "/../../../../src/packages/aggsPack/packages" )
sys.path.append( AGGSPACK_PATH )
import count, sum_agg, average, min_agg, max_agg

SIMPLEJOIN_PATH = os.path.abspath( __file__ + "/../../../../src/packages/simpleJoin/src" )
sys.path.append( SIMPLEJOIN_PATH )
import simpleJoin

# -------------------------------------- #

DEBUG      = settings.DEBUG
OUTPUTS    = settings.OUTPUTS
NOSQL_TYPE = "mongodb"

DBPATH = os.path.abspath( __file__ + "/../../dbtmp")
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
  print ">>>      PIPER EXAMPLE         <<<"
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
  print ">>>      PIPER EXAMPLE         <<<"
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

  # establsih clean target dir for db
  if not os.path.exists( DBPATH ) :
    os.system( "mkdir " + DBPATH + " ; " )
  else :
    os.system( "rm -rf " + DBPATH + " ; " )
    os.system( "mkdir " + DBPATH + " ; " )

  # build mongodb instance
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
  createInstance()
  time.sleep( 5 )

  # --------------------------------#
  # create db
  client = MongoClient()
  db = client.bookdb

  book1 = { "author" : "Elsa Menzel", "title" : "A Martial Arts Primer", "pubYear" : 2018, "numCopies" : 0, "categories" : ["fantasy"], "cost(Dollars)" : 10 }
  book2 = { "author" : "Anna Summers", "title" : "The Rising", "pubYear" : 2017, "numCopies" : 0, "categories" : ["fantasy"], "cost(Dollars)" : 9.99 }
  book3 = { "author" : "Kat Green", "title" : "Frozen Space", "pubYear" : 2017, "numCopies" : 0, "categories" : ["fantasy", "scifi"], "cost(Dollars)" : 0 }

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
  if OUTPUTS :
    print "********************\nDB CONTENTS:"
    print "bid1 = " + str(bid1)
    pprint.pprint( b.find_one( { "_id": bid1 } ) )
    print
    print "bid2 = " + str(bid2)
    pprint.pprint( b.find_one( { "_id": bid2 } ) )
    print
    print "bid3 = " + str(bid3)
    pprint.pprint( b.find_one( { "_id": bid3 } ) )
    print
    print

  # agg ops
  if OUTPUTS :
    print "********************\nRunning COUNT: count.count( NOSQL_TYPE, b, [ bid1, bid2 ], 'pubYear,>,2000' )\n" + str(count.count( NOSQL_TYPE, b, [ bid1, bid2 ], "pubYear,>,2000" )     )
    print "********************\nRunning SUM  : sum_agg.sum_agg( NOSQL_TYPE, b, [ bid1, bid2 ], 'pubYear,>,2000' )\n" + str(sum_agg.sum_agg( NOSQL_TYPE, b, [ bid1, bid2 ], "pubYear,>,2000" ) )
    print "********************\nRunning AVG  : average.average( NOSQL_TYPE, b, [ bid1, bid2 ], 'pubYear,>,2000' )\n" + str(average.average( NOSQL_TYPE, b, [ bid1, bid2 ], "pubYear,>,2000" ) )
    print "********************\nRunning MIN  : min_agg.min_agg( NOSQL_TYPE, b, [ bid1, bid2 ], 'pubYear,>,2000' )\n" + str(min_agg.min_agg( NOSQL_TYPE, b, [ bid1, bid2 ], "pubYear,>,2000" ) )
    print "********************\nRunning MAX  : max_agg.max_agg( NOSQL_TYPE, b, [ bid1, bid2 ], 'pubYear,>,2000' )\n" + str(max_agg.max_agg( NOSQL_TYPE, b, [ bid1, bid2 ], "pubYear,>,2000" ) )

  # join
  res = simpleJoin.simpleJoin( NOSQL_TYPE, b, [[bid1, bid2, bid3]], "pubYear", None )
  if OUTPUTS :
    print "********************\nRunning SIMPLE JOIN : simpleJoin.simpleJoin( NOSQL_TYPE, b, [[bid1, bid2, bid3]], 'pubYear', None )"
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
  os.system( "rm " + CURR_PATH + "/dbid.txt" )

  if DEBUG :
    print "dbid = " + dbid

  os.system( "kill " + dbid )

##############################
#  MAIN THREAD OF EXECUTION  #
##############################
main()


#########
#  EOF  #
#########
