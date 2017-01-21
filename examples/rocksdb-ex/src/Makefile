#IDIR =../include
IDIR=/afs/cats.ucsc.edu/users/j/kmdahlgr/software/rocksdb/build/include
CXX=g++
CXXFLAGS=-std=c++11 -Wall -g -I$(IDIR)

ODIR=../obj
#LDIR =../lib

LFLAGS=-L/afs/cats.ucsc.edu/users/j/kmdahlgr/software/rocksdb/build/lib -L/afs/cats.ucsc.edu/users/j/kmdahlgr/software/bzip2/build/lib -L/afs/cats.ucsc.edu/users/j/kmdahlgr/software/snappy/build/lib
LIBS=-lrocksdb -lbz2 -lsnappy -lz -lpthread -lrt

#_DEPS = hellomake.h
#DEPS = $(patsubst %,$(IDIR)/%,$(_DEPS))

_OBJ = myfile.o
OBJ = $(patsubst %,$(ODIR)/%,$(_OBJ))

EXEC=test3

$(ODIR)/%.o: %.cpp $(DEPS)
        $(CXX) -c -o $@ $< $(CXXFLAGS)

$(EXEC): $(OBJ)
        g++ -o $@ $^ $(CXXFLAGS) $(LFLAGS) $(LIBS)

.PHONY: clean

clean:
	rm -f $(EXEC) $(ODIR)/*.o *~ core $(IDIR)/*~
