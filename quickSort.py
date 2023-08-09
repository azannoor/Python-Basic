def quickSort(sequence):
    length=len(sequence)
    if length<=1:
        return sequence
    else:
        pivot=sequence.pop()


    greater=[]
    lower=[]
    for item in sequence:
        if item<pivot:
            lower.append(item)
        else :
            greater.append(item)
    return quickSort(lower) + [pivot] + quickSort(greater)

print(quickSort([5,6,3,12,1,9]))
