''' Write a Python program that prints the numbers from 1 to 50.

For each number:

If the number is divisible by 3, print "Fizz" instead of the number.

If the number is divisible by 5, print "Buzz" instead of the number.

If the number is divisible by both 3 and 5, print "FizzBuzz" instead of the number.

Otherwise, just print the number itself. '

numbers = range(1, 50)
for n in numbers:
    if n % 3 ==0 and n % 5== 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5==0:
        print("Buzz")
    else:
        print(n)

'''

'''
Write a Python program that:

Asks the user to enter 10 numbers, one by one.

After all 10 numbers are entered:

Prints how many of them were even.

Prints how many of them were odd.
'''

even_count=0
odd_count = 0
numbers_count = 0
'''
for i in range(10):
    number =int(input("Enter any 10 numbers between 1 and 10:"))
    if number % 2 == 0:
            even_count=even_count+1
    elif number % 2 !=0:
            odd_count= odd_count+1
    numbers_count = numbers_count +1

print("You entered total even numbers:", even_count)
print("You entered total odd numbers :", odd_count)


#using while loop to only allow numbers less than 10 and those 10 should be added to variable

while numbers_count < 10:
    number = int(input(f"enter 10 numbers between 1 and 10:"))
    if number > 10:
        print(f"please enter a number less than 10")

    if number % 2 == 0:
        even_count = even_count +1
    else:
        odd_count = odd_count +1

    numbers_count = numbers_count +1
print("total even numbers entered: ", even_count)
print("total odd numbers entered :", odd_count)