class Leidfinnur:

    def pathfinding(self,themap, epos, playpos, width, height):
        di = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        vis = {}
        fro = {}
        q = []
        q.append(epos)
        vis[epos] = 2
        fro[epos] = epos
        while(len(q) != 0):
            #print q[0]
            at = q[0]
            q.pop(0)
            for x in range(4):
                ne = (at[0]+di[x][0], at[1]+di[x][1])
                if 0 <= ne[0] and ne[0] < width and 0 <= ne[1] and ne[1] < height:
                    if ne not in vis:
                        if themap[ne] != "W" and themap[ne] != "M" :
                                q.append(ne)
                                vis[ne] = 1
                                fro[ne] = at

        #print(len(vis))
        if playpos in vis:
            cache = []
            row = []
            at = playpos
            while True:
                if at in fro:
                    if fro[at] != at:
                        row.append(at)
                        cache.append(at)
                        at = fro[at]
                    else:
                        break
            row.reverse()
            return row
        else:
            return []

    def Rect(self,r1x, r1y, r1w, r1h, r2x, r2y, r2w, r2h):
        if not (r2x > r1x + r1w or r2x + r2w < r1x or r2y > r1y + r1h or r2y + r2h < r1y):
            return True

    def GetDirections(self,at, to):
            print at,to
            if at[0] < to[0] and at[1] < to[1]:
                print "Ska"
                return(1,1)
            if at[0] > to[0] and at[1] > to[1]:
                print "Ska"
                return(-1,-1)
            if at[0] < to[0] and at[1] > to[1]:
                print "Ska"
                return(1,-1)
            elif at[0] > to[0] and at[1] < to[1]:
                print "ska"
                return(-1,1)
            elif at[0] < to[0]:
                return (1, 0)
            elif at[0] > to[0]:
                return (-1, 0)
            elif at[1] < to[1]:
                return (0, 1)
            elif at[1] > to[1]:
                return (0, -1)


    def findcord(self,posx, posy):
            area = 0
            best = (0, 0)
            for x in range(40):
                for y in range(30):
                    cordx = x * 16
                    cordy = y * 16
                    if self.Rect(posx, posy, 1, 1, cordx, cordy, 16, 16):
                        holdarea = self.calcarea(posx, posy, 1, 1, x, y, 16, 16)
                        if holdarea > area:
                            best = (x, y)
                            area = holdarea
            return best

    def calcarea(self,A, B, C, D, E, F, G, H):
            SA = abs((C - A) * (D - B))
            SB = abs((G - E) * (H - F))
            if E >= C or A >= G or B >= H or F >= D:
                return SA + B
            else:
                x1 = min(G, C)
                x2 = max(A, E)
                y1 = min(D, H)
                y2 = max(B, F)
                return SA + SB - abs((x1 - x2) * (y1 - y2))
