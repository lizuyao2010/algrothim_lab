def sequece_alignment(x,y,header,matrix):
	Fun=[]
	for i in range(len(x)+1):
		row=[]
		for j in range(len(y)+1):
			row.append(0)
		Fun.append(row)
	for i in range(len(x)+1):
		Fun[i][0]=-4*i
	for j in range(len(y)+1):
		Fun[0][j]=-4*j
	
	for i in range(1,len(x)+1):
		for j in range(1,len(y)+1):
			index_xi=header[x[i-1]]
			index_yj=header[y[j-1]]
			Fun[i][j]=max(int(matrix[index_xi][index_yj])+Fun[i-1][j-1],-4+Fun[i][j-1],-4+Fun[i-1][j])
	return Fun

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

if __name__=='__main__':
	header,matrix=read_matrix('BLOSUM62.txt')
	d=dict()
	d['Sphinx']='KQRK'
	d['Bandersnatch']='KAK'
	d['Snark']='KQRIKAAKABK'
	x='Snark'
	y='Bandersnatch'
	Fun=sequece_alignment(d[x],d[y],header,matrix)
	print Fun
