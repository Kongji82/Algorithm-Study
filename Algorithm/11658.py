def query(field, x, y):
    result = 0
    for i in range(y):
        for j in range(x):
            result += field[i][j]
            
    return result

# N, M = map(int, input().split())
# field = []
# for _ in range(N):
#     field.append(list(map(int, input().split())))

# for x in range(M):
#     temp = list(map(int, input().split()))
#     if temp[0] == 0:
#         field[temp[2] - 1][temp[1] - 1] = temp[3]
#     elif temp[0] == 1:
#         result = query(field, temp[3], temp[4]) + query(field, temp[1], temp[2]) - query(field, temp[1], temp[4]) - query(field, temp[3], temp[2])
#         print(result)
field = [[1,2,3,4], [2,3,4,5]]
print(query(field, 3,2))