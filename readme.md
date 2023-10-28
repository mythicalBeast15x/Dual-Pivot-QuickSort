# Dual Pivot QuickSort
## Intoduction
#### The Dual Pivot Sort is an improvement on the Quick Sort. It uses Insertion Sort as well as a second pivot to help improve the efficency in specific scenarios.
## Goals
The goals of this algorithm is to improve the efficency of the algorithm for lists on the shorter side, as well as reduce the amount of recursions and swaps that are needed to sort the list.
Shorter lists are not optimal for QuickSort. In such a case, this sort is more efficent as it uses less recursive calls and element swaps in order to have a faster sorting time
## Algorithm Description
The DualPivot QuickSort uses a secondary pivot to swap the elements twice in a single call of the function. This reduces the number of recursive calls that the sort has to make. In addition to this, when the subarray shrinks beyond a certain length, the algorith switches to Insertion sort to prevent the efficency from plummeting When sorting smaller arrays.
The algorithm works by:
1). Choosing 2 pivots
2). Splitting the array into 3 segments (elements less than pivot 1, elements less than pivot 2, but greater than pivot 1, and elements greater than pivot 2)
3). Repeat steps 1 and 2 on each sub array until the sub_array length reaches the threshold
4). When the subarray reaches the threshold, Utilize insertion sort on the sub array
## Benchmarking Result
The Dual Pivot QuickSort loses efficacy as it starts to deal with larger datasets. But when it's working with smaller datasets, it can sort faster than QuickSort. To test this, In main.py, I tested the algorithm with an array size of 1,000 random integers 1000 times. I timed both the Dual Pivot Quicksort as well as the regukar QuickSort with the same random dataset, and the results were that the Dual Pivot QuickSort was faster anywhere from 50% to 90% of the time. However, when I repeated the test with an random array of 10,000 integers, QuickSort started to consitantly be faster than Dual Pivot QuickSort.
## Performance
In the previous section, the tests show that for smaller datasets, Dual Pivot QuickSort is more effective most of the time. And in larger datasets it starts to lose its efficacy. However by using a threshold for the insertion sort, you can optimize the efficancy even with larger datasets up to an extent.

The worst case time complexity is still O(n^2), the same as regular QuickSort, however, the Dual Pivot QuickSort reaches that scenario less often because of the Dual Pivots, allowing for better partitioning. It still maintains the average case of O(n*log(n)) as well, but the sorting is more efficent due to the insertion sort being used for smaller arrays. In practice, this can help reduce memory for the program. Due to this fact, it is better than QuickSort for many real world applications.
