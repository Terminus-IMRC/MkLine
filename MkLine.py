#!/usr/bin/env python
import os

X=5
Ceilings=X**2
OneLine=X*(Ceilings+1)/2

ar=[-1]*(X-2)
#res=[[]]*((OneLine-1-2)-(OneLine-Ceilings-Ceilings-1))
res=[]
dned=[False]*Ceilings

def MkLine(level):
	if level==X-2:
		chk_and_add()
	else:
		for i in range(0, Ceilings):
			if dned[i]:
				continue
			ar[level]=i
			dned[i]=True
			MkLine(level+1)
			dned[i]=False

def chk_and_add():
	sum=0
	for i in ar:
		sum+=i
	if (OneLine-Ceilings-Ceilings-1)<=sum and sum<=(OneLine-1-2):
		res[sum-1-(OneLine-Ceilings-Ceilings-1)].append([-1]*(X-2))
		print res
		for i in range(0, X-2):
			res[sum-1-(OneLine-Ceilings-Ceilings-1)][i]=ar[i]
		#res[sum-1-(OneLine-Ceilings-Ceilings-1)].append(ar)
		#print ar

def outar():
	os.chdir("out")
	for i in range(OneLine-Ceilings-Ceilings-1, OneLine-1-2+1):
		f=open(str(i), "w")
		for j in res[i]:
			for k in j:
				f.write(str(k)+"\t")
			f.write("\n")
		f.close()

def mine():
	for i in range(0, (OneLine-1-2)-(OneLine-Ceilings-Ceilings-1)):
		res.append([])
	print res
	MkLine(0)
	outar()

if __name__=='__main__':
	mine()
