# piper
A package index and management system for database management tools.

## Dependencies
While the vision of Piper is the support of arbitrarily defined NoSQL database systems, the Piper prototype currently only supports RocksDB and MongoDB as underyling infrastructure. In particular, running some subset of the examples requires the prior installation of RocksDB or MongoDB either globally or locally on your machine. 

The setup.py script attempts to install/update both RocksDB and MongoDB automatically using HomeBrew (yes, very presumptuous). However, local installations of the NoSQL systems is currently the responsibility of the user.

* [RocksDB](https://github.com/facebook/rocksdb/blob/master/INSTALL.md)
* [MongoDB](https://docs.mongodb.com/manual/installation/)
