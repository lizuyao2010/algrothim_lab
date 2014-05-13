#-*- coding: utf-8 -*-
from operator import itemgetter
import math,sys

def parser(input):
	fin=open(input,'r')
	flag=False
	pl=[]
	for line in fin:
		line=line.strip()
		if line=='EOF' or line=='':
			break
		if line=='NODE_COORD_SECTION':
			flag=True
			continue
		if flag==True:
			line=line.split()
			x=float(line[1].strip())
			y=float(line[2].strip())
			pl.append((x,y))
	return pl

def divide_conqure(pointListx,pointListy):
	size=len(pointListx)
	if size==2:
		return distance(pointListx[0],pointListx[1])
	if size==1:
		return float("inf")
	pointListx1=pointListx[0:size/2]
	pointListx2=pointListx[size/2:size]
	L = (pointListx[size/2-1][0]+pointListx[size/2][0])/2.0
	'''
	pointListy1=[]
	pointListy2=[]
	for point in pointListy:
		x=point[0]
		if x < L:
			pointListy1.append(point)
		else:
			pointListy2.append(point)
	'''
	
	pointListy1=sorted(pointListx1,key=itemgetter(1))
	pointListy2=sorted(pointListx2,key=itemgetter(1))
	
	d1=divide_conqure(pointListx1,pointListy1)
	d2=divide_conqure(pointListx2,pointListy2)
	d = min(d1,d2)
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
	
	fin=open(sys.argv[1],'r')
	for line in fin:
		line=line.strip()
		if line=='':
			break
		line=line.split(':')
		filein=line[0]
		pl=parser(filein)
		pointListx = sorted(pl, key=itemgetter(0))
		pointListy = sorted(pl, key=itemgetter(1))
		d=divide_conqure(pointListx,pointListy)
		print filein+':',len(pl),d
	