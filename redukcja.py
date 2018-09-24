
def kost(n, dir):
    for d in dir:
        dlr = 0
        if d== 'g' or d== 'd':
            n=zi(n)
        for i in range(len(n)):
            if d== 'l' or d== 'g':
                dlr=1
                n[i]=movelp(n[i],dlr)
            elif d== 'p' or d== 'd':
                dlr=1
                n[i].reverse()
                n[i]=movelp(n[i],dlr)
                n[i].reverse()
        if d== 'g' or d== 'd':
            n=zi(n)


    print(n)
    return n
def movelp(m,dlr):
    for i in range(dlr,len(m)):
        if m[i-1]==0 or m[i-1]==m[i]:
            g=i-1
            while m[g]==0 and g!=-1 or m[g]==m[g+1] and g!=-1:
                if m[g]==m[g+1]:
                    m[g]=(m.pop(g+1)*2)%10
                    m.insert(g+1,0)
                    g-=1
                else:
                    m[g]=m.pop(g+1)
                    m.insert(g+1,0)
                    g-=1
    return m

def zi(m):
    e=[]
    w=[]
    for i in range(len(m[0])):
        w.append(e.copy())
    for j in m:
        u=0
        for i in j:
            w[u].append(i)
            u+=1
    return w

#kost([[2,2,0],[3,0,3],[1,2,2]],'l')
#kost([[8,0,1],[0,1,0],[8,0,1]],'d')
#kost([[3,2,1],[0,3,1],[2,0,4]],'d')
#kost([[2,3,0],[5,3,1],[6,0,0]],'p')
#kost([[6,3,5,2,5],[7,3,0,0,3],[5,0,0,0,1]],'l')
#kost([[0,0,0],[1,2,3],[4,2,1]],'l') źle

assert kost([[0,2,4],[4,4,8],[4,0,8]],'dldld')==[[0,0,0],[0,0,0],[4,0,0]]
assert kost([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]],'lpdg')==[[0,0,0,6],[0,0,0,0],[0,0,0,0],[0,0,0,0]]