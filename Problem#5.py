# You are given an integer array[]. 
# You need to move all the 0s to the end, but keep the order of the other non-zero elements the same.

def movezero(arr):
    j = 0
    for i in range (len(arr)):
        if (arr[i]!=0):
            arr[i], arr[j] = arr[j], arr[i]
            j+= 1
    return arr

print(movezero([1, 23, 0, 45, 0, 65, 0]))