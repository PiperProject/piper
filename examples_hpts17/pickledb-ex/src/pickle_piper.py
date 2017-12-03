#!/usr/bin/env python

# -------------------------------------- #
import pickledb, os, pprint, sys, time
from pymongo import MongoClient

CURR_PATH = os.path.abspath( __file__ + "/..")

# settings
SETTINGS_PATH = os.path.abspath( __file__ + "/../../../../src/core")
sys.path.append( SETTINGS_PATH )
import settings

# aggsPack
AGGSPACK_PATH = os.path.abspath( __file__ + "/../../../../src/packages/aggspack/src" )
sys.path.append( AGGSPACK_PATH )
import AggsPack

# simpleJoin
SIMPLEJOIN_PATH = os.path.abspath( __file__ + "/../../../../src/packages/simpleJoin/src" )
sys.path.append( SIMPLEJOIN_PATH )
import simpleJoin

# -------------------------------------- #

DEBUG      = settings.DEBUG
OUTPUTS    = settings.OUTPUTS
NOSQL_TYPE = "pickledb"
SAVE_FILE  = CURR_PATH + "/example.db"

###############
#  CLEAN DIR  #
###############
def cleandir() :
  if os.path.exists( SAVE_FILE ) :
    os.system( "rm " + SAVE_FILE  )


#####################
#  PRINT OPENING  #
#####################
def printOpening() :
  print ">>> *************************  <<<"
  print ">>>      PIPER EXAMPLE         <<<"
  print ">>>                            <<<"
  print ">>> STARTING PICKLEDB INSTANCE <<<"
  print ">>> *************************  <<<"
  print
  print


#####################
#  PRINT CLOSING  #
#####################
def printClosing() :
  print ">>> ************************* <<<"
  print ">>>      PIPER EXAMPLE        <<<"
  print ">>>                           <<<"
  print ">>> CLOSING PICKLEDB INSTANCE <<<"
  print ">>> ************************* <<<"
  print
  print


#####################
#  CREATE INSTANCE  #
#####################
def createInstance( filename ) :
  dbInst = pickledb.load( filename, False )
  return dbInst

###################
#  SAVE INSTANCE  #
###################
def saveInstance( dbInst ) :
  dbInst.dump()

###############
#  DELETE DB  #
###############
def deleteDB( dbInst ) :
  dbInst.deldb()

####################
#  CLOSE INSTANCE  #
####################
def closeInstance( dbInst ) :
  dbInst.deldb()

##########
#  MAIN  #
##########
def main() :

  # ---------------------------------------------------- #
  # prelims
  cleandir()
  printOpening()

  # ---------------------------------------------------- #
  # create db
  b = createInstance( SAVE_FILE )

  book1 = { "author" : "Elsa Menzel",  "title" : "A Martial Arts Primer", "pubYear" : 2018, "numCopies" : 0, "categories" : ["fantasy"],          "cost(Dollars)" : 10 }
  book2 = { "author" : "Anna Summers", "title" : "The Rising",            "pubYear" : 2017, "numCopies" : 0, "categories" : ["fantasy"],          "cost(Dollars)" : 9.99 }
  book3 = { "author" : "Kat Green",    "title" : "Frozen Space",          "pubYear" : 2017, "numCopies" : 0, "categories" : ["fantasy", "scifi"], "cost(Dollars)" : 0 }

  bid1 = "bid1"
  bid2 = "bid2"
  bid3 = "bid3"

  # insert data
  b.set( bid1, book1 )
  b.set( bid2, book2 )
  b.set( bid3, book3 )

  # check data
  if OUTPUTS :
    print "********************\nDB CONTENTS:"
    print b.get( bid1 )
    print b.get( bid2 )
    print b.get( bid3 )

  # agg ops
  aggspack_op = AggsPack.AggsPack( NOSQL_TYPE, b )

  if OUTPUTS :
    print "********************\nRunning COUNT : aggspack_op.count(   NOSQL_TYPE, b, [ bid1, bid2 ], 'pubYear,>,2017' )\n" + str(aggspack_op.count( [ bid1, bid2 ], "pubYear,>,2017" )     )
    print "********************\nRunning SUM   : aggspack_op.sum_agg( NOSQL_TYPE, b, [ bid1, bid2 ], 'pubYear,>,2000' )\n" + str(aggspack_op.sum_agg( [ bid1, bid2 ], "pubYear,>,2000" ) )
    print "********************\nRunning AVG   : aggspack_op.average( NOSQL_TYPE, b, [ bid1, bid2 ], 'pubYear,>,2000' )\n" + str(aggspack_op.average( [ bid1, bid2 ], "pubYear,>,2000" ) )
    print "********************\nRunning MIN   : aggspack_op.min_agg( NOSQL_TYPE, b, [ bid1, bid2 ], 'pubYear,>,2000' )\n" + str(aggspack_op.min_agg( [ bid1, bid2 ], "pubYear,>,2000" ) )
    print "********************\nRunning MAX   : aggspack_op.max_agg( NOSQL_TYPE, b, [ bid1, bid2 ], 'pubYear,>,2000' )\n" + str(aggspack_op.max_agg( [ bid1, bid2 ], "pubYear,>,2000" ) )

  # join
  res = simpleJoin.simpleJoin( NOSQL_TYPE, b, [[bid1, bid2, bid3]], "pubYear", None )
  if OUTPUTS :
    print "********************\nRunning SIMPLE JOIN : simpleJoin.simpleJoin( NOSQL_TYPE, b, [[bid1, bid2, bid3]], 'pubYear', None )"
    for i in res :
      print i

  # ---------------------------------------------------- #
  # save db instance
  saveInstance( b )

  # ---------------------------------------------------- #
  # close pickle db instance
  deleteDB( b )
  closeInstance( b )
  printClosing()

##############################
#  MAIN THREAD OF EXECUTION  #
##############################
main()
