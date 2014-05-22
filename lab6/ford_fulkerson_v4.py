class Edge(object):
	def __init__(self,u,v,w):
		self.source=u
		self.sink=v
		self.capacity=w
	def __repr__(self):
		return "%s->%s:%s" % (self.source,self.sink,self.capacity)

class FlowNetwork(object):
	def __init__(self):
		self.adj={}
		self.flow={}

	def add_vertex(self, vertex):
		self.adj[vertex]=[]

	def get_edges(self,v):
		return self.adj[v]

	def add_edge(self,u,v,w=0):
		if u==v:
			raise ValueError("u"=="v")
		edge=Edge(u,v,w)
		redge=Edge(v,u,w)
		edge.redge=redge
		redge.redge=edge
		self.adj[u].append(edge)
		self.adj[v].append(redge)
		self.flow[edge]=0
		self.flow[redge]=0

	def find_path(self,source,sink,path):
		if source == sink:
			return path
		edges=self.get_edges(source)
		for edge in edges:
			residual=edge.capacity-self.flow[edge]
			if residual>0 and edge not in path:
				newpath=self.find_path(edge.sink,sink,path+[edge])
				if newpath != None:
					return newpath
		return None

	def min_cut(self,source):
		queue=[]
		visited=[]
		queue.append(source)
		while queue:
			v=queue.pop(0)
			visited.append(v)
			edges=self.get_edges(v)
			for edge in edges:
				residual=edge.capacity-self.flow[edge]
				if residual>0 and edge.sink not in visited:
					queue.append(edge.sink)
		mincut=[]
		for v in visited:
			edges=self.get_edges(v)
			for edge in edges:
				if edge.sink not in visited and edge.capacity>0:
					mincut.append(edge)
		return mincut


	def find_path_bfs(self,source,sink):
            queue=[]
	    visited=[]
	    path={}
	    queue.append(source)
	    while queue:
	    	v=queue.pop(0)
	    	visited.append(v)
	    	edges=self.get_edges(v)
	    	for edge in edges:
	    		residual=edge.capacity-self.flow[edge]
	    		if residual>0 and edge.sink not in visited:
	    			queue.append(edge.sink)
				if not path.has_key(edge.sink):
					path[edge.sink]=[]
				path[edge.sink]+=[edge]
				if edge.sink==sink:
					return path[edge.sink]
	    return None

    
	def max_flow(self,source,sink):
		path=self.find_path(source,sink,[])
		while path!=None:
			residuals=[edge.capacity-self.flow[edge] for edge in path]
			flow = min(residuals)
			for edge in path:
				self.flow[edge]+=flow
				self.flow[edge.redge]-=flow
			path=self.find_path(source,sink,[])
			print sum(self.flow[edge] for edge in self.get_edges(0))
		return sum(self.flow[edge] for edge in self.get_edges(source))


if __name__=='__main__':
    f = open('rail.txt','r')
    g = FlowNetwork()
    for v in range(55):
        g.add_vertex(v)
    for line in f:
        line=line.strip().split()
        u=int(line[0])
        v=int(line[1])
        w=int(line[2])
        if w==-1:
            w=float("inf")
        g.add_edge(u,v,w)
    print g.max_flow(0,54)
    for edge in g.min_cut(0):
        print edge
    '''
    g = FlowNetwork()
    for v in 'sopqrt':
        g.add_vertex(v)
    g.add_edge('s','o',10)
    g.add_edge('s','p',10)
    g.add_edge('o','p',2)
    g.add_edge('o','q',4)
    g.add_edge('o','r',8)
    g.add_edge('p','r',9)
    g.add_edge('r','q',6)
    g.add_edge('r','t',10)
    g.add_edge('q','t',10)
    print g.max_flow('s','t')
    for edge in g.min_cut('s'):
        print edge
    #print g.find_path_bfs('s')
    '''