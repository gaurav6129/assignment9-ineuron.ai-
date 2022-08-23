# Write a python script to print first N even natural number in reverse order.
num=int(input("Enter the number:"))
i=num
while i>0:
    if i%2 == 0:
        print(i)
    i-=1