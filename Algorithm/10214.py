num = int(input())
yon = []
ko = []
for i in range(9):
    x, y = map(int, input().split())
    yon.append(x)
    ko.append(y)
for j in range(num):
    if yon[j] > ko[j]:
        print("Yonsei")
    elif yon[j] == ko[j]:
        print("Draw")
    else:
        print("Korea")