import random
from Sorts import hybrid_sort, quick_sort
import time
# inital test

arr = [4, 2, 7, 1, 9, 3, 2, 5, 8, 3, 2, 1, 5, 6, 8, 9, 0]
print("original:", arr)
hybrid_sort(arr, threshold=10)
print("sorted:", arr)

# testing
log = []
hybrid_times = []
quick_times = []
for x in range(1000):
    arr = []
    arr2 = []
    for _ in range(1000):
        x = random.randint(1,10000)
        arr.append(x)
        arr2.append(x)

    t1 = time.time()
    hybrid_sort(arr, threshold=10)
    t2 = time.time()

    t3 = time.time()
    arr3 = quick_sort(arr2)
    t4 = time.time()
    hybrid_times.append(t2-t1)
    quick_times.append(t4-t3)
    val = min(("hybrid", t2-t1), ("quicksort", t4-t3), key = lambda x: x[1])
    log.append(val[0])



hybrid = 0
quick = 0
for x in log:
    if x == "hybrid":
        hybrid += 1
    else:
        quick += 1
results = "hybrid: {}% \nquicksort: {}%".format((hybrid/len(log))*100, (quick/len(log))*100)
print(results)