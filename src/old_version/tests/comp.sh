#!bin/bash

mkdir bin
gcc gonnacry.c lib/func.c lib/struct.c lib/crypto.c -o bin/gonnacry -lcrypto
