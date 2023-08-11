def sort(numbers):
    for i in range(5):
        minVal=i
        for j in range(minVal+1,6):
            if(numbers[j]<numbers[minVal]):
                minVal=j
        temp=numbers[i]
        numbers[i]=numbers[minVal]
        numbers[minVal]=temp
numbers=[6,5,4,3,2,1]
sort(numbers)
print(numbers)
