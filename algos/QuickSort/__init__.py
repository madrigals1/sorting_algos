def quick_sort(arr):
    less = []
    equal = []
    greater = []
 
    if len(arr) > 1:
        pivot = arr[0]
        
        for x in arr:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
    
        return quick_sort(less) + equal + quick_sort(greater)
 
    else:
        return arr
