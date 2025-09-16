#binary search

def binarySearch(arr,target):
    arr.sort()
    low=0
    high = len(arr)-1
    # print("high",high)
    while low<high:
        midIndex=(low+high)//2
        # print("midIndex",midIndex)
        if arr[midIndex]==target:
            return True
        elif arr[midIndex]>target:
            high =midIndex-1
        elif arr[midIndex]<target:
            low =midIndex+1
    return False

def linearSearch(arr,target):
    for i in arr:
        if i==target:
            return True

    return False
a=[6,66,8,9,22,111]
print(binarySearch(a,6))
print(linearSearch(a,1411))