def dual_pivot_quick_sort(arr, left, right):
    if left < right:
        if right - left <= 10:
            insertion_sort(arr, left, right)
        else:
            pivot1, pivot2 = partition(arr, left, right)
            dual_pivot_quick_sort(arr, left, pivot1 - 1)
            dual_pivot_quick_sort(arr, pivot1 + 1, pivot2 - 1)
            dual_pivot_quick_sort(arr, pivot2 + 1, right)

def partition(arr, left, right):
    if arr[left] > arr[right]:
        arr[left], arr[right] = arr[right], arr[left]

    pivot1, pivot2 = arr[left], arr[right]
    i = left + 1
    j = left + 1
    k = right - 1

    while j <= k:
        if arr[j] < pivot1:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        elif arr[j] >= pivot1 and arr[j] <= pivot2:
            j += 1
        else:
            arr[j], arr[k] = arr[k], arr[j]
            k -= 1

    arr[left], arr[i - 1] = arr[i - 1], arr[left]
    arr[right], arr[k + 1] = arr[k + 1], arr[right]
    return i - 1, k + 1

def insertion_sort(arr, left, right):
    #print("Insertion")
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def hybrid_sort(arr, threshold):
    dual_pivot_quick_sort(arr, 0, len(arr) - 1)
    if len(arr) <= threshold:
        insertion_sort(arr, 0, len(arr) - 1)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)
