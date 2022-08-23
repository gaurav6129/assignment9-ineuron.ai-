# Write a python script to print squares of first N natural numbers.
num=int(input("Enter the number:"))
i=1
while i<=num:
    cube=pow(i, 3)
    print(cube)
    i+=1