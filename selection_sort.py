toBeSorted = [12,7,4,9,3,10,47,23,84,2,6,5] #length of array = 12

def selectionSort(newArray):
    for i in range(len(newArray)):
        minNum = i
        for val in range(i+1, len(newArray)):
            if(newArray[minNum] > newArray[val]):
                minNum = val
        newArray[i] , newArray[minNum] = newArray[minNum] , newArray[i]
    return newArray


x = selectionSort(toBeSorted)
print(x)