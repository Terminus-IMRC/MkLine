#!/usr/bin/env python
import os, sys

X=0
Ceilings=0
OneLine=0

ar=[-1]*(X-2)
#res=[[]]*((OneLine-1-2)-(OneLine-Ceilings-Ceilings-1))
res=[[] for i in range((OneLine-1-2)-(OneLine-Ceilings-(Ceilings-1)) +1 )]
dned=[False]*Ceilings

def MkLine(level):
	if level==X-2:
		chk_and_add()
	else:
		for i in range(1, Ceilings+1):
			if dned[i-1]:
				continue
			ar[level]=i
			dned[i-1]=True
			MkLine(level+1)
			dned[i-1]=False

def chk_and_add():
	sum=0
	for i in ar:
		sum+=i
	if (OneLine-Ceilings-(Ceilings-1))<=sum and sum<=(OneLine-1-2):
		res[sum-(OneLine-Ceilings-(Ceilings-1))].append([-1]*(X-2))
		l=len(res[sum-(OneLine-Ceilings-(Ceilings-1))])
		for i in range(0, X-2):
			res[sum-(OneLine-Ceilings-(Ceilings-1))][l-1][i] = ar[i]

def outar():
	os.system("rm -rf out; mkdir out")
	os.chdir("out")
	for i in range(0, (OneLine-1-2)-(OneLine-Ceilings-(Ceilings-1))+1):
		f=open(str(i+(OneLine-Ceilings-(Ceilings-1))), "w")
		for j in res[i]:
			for k in j:
				f.write(str(k)+"\t")
			f.write("\n")
		f.close()

def mine():
	if len(sys.argv)!=2:
		print >>sys.stderr, "Invalid the argument."
		exit(1)
	X=int(sys.argv[1])
	Ceilings=X*X
	OneLine=X*(Ceilings+1)/2
	MkLine(0)
	outar()

if __name__=='__main__':
	mine()
