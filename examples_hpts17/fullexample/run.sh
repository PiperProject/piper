#!/usr/bin/env bash

echo "##################################"
echo "      INSTALLING aggsPack..."
python ./../../src/drivers/piper.py install aggsPack
echo "...done."
echo "##################################"

echo "##################################"
echo "      INSTALLING simpleJoin..."
python ./../../src/drivers/piper.py install simpleJoin
echo "##################################"

echo "##################################"
echo "      RUNNING MONGODB EXAMPLE"
python ./../../examples/mongodb-ex/src/mongo_piper.py
echo "##################################"

echo "##################################"
echo "      RUNNING PICKLEDB EXAMPLE"
python ./../../examples/pickledb-ex/src/pickle_piper.py
echo "##################################"
