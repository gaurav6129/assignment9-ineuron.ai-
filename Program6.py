# Write a python script to print first N even natural number.
num=int(input("Enter the number:"))
i=1
while i<=num:
    if i%2 == 0:
        print(i)
    i+=1