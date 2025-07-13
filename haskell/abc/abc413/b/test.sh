#!/bin/bash

ghc ./Main.hs

echo "ex1"
echo "  want: 11"
echo -n "  got : "
./Main < ./ex1

echo "ex2"
echo "  want: 7"
echo -n "  got : "
./Main < ./ex2

echo "ex3"
echo "  want: 90"
echo -n "  got : "
./Main < ./ex3
