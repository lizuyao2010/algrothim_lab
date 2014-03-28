import sys
def match(men,women,pref):
	#initial data structure
	'''
	men=[1,3,5]
	women=[2,4,6]
	pref={1:[6,4,2],2:[3,5,1],3:[2,6,4],4:[5,1,3],5:[6,4,2],6:[1,5,3]}
	'''
	freemen=[]
	for m in men:
		freemen.append(m)
	wife={}
	husband={}
	for m in men:
		wife[m]=0
	for w in women:
		husband[w]=0

	proposal={}
	for m in men:
		proposal[m]=0

	inverse={}
	for w in women:
		inverse[w]={}
		n=1
		for m in pref[w]:
			inverse[w][m]=n
			n+=1
	while freemen:
		m=freemen.pop(0)
		if proposal[m]<len(women):
			# do proposal
			p=proposal[m]
			proposal[m]+=1

			w=pref[m][p]
			currenthusband=husband[w]
			if currenthusband==0:
				husband[w]=m
				wife[m]=w
			elif inverse[w][m] < inverse[w][currenthusband]:
				husband[w]=m
				wife[m]=w
				wife[currenthusband]=0
				freemen.append(currenthusband)
			else:
				# w rejects m
				#print w,"rejects",m
				freemen.append(m)

		else:
			# has proposed to every women
			print m,"has proposed to every women"
			break
	
	return wife

def read_input(fileName):
	fin=open(fileName,'r')
	n=0
	men={}
	women={}
	pref={}
	flag=0
	for line in fin:
		if line=='\n':
			flag=1
		if line[0]=='#':
			continue # it's comment
		elif line[0]=='n':
			n=int(line.split('=')[1].strip())
		elif flag==0 and line[0].isdigit():
			keyvalue=line.strip().split()
			key=int(keyvalue[0])
			value=keyvalue[1]
			if key%2 != 0:
				men[key]=value
			else:
				women[key]=value
		elif flag==1 and line[0].isdigit():
			line=line.strip().split(':')
			key=int(line[0])
			ls=line[1].strip().split()
			i=0
			while i< len(ls):
				ls[i]=int(ls[i])
				i+=1
			pref[key]=ls
		else:
			None
	return men,women,pref


if __name__=='__main__':
	fileName=sys.argv[1]
	men,women,pref=read_input(fileName)
	wife=match(sorted(men.keys()),sorted(women.keys()),pref)
	for m in sorted(men.keys()):
		print men[m],'--',women[wife[m]]
