import sys
def sequece_alignment(x,y,header,matrix):
	Fun=[]
	path=dict()
	path[(0,0)]=[]
	for i in range(len(x)+1):
		row=[]
		for j in range(len(y)+1):
			row.append(0)
		Fun.append(row)

	for i in range(len(x)+1):
		Fun[i][0]=-4*i
		if i-1>=0:
			path[(i,0)]=path[(i-1,0)]+[(x[i-1],'-')]
	for j in range(len(y)+1):
		Fun[0][j]=-4*j
		if j-1>=0:
			path[(0,j)]=path[(0,j-1)]+[('-',y[j-1])]
	
	for i in range(1,len(x)+1):
		for j in range(1,len(y)+1):
			index_xi=header[x[i-1]]
			index_yj=header[y[j-1]]
			score1=int(matrix[index_xi][index_yj])+Fun[i-1][j-1]
			score2=-4+Fun[i][j-1]
			score3=-4+Fun[i-1][j]
			Fun[i][j]=max(score1,score2,score3)
			if Fun[i][j]==score1:
				path[(i,j)]=path[(i-1,j-1)]+[(x[i-1],y[j-1])]
			if Fun[i][j]==score2:
				path[(i,j)]=path[(i,j-1)]+[('-',y[j-1])]
			if Fun[i][j]==score3:
				path[(i,j)]=path[(i-1,j)]+[(x[i-1],'-')]

	return Fun,path

def read_matrix(f1):
	header=dict()
	matrix=[]
	fp=open(f1,'r')
	lines=fp.readlines()
	lines=lines[0].split('\r')
	i=0
	for line in lines:
		line=line.split()
		if i==0:
			j=0
			for item in line:
				header[item]=j
				j+=1
		else:
			removed=line.pop(0)
			matrix.append(line)
		i+=1
	return header,matrix

def parser(f2):
	d=dict()
	fp=open(f2,'r')
	value=''
	name=''
	for line in fp:
		line=line.strip()
		if line[0]=='>':
			if name and value:
				d[name]=value
			name=line.split()[0].lstrip('>')
			value=''
		else:
			value+=line
	d[name]=value
	return d

if __name__=='__main__':
	header,matrix=read_matrix('BLOSUM62.txt')
	
	d=parser('HbB_FASTAs.in')
	x=sys.argv[1]
	y=sys.argv[2]

	d['Sphinx']='KQRK'
	d['Bandersnatch']='KAK'
	d['Snark']='KQRIKAAKABK'
	Fun,path=sequece_alignment(d[x],d[y],header,matrix)
	
	Path=path[(len(d[x]),len(d[y]))]
	path1=''
	path2=''
	for item in Path:
		path1+=item[0]
		path2+=item[1]
	print x+'--'+y+':',Fun[len(d[x])][len(d[y])]
	print path1
	print path2
