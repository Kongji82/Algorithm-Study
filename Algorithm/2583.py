from collections import deque
M, N, K = map(int, input().split())
board = [[0 for x in range(N)] for y in range(M)]
for i in range(K):
    location = list(map(int, input().split()))
    for y in range(location[2]-location[0]):
        for x in range(location[3]-location[1]):
            board[location[1]+x][location[0]+y] = 1

dx = [-1, 0, 1, 0]            
dy = [0, 1, 0, -1]
reseult = []
def dfs(s1, s2):
    de = deque()
    de.append([s1, s2])
    board[s1][s2] = 1
    c = 1
    while de:
        x, y = de.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < M and 0 <= ny < N:
                if board[nx][ny] == 0:
                    board[nx][ny] = 1
                    c += 1
                    de.append([nx, ny])
    
    reseult.append(c)
    
for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            dfs(i, j)
            
print(len(reseult))
reseult.sort()
for i in reseult:
    print(i, end = ' ')