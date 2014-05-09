import math
fcorrect=open('closest-pair.out','r')
four=open('ouroutput.txt','r')
correct=[]
ours=[]
for line in fcorrect:
	line=line.strip()
	line=line.split()
	correct.append(float(line[2]))

for line in four:
	line=line.strip()
	line=line.split()
	ours.append(float(line[2]))

sum=0
for i in range(0,len(correct)):
	differ=math.fabs(correct[i]-ours[i])
	sum+=differ
print sum