# Problem: Masha and Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

t = int(input())
for a in range(t):
    b = int(input())
    c = list(map(int, input().split()))

    def beauty_tree(d):
        if len(d) == 1:
            return (0, d)
        e = len(d) // 2
        f, g = beauty_tree(d[:e])
        h, i = beauty_tree(d[e:])
        
        if f == -1 or h == -1:
            j = None
            k = None
        else:
            if g[-1] < i[0]:
                j = (f + h, g + i)
            else:
                j = None
            
            if i[-1] < g[0]:
                k = (f + h + 1, i + g)
            else:
                k = None
        
        if j is None and k is None:
            return (-1, [])
        elif j is None:
            return k
        elif k is None:
            return j
        else:
            if j[0] <= k[0]:
                return j
            else:
                return k

    l, m = beauty_tree(c)
    print(l)
