import random
def span(G):
	V=G.keys()
	seed=random.choice(V)
	Vnew=['A']#Vnew.append(seed)
	Enew=[]
	while len(Vnew)<len(V):
		min=['',1000000]
		for vnew in Vnew:
			for to in G[vnew].keys():
				if to not in Vnew:
					if G[vnew][to]<min[1]:
						min[0]=to
						min[1]=G[vnew][to]
		Vnew.append(min[0])
		Enew.append(min[1])
	return sum(Enew)
if __name__=='__main__':
	G={'A':{'B':2,'D':1},'B':{'A':2,'D':2},'C':{'D':3},'D':{'A':1,'B':2,'C':3}}
	print span(G)