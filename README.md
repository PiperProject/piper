# piper
A package index and management system for database management tools organized on Github under the organization of the Piper Project. The base "piper" package encompasses the basic manaagement code necessary for integrating packages from the Piper Project over your underlying NoSQL system. NoSQL databases currently supported by the index include: MongoDB and PickleDB. With piper, users can pull all and only the database management tools from the package index maintained under the Piper Project relevant to their needs.

## Installing piper
Installing the base piper index and management software is as easy as cloning the repository:
```git clone https://github.com/PiperProject/piper.git```

However, installing piper does not include any default packages from the index. Users pull specific packages from the index explicitly. For example, suppose a user intends to augment the capabilities of an underlying NoSQL system with the basic set of aggregate operations rendered canonical by RDBMSs in the 1990s and early 2000s. The aggsPack package in the index supports all five canonical aggregates (COUNT, SUM, AVERAGE, MIN, MAX). To pull the package, run the following command from the top of the piper/ directory:
```python ./src/drivers/piper.py install aggsPack```

piper also supports explicit package updates with the command:
```python ./src/drivers/piper.py update```

Finally, piper supports the easy deinstallation of packages loaded from the index:
```python ./src/drivers/piper.py uninstall aggsPack```

## Dependencies

### Python
* [pymongo](https://api.mongodb.com/python/2.7.2/installation.html)
* [pickledb](https://api.mongodb.com/python/2.7.2/installation.html://pypi.python.org/pypi/pickleDB)

### Other
* [MongoDB](https://docs.mongodb.com/manual/installation/)

While the vision of Piper is the support of arbitrarily defined NoSQL database systems, the Piper prototype currently only supports MongoDB and PickleDB as underyling database infrastructure options. In particular, running some subset of the examples requires the prior installation of MongoDB or PickleDB either globally or locally on your machine. 

