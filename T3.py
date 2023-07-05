import time
import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2] 

    # 피벗 나누기 list Comprehension (Main Algorithm)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot] 


    return quick_sort(left) + middle + quick_sort(right) 


liner_ls = list(range(1, 1000001)) 
worst_case = list(range(1, 1000001, -1))

array = list(range(1, 1000001))
random.shuffle(array)


# Shuffle Case
start_time = time.time()
quick_sort(array)
end_time = time.time()
Shuffle_case = end_time - start_time
print("Shuffle : ", Shuffle_case)

# Worst Case
start_time = time.perf_counter() 
quick_sort(worst_case)
end_time = time.perf_counter() 
Worst_Time = end_time - start_time
print("Worst : ", Worst_Time)

# Quick Liner case
start_time = time.perf_counter() 
quick_sort(liner_ls)
end_time = time.perf_counter() 
Liner_Q = end_time - start_time
print("Liner_Q : ", Liner_Q)

# Tim case
start_time = time.time()
array.sort()
end_time = time.time()
Tim_Time = end_time - start_time
print("Timsort : ", Tim_Time)

