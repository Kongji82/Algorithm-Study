N, M = map(int, input().split())
field = []
for _ in range(N):
    field.append(list(map(int, input().split())))

for _ in range(M):
    temp = list(map(int, input().split()))
    if temp[0] == 0:
        field[temp[1]-1][temp[2]-1] = temp[3]
        print(field)
    elif temp[0] == 1:
        result = 0
        for i in range(temp[1]-1 , temp[3]):
            for j in range(temp[2]-1, temp[4]):
                result += field[i][j]
                    
        print(result)