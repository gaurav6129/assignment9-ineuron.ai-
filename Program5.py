# Write a python script to print first N odd natural numbers in reverse order.
num=int(input("Enter the number:"))
i=num
while i>0:
    if i%2 != 0:
        print(i)
    i-=1