# You are given 3 numbers A, B, and C.
# Determine whether the average of A and B is strictly greater than C or not?
# NOTE: Average of A and B is defined as (A+B)/2. For example, average of 5 and 9 is 7, average of 5 and 8 is 6.5.

# for i in range(int(input())):
a = int(input())
b = int(input())
c = int(input())
print("Yes" if a+b > 2*c else "No")