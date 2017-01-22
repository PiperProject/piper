#!/usr/bin/env python

import os, sys
from pymongo import *

def get( ID, cursor ) :
  return cursor.find_one( { "_id" : ID } )
