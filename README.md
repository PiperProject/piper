# piper
A package index and management system for database management tools organized on Github under the organization of the Piper Project. The base "piper" package encompasses the basic manaagement code necessary for integrating packages from the Piper Project over your underlying NoSQL system. NoSQL databases currently supported by the index include: MongoDB and PickleDB. With piper, users can pull all and only the database management tools from the package index maintained under the Piper Project relevant to their needs.

## Installing piper
Installing the base piper index and management software is as easy as cloning the repository:
```
python setup.py
```

## Installing piper packages
Installing piper does not trigger the installation of any packages from the index. Users pull specific packages from the index explicitly. For example, suppose a user intends to augment the capabilities of an underlying NoSQL system with the basic set of aggregate operations rendered canonical by RDBMSs in the 1990s and early 2000s. The aggsPack package in the index supports all five canonical aggregates (COUNT, SUM, AVERAGE, MIN, MAX). To pull the package, run the following command from the top of the piper/ directory:
```
python ./src/drivers/piper.py install aggsPack
```

piper also supports explicit package updates with the command:
```
python ./src/drivers/piper.py update
```

Finally, piper supports the easy deinstallation of packages loaded from the index:
```
python ./src/drivers/piper.py uninstall aggsPack
```

## Examples
The current prototype ships with two examples illustrating the use of piper within the contexts of two different classes of NoSQL database systems. One example illustrates the use of piper to augment a MongoDB document store with both the basic aggregates and a simple join. Similarly, the other example uses piper to extend the capabilities of a PickleDB key-value store with the basic aggregates and simple join currently available in the package index.

After installing aggsPack and simpleJoin, the following command runs the MongoDB document store example from the top directory: 
```
python examples/mongodb-ex/src/mongo_piper.py
``` 
The output details the contents of the database and the results of applying all the basic aggregates and the simple join on the contents.

The following command performs a similar action for a PickleDB key-value store:
```
python examples/pickledb-ex/src/pickle_piper.py 
``` 

## Dependencies

### Python
* [pymongo](https://api.mongodb.com/python/2.7.2/installation.html)
* [pickledb](https://pythonhosted.org/pickleDB/)

### Other
* [MongoDB](https://docs.mongodb.com/manual/installation/)

While the vision of Piper is the support of arbitrarily defined NoSQL database systems, the Piper prototype currently only supports MongoDB and PickleDB as underyling database infrastructure options. In particular, running some subset of the examples requires the prior installation of MongoDB or PickleDB either globally or locally on your machine. 

