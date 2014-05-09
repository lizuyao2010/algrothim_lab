#-*- coding: utf-8 -*-
from operator import itemgetter
import math
def divide_conqure(pointListx,pointListy):
	size=len(pointListx)
	if size==2:
		return distance(pointListx[0],pointListx[1])
	if size==1:
		return float("inf")
	pointListx1=pointListx[0:size/2]
	pointListx2=pointListx[size/2:size]
	pointListy1=sorted(pointListx1,key=itemgetter(1))
	pointListy2=sorted(pointListx2,key=itemgetter(1))
	d1=divide_conqure(pointListx1,pointListy1)
	d2=divide_conqure(pointListx2,pointListy2)
	d = min(d1,d2)
	L = (pointListx[size/2-1][0]+pointListx[size/2][0])/2.0
	region=[]
	for point in pointListy:
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
	pointListx = sorted(pl, key=itemgetter(0))
	pointListy = sorted(pl, key=itemgetter(1))
	d=divide_conqure(pointListx,pointListy)
	print d