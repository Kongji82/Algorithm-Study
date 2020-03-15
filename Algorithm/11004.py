# Boj 11004

def quick_seletion(arr, k):
    pivot = arr[len(arr) + 1//2 - 1]
    left, mid, right = [], [], []
    
    for i in range(len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] > pivot:
            right.append(arr[i])
        else:
            mid.append(arr[i])
        
    if k < len(left):
        return quick_seletion(left, k)
    elif k < len(left) + len(mid):
        return mid[0]
    else:
        return quick_seletion(right, k - len(left) - len(mid))
            

N, K = map(int, input().split())
num = list(map(int, input().split()))
print(quick_seletion(num, K-1))

