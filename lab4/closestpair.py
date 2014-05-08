#-*- coding: utf-8 -*-
from operator import itemgetter
import math
def divide_conqure(Plx,Ply):
	print Plx
	size=len(Plx)
	if size==2:
		return distance(Plx[0],Plx[1])
	if size==1:
		return float("inf")
	Plx1=Plx[0:size/2]
	Plx2=Plx[size/2:size]
	Ply1=sorted(Plx1,key=itemgetter(1))
	Ply2=sorted(Plx2,key=itemgetter(1))
	d1=divide_conqure(Plx1,Ply1)
	d2=divide_conqure(Plx2,Ply2)
	d = min(d1,d2)
	L = (Plx[size/2-1][0]+Plx[size/2][0])/2.0
	region=[]
	for point in Ply:
		x=point[0]
		if x>= L-d and x<= L+d:
			region.append(point)
	for i in range(0,len(region)-1):
		for j in range(1,16):
			if i+j<len(region):
				d=min(d,distance(region[i],region[i+j]))
	return d



def distance(p1,p2):
	return math.sqrt((p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1]))

if __name__ == '__main__':
	pl=[]
	pl.append((0.25,2))
	pl.append((-0.25,2))
	pl.append((-20,1))
	pl.append((-20,0))
	pl.append((20,2))
	pl.append((20,0))
	Plx = sorted(pl, key=itemgetter(0))
	Ply = sorted(pl, key=itemgetter(1))
	d=divide_conqure(Plx,Ply)
	print d