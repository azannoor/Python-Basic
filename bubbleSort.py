def bubble(numbers):
    for i in range(5):
        for j in range(0,len(numbers)-i-1):
            if(numbers[j]>numbers[j+1]):
                temp=numbers[j]
                numbers[j]=numbers[j+1]
                numbers[j+1]=temp



numbers=[6,5,4,3,2,1]
bubble(numbers)
print(numbers)