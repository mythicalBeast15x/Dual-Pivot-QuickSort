def partition(array, low, high):
    pivot = array[high]
    i = low
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i + 1


def insertion_sort(array, left, right):
    for i in range(left + 1, right + 1):
        key_item = array[i]
        j = i-1
        while j >= left and array[j] > key_item:
            array[j + i] = array[j]
            j -= 1
        array[j+1] = key_item

def intro_sort(array):
    max_depth = 2*len(array).bit_length()