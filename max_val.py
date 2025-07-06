def max(arr):
    max = arr[0]
    for val in arr:
        if val > max:
            max = val
    return max
print(max([12, 52, 65, 85, 45]))
