def ford_fulkerson(G,s,t):
    Gf=redisdualgraph(G)
    print Gf
    #(id,flow,residual)
    path = find_path(Gf,s,t) 
    while path:
        print path
        Gf=augment(path,Gf)
        print Gf
        path = find_path(Gf,s,t)

    print Gf

def update(node1,node2,minresidual,Gf):
    index=0
    for edge in Gf[node1]:
        if edge[0]==node2:
            edge[1]-=minresidual
            Gf[node1][index]=[node2,edge[1]]
        index+=1
    index=0
    for edge in Gf[node2]:
        if edge[0]==node1:
            edge[1]+=minresidual
            Gf[node2][index]=[node1,edge[1]]
        index+=1
    #print Gf
    return Gf

def augment(path,Gf):
    minresidual = path[1][1]
    for i in range(2,len(path)):
        if path[i][1]< minresidual:
        	minresidual=path[i][1]

    for i in range(len(path)):
    	if i+1<=(len(path)-1):
            Gf=update(path[i][0],path[i+1][0],minresidual,Gf)

    return Gf
        

def find_path(graph, start, end, path=[],edgelen=0):
    path = path + [(start,edgelen)]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node[0] not in path and node[1]>0:
            newpath = find_path(graph, node[0], end, path, node[1])
            if newpath: 
                return newpath
    return None

def redisdualgraph(graph):
    G=dict()
    for key in graph.keys():
        G[key]=[]
    for key in graph.keys():
        values=graph[key]
        for value in values:
            #(id,residual)
            G[key].append([value[0],value[2]])
            #(key,flow)
            G[value[0]].append([key,value[1]])
    return G

if __name__=='__main__':
    # (id,flow,capcity)
    graph = {1: [[2,0,10],[3,0,10]],
             2: [[3,0,2],[4,0,4],[5,0,8]],
             3: [[5,0,9]],
             4: [[6,0,10]],
             5: [[4,0,6],[6,0,10]],
             6: []}
    
    ford_fulkerson(graph,1,6)
