def linear_search (arr, target):
    for i in range (len(arr)):
        if arr[i] == target:
            return i
    return "Not Found"
print(linear_search([1, 2, 7, 5, 65, 52, 46, 52, 45], 52))