a = int(input("Enter Marks : "))
b = int(input("Enter Marks : "))
c = int(input("Enter Marks : "))

sum = (a+b+c)/3

if (sum > 90): {
    print("Grade A")
}
elif (sum > 70): {
    print("Grade B")
}
elif (sum > 50): {
    print("Grade C")
}
else: {
    print("Grade D")
}

print(sum)