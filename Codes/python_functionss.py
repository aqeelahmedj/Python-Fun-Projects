#find average

# user enters numbers--> that go into some list ---> we look into list --- and take the average

'''
def avg(*args):
    times=5
    sum=0
    count=0

    for i in range(times):
        numbers=int(input(f"enter 5 numbers {i+1}: "))
        sum = sum+numbers
        count=count+1

    avg = print("Average: ", sum / count)
    return avg

avg()


def triangle(*args):
    n = 5
    for i in range(1, n+1):  #outer loop is for controlling row count
        for j in range(1, i+1):    #inner loop is for printing stars
            print("*", end='')
        print()

triangle()

*
**
***
****
*****

def square(*args):
    n=3
    for i in range(1, n+1):
        for j in range(1, n+1):
            print("*", end=' ')
        print()

square()

***
***
***



def triangle(*args):
    n = 5
    for i in range(1, n+1):  #outer loop is for controlling row count
        for j in range(1, i+1):    #inner loop is for printing stars
            print(j, end='')
        print()

triangle()

1
12
123
1234
12345

def triangle(*args):
    n = 5
    for i in range(1, n+1):  #outer loop is for controlling row count
        for j in range(1, n+1):    #inner loop is for printing stars
            print("*", end='')     #prints 5 stars
            n=j-1                 # now we need to produce 4 stars hence n should be 4..
        print()
triangle()

*****
****
***
**
*

def triangle(*args):
    n = 5
    for i in range(1, n+1):         #first loop for rows -- 5 rows
        for j in range(1, n):     # second loop for spaces -- 4 spaces n is 5 so n-1 ==4 makes sense...
            print(" ", end='')
        n=n-1
        for k in range(1, i+1):      # third loop for stars --- 1 star ---
            print("*", end='')

        print()

triangle()
    *
   **
  ***
 ****
*****

'''


#print table
# i=1
# n=3
#
# while i<=10:
#     print(i*n)
#     i=i+1
#
# print("number printed")
#

#printing a table of any number

# n=int(input("Enter any number: "))
#
#
# i=1
# while i<=10:
#     print(i*n)
#     i=i+1
#
# print("Table Printed !")


#traversing a list using loop

# listA=[1,4,9, 5, 6, 69, 303, 20, 2, 2]
#
# idx=0
#
# while idx<len(listA):
#     print(listA[idx])
#     idx=idx+1







