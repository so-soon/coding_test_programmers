from collections import deque,defaultdict


def solution(land, height):
    answer = 0
    row = len(land)
    col = len(land[0])

    visited = []



    vi_co = 0

    for i in range(row):
        temp = []
        for j in range(col):
            temp.append(0)
        visited.append(temp)

    for i in range(row):
        for j in range(col):
            if visited[i][j] != 0:
                continue
            else:
                deq = deque()
                deq.append([i, j])
                vi_co += 1

                visited[i][j] = vi_co

                while len(deq) != 0:
                    r = deq[0][0]
                    c = deq[0][1]
                    deq.popleft()

                    if (r + 1) < row and (r + 1) >= 0 and c < col and c >= 0:
                        if abs(land[r][c] - land[r + 1][c]) <= height and visited[r + 1][c] == 0:
                            deq.append([r + 1, c])
                            visited[r + 1][c] = vi_co
                    if (r - 1) < row and (r - 1) >= 0 and c < col and c >= 0:
                        if abs(land[r][c] - land[r - 1][c]) <= height and visited[r - 1][c] == 0:
                            deq.append([r - 1, c])
                            visited[r - 1][c] = vi_co
                    if r < row and r >= 0 and (c + 1) < col and (c + 1) >= 0:
                        if abs(land[r][c] - land[r][c + 1]) <= height and visited[r][c + 1] == 0:
                            deq.append([r, c + 1])
                            visited[r][c + 1] = vi_co
                    if r < row and r >= 0 and (c - 1) < col and (c - 1) >= 0:
                        if abs(land[r][c] - land[r][c - 1]) <= height and visited[r][c - 1] == 0:
                            deq.append([r, c - 1])
                            visited[r][c - 1] = vi_co

    dir = [ [1,0] , [-1,0] , [0,1], [0,-1] ]
    cost = defaultdict(lambda :10000)
    is_connected = []
    for r in range(row):
        for c in range(col):
            for dr,dc in dir:
                if 0 <= r+dr < row and 0 <= c + dc < col:
                    if visited[r+dr][c+dc] < visited[r][c]:
                        continue
                    elif visited[r+dr][c+dc] > visited[r][c]:
                        cost[(visited[r][c],visited[r+dr][c+dc])] = min(cost[(visited[r][c],visited[r+dr][c+dc])],abs(land[r][c] - land[r+dr][c+dc]))


    cost = sorted(cost.items(),key=lambda x:x[1])


    global root
    root = [-1]
    for i in range(1, vi_co + 1):
        root.append(i)

    for (s,e),c in cost:
        root_x = u_find(s)
        root_y = u_find(e)

        if root_x != root_y:
            u_union(s,e)
            answer+=c


    return answer


def u_find(x):
    global root

    if root[x] == x:
        return x
    else:
        root[x] = u_find(root[x])
        return root[x]

def u_union(x,y):
    global root

    x = u_find(x)
    y = u_find(y)

    root[y] = x
