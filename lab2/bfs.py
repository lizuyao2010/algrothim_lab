def bfs(G,source,destination):
  path={}
  Q=[]
  V=[]
  Q.append(source)
  V.append(source)
  path[source]=[]
  while Q:
    t=Q.pop(0)
    if t==destination:
       path[destination]=path[t]
       return len(path[destination])
    for word in G[t]:
       if word not in V:
          V.append(word)
          Q.append(word)
          path[word]=path[t]+[word]
  return -1
def build_graph(dataFile):
  ls=[]
  G={}
  f=open(dataFile,'r')
  for row in f:
    ls.append(row)
  
  for word in ls:
    G[word]=[]
    last4=word[1:]
    for w in ls:  
      if exists(last4,w):
         G[word].append(w)

  return G
    
def exists(last4,word):
  wordls=[]
  for l in word:
    wordls.append(l)
  for letter in last4:
    if letter not in wordls:
       return False
    wordls.remove(letter)
  return True

if __name__=='__main__':
   G={'grass':['stars'],'stars':['parts','start'],'parts':['stars','start'],'start':[]}
   source='parts'
   destination='grass'
   #distance=bfs(G,source,destination)
   #print distance
   '''
   if exists('here','where'):
     print 'Yes'
   else:
     print 'No'
   '''
   print build_graph('data/words-10.dat')
