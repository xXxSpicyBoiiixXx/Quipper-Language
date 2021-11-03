## Installation 

I will be utilzing the MacOS interface but if I run into problems with the operating system I will move to Linux. 

You will need brew installed to complete the installation process, you can download brew package manager at the link below. 

https://brew.sh

The first step is to make sure to get cabal, update it, and install quipper. To do so simply type below. 

brew install cabal-install
cabal update 
cabal install quipper

If this method fails, we can go ahead with the legacy installation, so make sure you get the tar file below 

https://www.mathstat.dal.ca/~selinger/quipper/downloads/quipper-0.9.0.0.tgz

Once downloaded, navigate in your terminal to the file and type 

tar -xvf quipper-0.9.0.0.tgz 

It's important to note that if the version changes, just change the numbers for the version type that is downloaded. At the current moment we are on version 0.9.0.0. From here you will need to download some Haskell libraries which are done by the following commands. 

cabal install random
cabal install mtl 
cabal install primes 
cabal install Lattices 
cabal install zlib 
cabal install easyrender
cabal install fixedprec
cabal install newsynth
cabal install containers 
cabal install QuickCheck

