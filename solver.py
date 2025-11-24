from collections import deque
import heapq

GOAL = (1,2,3,4,5,6,7,8,0)

NEIGHBORS = {
    0:[1,3], 1:[0,2,4], 2:[1,5],
    3:[0,4,6], 4:[1,3,5,7], 5:[2,4,8],
    6:[3,7], 7:[4,6,8], 8:[5,7]
}

def is_solvable(state):
    arr=[x for x in state if x!=0]
    inv=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]: inv+=1
    return inv%2==0

def manhattan(state):
    d=0
    for i,v in enumerate(state):
        if v==0: continue
        gi=GOAL.index(v)
        x1,y1=divmod(i,3)
        x2,y2=divmod(gi,3)
        d+=abs(x1-x2)+abs(y1-y2)
    return d

def neighbors(state):
    z=state.index(0)
    for nb in NEIGHBORS[z]:
        s=list(state)
        s[z],s[nb]=s[nb],s[z]
        yield tuple(s), state[nb]

def reconstruct(par, start, goal):
    path=[]
    cur=goal
    while cur!=start:
        prev, tile=par[cur]
        path.append(tile)
        cur=prev
    return list(reversed(path))

def bfs(start):
    if start==GOAL: return []
    if not is_solvable(start): return None

    q=deque([start])
    par={start:(None,None)}

    while q:
        st=q.popleft()
        if st==GOAL:
            return reconstruct(par, start, GOAL)

        for nb,tile in neighbors(st):
            if nb not in par:
                par[nb]=(st,tile)
                q.append(nb)
    return None

def astar(start):
    if start==GOAL: return []
    if not is_solvable(start): return None

    pq=[]
    g={start:0}
    par={start:(None,None)}

    heapq.heappush(pq,(manhattan(start),start))

    while pq:
        _,st=heapq.heappop(pq)

        if st==GOAL:
            return reconstruct(par, start, GOAL)

        for nb,tile in neighbors(st):
            ng=g[st]+1
            if nb not in g or ng<g[nb]:
                g[nb]=ng
                par[nb]=(st,tile)
                f=ng+manhattan(nb)
                heapq.heappush(pq,(f,nb))
    return None
