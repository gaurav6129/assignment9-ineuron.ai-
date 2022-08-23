# Write a python script to print squares of first N natural numbers.
num=int(input("Enter the number:"))
i=1
while i<=num:
    square=pow(i, 2)
    print(square)
    i+=1