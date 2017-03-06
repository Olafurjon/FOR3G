
def pathfinding(themap, epos, playpos, height, width):
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    vis = {}
    fro = {}
    q = []
    q.append(epos)
    vis[epos] = 1
    fro[epos] = epos
    while(len(q) != 0):
        at = q[0]
        q.pop(0)
        for x in range(4):
            ne = [at[0]+dx[x], at[1]+dy[x]]
            if 0 <= ne[0] and ne[0] < width and 0 <= ne[1] and ne[1] < height:
                if ne not in vis:
                    if themap[ne] != 'W' and themap[ne] != 'M':
                        q.push(ne)
                        vis[ne] = 1
                        fro[ne] = at
    if playpos in vis:
        row = []
        at = playpos
        while True:
            if at in vis:
                if vis[at] != at:
                    row.append(at)
                    at = vis[at]
                else:
                    break
        row = reversed(row)
        return row
    else:
        return ["impossible"]



