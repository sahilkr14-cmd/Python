# You have been given a sorted array. 
# You have to remove the duplicate elements and shift the unique elements to the left side. 
# Return how many unique elements are there.

# #Do not use extra array.


def remove_dup(arr):
    i = 0
    for j in range (len(arr)):
        if arr[j]!= arr[i]:
            i+=1
            arr[i]=arr[j]
    return i+1


arr = [1,1,1,2,2,3,3,3,4,5,5]
k = remove_dup(arr)
print("Count of unique elements:", k)
print("Modified array:", arr[:k])