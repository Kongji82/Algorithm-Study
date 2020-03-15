# Boj 11004

def quick_sort(num):
    if len(num) <= 1:
        return num
    pivot = num[len(num) // 2]
    less_arr, equal_arr, big_arr = [], [], []
    for i in num:
        if i < pivot:
            less_arr.append(i)
        elif i > pivot:
            big_arr.append(i)
        else:
            equal_arr.append(i)
    return quick_sort(less_arr) + equal_arr + quick_sort(big_arr)

N, K = map(int, input().split())
num = list(map(int, input().split()))
result = quick_sort(num)
print(result[K-1])