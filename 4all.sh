#!/bin/sh
X=$1
if ! [ $X ];then
	echo Specify X on commandline. >&2
	exit 1
fi

rm -rf e1 e2 e3

cc MkLine.c -DX=$X -DELEM=X-2 -DRANGE_MAX=OneLine-1-2 -DRANGE_MIN=OneLine-Ceilings-\(Ceilings-1\) -O2
./a.out
mv out e1

if [ $X -gt 5 ];then
	cc MkLine.c -DX=$X -DELEM=X-4 -DRANGE_MAX=OneLine-1-2-3 -DRANGE_MIN=OneLine-Ceilings-\(Ceilings-1\)-\(Ceilings-2\) -O2
	./a.out
	mv out e2
else
	echo Skipping experiment 2 because $X is not greater the 5.
fi

if [ $(($X%2)) -eq 1 ];then
	cc MkLine.c -DX=$X -DELEM=X-1 -DRANGE_MAX=OneLine-1 -DRANGE_MIN=OneLine-Ceilings -O2
	./a.out
	mv out e3
else
	echo Skipping experiment 3 because $X is even.
fi
