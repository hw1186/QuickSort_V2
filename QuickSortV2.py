import random
import time
import sys

# 재귀 호출 제한을 늘립니다.
sys.setrecursionlimit(10**6)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def quick_sortV2(arr):
    if len(arr) <= 10:
        return insertion_sort(arr)
    pivot = arr[len(arr) // 2]  # 중앙 값을 피벗으로 사용합니다.
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sortV2(left) + middle + quick_sortV2(right)

array = list(range(1, 1000001))
random.shuffle(array)

start_time = time.perf_counter()
array = quick_sortV2(array)
end_time = time.perf_counter()

QuickSort = end_time - start_time

# print(array)
print(QuickSort)
