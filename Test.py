import random 
import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2] 

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot] 

    return quick_sort(left) + middle + quick_sort(right)

array = list(range(1, 1000001))
random.shuffle(array)

start_time = time.perf_counter()
quick_sort(array)
end_time = time.perf_counter()
Shuffle_case = end_time - start_time
print("Shuffle : ", Shuffle_case)

