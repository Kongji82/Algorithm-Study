N = int(input())

binary = [0] * (N+1)
binary[0] = 1
binary[1] = 1

for i in range(2, N):
    binary[i] = binary[i-2] + binary[i-1]

print(binary[N-1])