# # 1. Print “Hello, World!”
# print("Hello, World!")

# # 2. Variables and Data Types
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print(f"Your name is {name} and your age is {age}.")


# # 3. Arithmetic Operations
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# print(f"Sum: {num1 + num2}")
# print(f"Difference: {num1 - num2}")
# print(f"Product: {num1 * num2}")
# print(f"Division: {num1 / num2}")
# print(f"Modulus: {num1 % num2}")


# # 4. Convert Celsius to Fahrenheit
# celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print(f"Temperature in Fahrenheit: {fahrenheit}")


# # 5. Swap Two Variables
# a = input("Enter the first variable: ")
# b = input("Enter the second variable: ")
# print(f"Before swapping: a = {a}, b = {b}")
# a, b = b, a
# print(f"After swapping: a = {a}, b = {b}")


# # 6. Even or Odd
# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")


# # 7. Check Vowel or Consonant
# letter = input("Enter a letter: ").lower()
# if letter in 'aeiou':
#     print("The letter is a vowel.")
# else:
#     print("The letter is a consonant.")


# # 8. Square, Cube, and Square Root
# number = float(input("Enter a number: "))
# print(f"Square: {number ** 2}")
# print(f"Cube: {number ** 3}")
# print(f"Square Root: {number ** 0.5}")


# # 9. Area of Circle
# radius = float(input("Enter the radius of the circle: "))
# area = 3.14159 * radius ** 2
# print(f"Area of the circle: {area}")


# # 10. Simple Interest Calculation
# principal = float(input("Enter the principal amount: "))
# rate = float(input("Enter the rate of interest: "))
# time = float(input("Enter the time in years: "))
# simple_interest = (principal * rate * time) / 100
# print(f"Simple Interest: {simple_interest}")


# # 11. Largest of Three Numbers
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
# largest = max(num1, num2, num3)
# print(f"The largest number is {largest}")


# # 12. Leap Year Checker

# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")



# # 13 Multiplication Table
# num = int(input("Enter a positive integer: "))
# print(f"Multiplication Table for {num}")
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")


# # 14 Sum of N Natural Numbers
# n = int(input("Enter a positive integer: "))
# if n > 0:
#     total_sum = n * (n + 1) // 2
#     print(f"The sum of the first {n} natural numbers is {total_sum}")
# else:
#     print("Please enter a positive integer.")


# # 15 Factorial of a Number
# num = int(input("Enter a non-negative integer: "))
# if num >= 0:
#     factorial = 1
#     for i in range(1, num + 1):
#         factorial *= i
#     print(f"The factorial of {num} is {factorial}")
# else:
#     print("Please enter a non-negative integer.")

# # 16 Generate a random number. Prompt the user to guess until they get it right. Give hints (too high/too low).
# import random
# secret_number = random.randint(1, 100)
# guess = None
# print("Guess the number (between 1 and 100):")
# while guess != secret_number:
#     guess = int(input("Enter your guess: "))
#     if guess < secret_number:
#         print("Too low!")
#     elif guess > secret_number:
#         print("Too high!")
#     else:
#         print("Congratulations! You guessed the number.")


# # 17 Count Digits of a Number
# num = int(input("Enter a positive integer: "))
# if num > 0:
#     digit_count = len(str(num))
#     print(f"The number of digits in {num} is {digit_count}")
# else:
#     print("Please enter a positive integer.")


# # 18 Reverse a Number (While Loop)
# num = int(input("Enter a numbernumber :"))
# if num > 0:
#     reversed_num = 0
#     while num > 0:
#         digit = num % 10
#         reversed_num = reversed_num * 10 + digit
#         num //= 10
#     print(f"The reversed number is {reversed_num}")
# else:
#     print("Please enter a positive integer.")


# # 19 Sum of Even and Odd Numbers Separately
# n = int(input("Enter a number :"))
# if n > 0:
#     sum_even = sum(i for i in range(1, n + 1) if i % 2 == 0)
#     sum_odd = sum(i for i in range(1, n + 1) if i % 2 != 0)
#     print(f"Sum of even numbers from 1 to {n}: {sum_even}")
#     print(f"Sum of odd numbers from 1 to {n}: {sum_odd}")
# else:
#     print("Please enter a positive integer.")


# # 20 Palindrome Checker (Integer)
# num = int(input("Enter a positive integer :"))
# if num > 0:
#     original_num = num
#     reversed_num = 0
#     while num > 0:
#         digit = num % 10
#         reversed_num = reversed_num * 10 + digit
#         num //= 10
#     if original_num == reversed_num:
#         print(f"{original_num} is a palindrome.")
#     else:
#         print(f"{original_num} is not a palindrome.")
# else:
#     print("Please enter a positive integer.")


# # 21 Simple Calculator
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return "Division by zero is undefined."

# # User Input
# print("Select operation: 1. Add 2. Subtract 3. Multiply 4. Divide")
# choice = input("Enter choice (1/2/3/4) :")

# num1 = float(input("Enter the first number :"))
# num2 = float(input("Enter the second number :"))

# if choice == '1':
#     print(f"Result: {add(num1, num2)}")
# elif choice == '2':
#     print(f"Result: {subtract(num1, num2)}")
# elif choice == '3':
#     print(f"Result: {multiply(num1, num2)}")
# elif choice == '4':
#     print(f"Result: {divide(num1, num2)}")
# else:
#     print("Invalid choice.")


# # 22 Power Function
# def power(base, exponent):
#     result = 1
#     for _ in range(abs(exponent)):
#         result *= base
#     return result if exponent >= 0 else 1 / result

# base = float(input("Enter the base :"))
# exponent = int(input("Enter the exponent :"))
# print(f"{base} to the power of {exponent} is {power(base, exponent)}")


# # 23 Count Characters in a String
# def count_characters(string):
#     return len(string)

# # User Input
# user_string = input("Enter a string :")
# print(f"The number of characters in the string is {count_characters(user_string)}")


# # 24 Check Prime
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# # User Input
# num = int(input("Enter a number to check if it's prime :"))
# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")

# # 25
# def fibonacci(x):
#     y=[0,1]
#     for i in range(2,x):
#         z=y[-1]+y[-2]
#         y.append(z)
#     return y
# x=int(input("Enter the number"))
# print(fibonacci(x))


# # 26
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# x = int(input("Enter the first number :"))
# y = int(input("Enter the second numbern :"))
# print(f"The GCD of",x,"and",y,"is:", gcd(x, y))
        

# # 27
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# def lcm(a,b):
#     z=abs(a*b)/(gcd(a,b))
#     return z

# x = int(input("Enter the first number :"))
# y = int(input("Enter the second number :"))
# print(f"The LCM of",x,"and",y,"is:", gcd(x, y))


# # 28
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# x = int(input("Enter the number :"))
# print("Factorial of",x,"is", factorial(x))


# # 29
# def tower_of_hanoi(n, a, b, c):
#     if n == 1:
#         print("Move disk 1 from",a,"to",b)
#         return
    
#     tower_of_hanoi(n - 1, a, c, b)
    
#     print("Move disk",n,"from",a,"to",b)
    
#     tower_of_hanoi(n - 1, c, b, a)

# n = int(input("Enter the number of disks: "))
# tower_of_hanoi(n, 'A', 'C', 'B')


# 30
# def count_occurrences(lst, x):
#     count = 0
    
#     for i in lst:
#         if i == x:
#             count += 1
#     return count
# lst = [1, 2, 3, 4, 2, 2, 5]
# x = int(input("Enter the number :"))
# print("The number",x,"appears",count_occurrences(lst, x),"times in the list")


# # 31
# my_list=[10,20]
# print("Initial list",my_list)

# my_list.append(30)
# my_list.append(40)
# print("After appending 30 and 40",my_list)

# my_list.insert(1, 15) 
# print("After inserting 15 at index 1:", my_list)

# my_list.remove(20)  
# print("After removing 20:", my_list)

# popped_element = my_list.pop()  
# print(f"After popping the last element", (popped_element),":", my_list)

# print("Final list:", my_list)


# # 32
# x=int(input("Enter the number of elements you want in your list"))
# numbers=[]
# for i in range(0,x):
#     z=input("Enter element for the list")
#     numbers.append(z)
# print("Your List",numbers)

# max_value = max(numbers)
# min_value = min(numbers)

# print(f"Maximum value: {max_value}")
# print(f"Minimum value: {min_value}")


# # 33
# x=int(input("Enter the number of elements you want in your list"))
# numbers=[]
# for i in range(0,x):
#     z=input("Enter element for the list")
#     numbers.append(z)
# print("Your List",numbers)

# numbers.sort()  
# second_largest = numbers[-2]  

# print(f"The second largest element is: {second_largest}")


# # 34
# x=int(input("Enter the number of elements you want in your list"))
# numbers=[]
# for i in range(0,x):
#     z=input("Enter element for the list")
#     numbers.append(z)
# print("Your List",numbers)
# z=list(map(float,numbers))

# total = sum(z)
# average = total / len(z)

# # Print the results
# print(f"Sum: {total}")
# print(f"Average: {average}")


# # 35
# x=int(input("Enter the number of elements you want in your list"))
# numbers=[]
# for i in range(0,x):
#     z=input("Enter element for the list")
#     numbers.append(z)
# print("Your List",numbers)
# z=list(map(float,numbers))
# positive_count = 0
# negative_count = 0
# zero_count = 0

# for num in z:
#     if num > 0:
#         positive_count += 1
#     elif num < 0:
#         negative_count += 1
#     else:
#         zero_count += 1

# print(f"Positive numbers: {positive_count}")
# print(f"Negative numbers: {negative_count}")
# print(f"Zeros: {zero_count}")


# # 36
# x=int(input("Enter the number of elements you want in your list"))
# numbers=[]
# for i in range(0,x):
#     z=input("Enter element for the list")
#     numbers.append(z)
# print("Your List",numbers)

# unique_numbers = list(set(numbers))

# # Print the result
# print("List with duplicates removed:", unique_numbers)



# # 37 Input two lists from the user and concatenate them.
# list1 = input("Enter the first list: ")
# list2 = input("Enter the second list: ")
# list3 = list1 + list2
# print("Concatenated list:", list3)


# # 38 Write a function to reverse a given list in place.
# def reverse_list(lst):
#     lst.reverse()
# my_list = [1, 2, 3, 4, 5]
# reverse_list(my_list)
# print("Reversed list:", my_list)


# # 39 Given two lists, find the common elements and store them in a new list.
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# common_elements = list(set(list1) & set(list2))
# print("Common elements:", common_elements)


# # 40 Given two lists of equal length, create a third list that stores the element-wise sum.
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# sum_list = [x + y for x, y in zip(list1, list2)]
# print("Sum of elements:", sum_list)

# # 41 Create a tuple of strings. Prompt the user for an index and print the element at that index.
# tuple1 = ('Apple', 'Bannana', 'Pineapple', 'Pomogranate', 'Pear', 'Potato', 'Tomato')
# index = int(input("Enter the index: "))
# print("Element at the given index:", tuple1[index])

# # 42 Convert a user-defined tuple to a list, modify it, and convert it back to a tuple.
# tuple1 = input("Enter a tuple: ")
# list1 = list(tuple1)
# print('Modified list:', list1)
# list1[0] = "Chaitanya"
# tuple1 = tuple(list1)
# print("Modified tuple:", tuple1)


# # 43 Prompt the user for an element and check if it exists in the tuple.
# tuple1 = ('Chaitanya', 'Sourabh', 'Vinayak', 'shashank', 'Yash', 'Soham', 'Ronak', 'Sujal', 'Rohan', 'Tanishq')
# element = input("Enter an element: ")   
# if element in tuple1:
#     print("Element exists in the tuple.")
# else:
#     print("Element does not exist in the tuple.")


# # 44 Prompt the user for a string and build a dictionary that counts how many times each word appears.

# string = input("Enter a string: ")
# words = string.split()
# word_count = {}

# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1

# print("Word count:", word_count)
# text = input("Enter a string: ")
# words = text.split()
# word_count = {}
# for word in words:
#     word_count[word] = word_count.get(word, 0) + 1
# print("Word count:", word_count)


# # 45 Create a dictionary with student names as keys and their grades as values. Prompt the user for a name and display the grade.
# student_grades = {
#     "Apple": "A",
#     "Bannan": "B",
#     "Cndy": "C",
#     "Diwali": "D",
#     "Ell": "E",
#     "Fish": "F",
#     "Gon": "G",
#     "Hii": "H",
#     "IceCream": "I",
#     "Josh": "J"
# }
# name = input("Enter a student name: ")

# if name in student_grades:
#     print(f"The grade of {name} is {student_grades[name]}")
# else:
#     print("Student not found in the dictionary.")


# # 46 Create a dictionary and then print just its keys and just its values separately.
# my_dict = {
#     "Apple": "A",
#     "Bannan": "B",
#     "Cndy": "C",
#     "Diwali": "D",
#     "Ell": "E",
#     "Fish": "F",
#     "Gon": "G",
#     "Hii": "H",
#     "IceCream": "I",
#     "Josh": "J"
# }
# print("Keys:", my_dict.keys())
# print("Values:", my_dict.values())


# # 47 Given two dictionaries, merge them into a new dictionary.

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}

# merged_dict = {**dict1, **dict2}

# print("Merged dictionary:", merged_dict)


# # 48 Given a dictionary {key: value}, swap keys and values if all values are unique (produce {value: key}).
# my_dict = {
#     "Chaitanya": "A",
#     "Sourabh": "B",
#     "Vinayak": "C",
#     "shashank": "D",
#     "Yash": "E",
#     "Soham": "F",
#     "Ronak": "G",
#     "Sujal": "H",
#     "Rohan": "I",
#     "Tanishq": "J"
# }
# swapped_dict = {value: key for key, value in my_dict.items() if len(my_dict) == len(set(my_dict.values()))}
# print("Swapped dictionary:", swapped_dict)


# # 49BSet Operations
# list1 = input("Enter the first list of numbers (separated by space): ").split()
# list2 = input("Enter the second list of numbers (separated by space): ").split()

# set1 = set(list1)
# set2 = set(list2)

# union = set1.union(set2)
# intersection = set1.intersection(set2)
# difference = set1.difference(set2)

# print("Union:", union)
# print("Intersection:", intersection)
# print("Difference (set1 - set2):", difference)


# # 50 Set Membership Testing
# names_set = {"Alice", "Bob", "Charlie", "Diana"}

# name = input("Enter a name to check: ")

# if name in names_set:
#     print(f"{name} is in the set.")
# else:
#     print(f"{name} is not in the set.")


# # 51 Reverse a String
# user_string = input("Enter a string: ")

# reversed_string = user_string[::-1]

# print("Reversed String:", reversed_string)


# # 52 Palindrome String Checker
# user_string = input("Enter a string: ")

# if user_string == user_string[::-1]:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")


# # 53 Count Vowels in a String
# user_string = input("Enter a string: ")

# vowels = "aeiouAEIOU"

# vowel_count = 0

# for char in user_string:
#     if char in vowels:
#         vowel_count += 1

# print("Number of vowels:", vowel_count)


# # 54 Check Anagram
# str1 = input("Enter the first string: ")
# str2 = input("Enter the second string: ")

# if sorted(str1) == sorted(str2):
#     print("The strings are anagrams.")
# else:
#     print("The strings are not anagrams.")


# # 55 Remove Spaces
# user_string = input("Enter a string: ")

# no_spaces_string = user_string.replace(" ", "")
# print("String without spaces:", no_spaces_string)


# # 56 Longest Word in a Sentence
# sentence = input("Enter a sentence: ")

# words = sentence.split()

# longest_word = max(words, key=len)

# print("The longest word is:", longest_word)

# #key=len argument tells Python to compare the words based on their length.


# # 57 String Case Conversion
# user_string = input("Enter a string: ")

# upper_case = user_string.upper()
# lower_case = user_string.lower()
# title_case = user_string.title()

# print("Upper case:", upper_case)
# print("Lower case:", lower_case)
# print("Title case:", title_case)


# # 58 Capitalize Every Word
# user_string = input("Enter a string: ")

# capitalized_string = user_string.title()
# print("String with capitalized words:", capitalized_string)


# # 59 Count Special Characters
# user_string = input("Enter a string: ")

# special_chars = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?"

# special_char_count = 0
# for char in user_string:
#     if char in special_chars:
#         special_char_count += 1
# print("Number of special characters:", special_char_count)


# # 60 Character Frequency in String
# user_string = input("Enter a string: ")

# char_count = {}

# for char in user_string:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
# print("Character frequency:", char_count)



# # ''' 61 ARMSTRONG NUMBER : An Armstrong number is a number where the sum of its digits raised to the power of the number of digits equals the number itself.
# # # Example: 153
# #             (number of digits = 3, hence the power of all digits will be 3)
# #             = 1^3 + 5^3 + 3^3
# #             = 1 + 125 + 27
# #             = 153
# # '''

# def is_armstrong(number):
#     digits = str(number)
#     power = len(digits)
#     total = 0
#     for digit in digits:
#         total += int(digit) ** power
#     if total == number:
#         return True
#     else:
#         return False

# num = int(input("Enter a number: "))
# if is_armstrong(num):
#     print(f"{num} is an Armstrong number.")
# else:
#     print(f"{num} is not an Armstrong number.")


# # '''
# # 62 Strong NUmber : A Strong Number is a special number whose sum of the factorials of its digits is equal to the number itself.
# # Example : 145
# #         = 1! + 4! + 5!
# #         = 1 + 24 + 120
# #         = 145

# # '''


# from math import factorial

# def is_strong(number):
#     digits = str(number)
#     total = 0
#     for digit in digits:
#         total += factorial(int(digit))
#     if total == number:
#         return True
#     else:
#         return False

# num = int(input("Enter a number: "))
# if is_strong(num):
#     print(f"{num} is a Strong number.")
# else:
#     print(f"{num} is not a Strong number.")


# # ''' 63 PERFECT NUMBER : A Perfect Number is a positive integer that is equal to the sum of its proper divisors (excluding itself).
# # Example : • 6                                    • 28
# #         (proper divisors - 1,2,3)                 (proper divisors : 1,2,4,7,14)
# #         = 1 + 2 + 3                                = 1 + 2 + 4 + 7 + 14
# #         = 6                                        = 28


# # '''


# def is_perfect(number):
#     total = 0
#     for i in range(1, number):
#         if number % i == 0:
#             total += i
#     if total == number:
#         return True
#     else:
#         return False

# num = int(input("Enter a number: "))
# if is_perfect(num):
#     print(f"{num} is a Perfect number.")
# else:
#     print(f"{num} is not a Perfect number.")


# # 64 Sum of Digits

# def sum_of_digits(number):
#     total = 0
#     for digit in str(number):  #used constructor for iteration
#         total += int(digit)    #used constructor for iteration
#     return total

# num = int(input("Enter a number: "))
# print(f"Sum of digits of {num} is: {sum_of_digits(num)}")


# # 65 Convert binary to decimal

# def binary_to_decimal(binary_str):
#     decimal = 0
#     power = len(binary_str) - 1   # (-1) int the end gives the index of the most significant bit (the leftmost bit).
#     for digit in binary_str:
#         decimal += int(digit) * (2 ** power)
#         power -= 1
#     return decimal

# binary = input("Enter a binary number: ")
# print(f"The decimal equivalent of {binary} is: {binary_to_decimal(binary)}")


# # 66 Decimal to binary

# def decimal_to_binary(decimal_number):
#     binary = ""
#     '''
#         The binary variable is initially set to an empty string ("") because this is    
#         where the binary digits (either 0 or 1) will be accumulated. 
#         Each new digit will be added to the front of this string as the conversion process proceeds.
#     '''
#     while decimal_number > 0:
#         binary = str(decimal_number % 2) + binary
#         decimal_number //= 2
#     return binary

# decimal = int(input("Enter a decimal number: "))
# print(f"The binary equivalent of {decimal} is: {decimal_to_binary(decimal)}")


# # 67 Prime FActor : Factors of a number which are also prime nos
# # '''
# # Exmple : 30
# #         (Factors of 30 are 1, 2, 3, 5, 6, 10)
# #         Prime factors are 1, 2, 3, 5   (since 6 and 10 are not prime nos)
# # '''

# def prime_factors(number):
#     factors = []
#     divisor = 2
#     while number > 1:
#         if number % divisor == 0:
#             factors.append(divisor)
#             number //= divisor
#         else:
#             divisor += 1
#     return factors

# num = int(input("Enter a number: "))
# print(f"Prime factors of {num} are: {prime_factors(num)}")


# # 68 Number to Words

# def number_to_words(number):
#     words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
#     result = ""
#     for digit in str(number):
#         result += words[int(digit)] + " "
#     return result.strip()

# num = int(input("Enter a number: "))
# print(f"{num} in words is: {number_to_words(num)}")


# # 69 
# from math import gcd

# def lcm(a, b):
#     return (a * b) // gcd(a, b)

# def lcm_of_range(n):
#     result = 1
#     for i in range(1, n + 1):
#         result = lcm(result, i)
#     return result

# n = int(input("Enter the range n: "))
# print(f"LCM of numbers from 1 to {n} is: {lcm_of_range(n)}")


# # 70 sieve_of_eratosthenes : algorithm used to find all prime numbers up to a specified integer n

# def sieve_of_eratosthenes(n):
#     primes = [True] * (n + 1)  # Assume all numbers are prime initially
#     primes[0] = primes[1] = False  # 0 and 1 are not prime numbers

#     for i in range(2, n + 1):  # Check numbers from 2 to n
#         if primes[i]:  # If i is prime
#             # Mark all multiples of i as not prime
#             for j in range(i * 2, n + 1, i):
#                 primes[j] = False

#     # Collect and return all numbers that are still marked as prime
#     return [i for i in range(2, n + 1) if primes[i]]

# # Get input from the user
# n = int(input("Find all primes up to: "))

# # Display the result
# print(f"Prime numbers up to {n}: {sieve_of_eratosthenes(n)}")


# # 70sieve_of_eratosthenes : algorithm used to find all prime numbers up to a specified integer n
# def sieve_of_eratosthenes(n):
#     primes = [True] * (n + 1)  # Assume all numbers are prime initially
#     primes[0] = primes[1] = False  # 0 and 1 are not prime numbers

#     for i in range(2, n + 1):  # Check numbers from 2 to n
#         if primes[i]:  # If i is prime
#             # Mark all multiples of i as not prime
#             for j in range(i * 2, n + 1, i):
#                 primes[j] = False

#     # Collect and return all numbers that are still marked as prime
#     return [i for i in range(2, n + 1) if primes[i]]

# # Get input from the user
# n = int(input("Find all primes up to: "))

# # Display the result
# print(f"Prime numbers up to {n}: {sieve_of_eratosthenes(n)}")



# # 71 write in a file

# text = input("Enter a string to write to the file: ")  # Prompt user for input
# file = open("output.txt", "w")  # Open the file in write mode
# file.write(text)  # Write the input text to the file
# file.close()  # Close the file after writing
# print("Text has been written to output.txt")


# # 72
# try:
#     file = open("output.txt", "r")  # Open the file in read mode
#     content = file.read()  # Read the content of the file
#     file.close()  # Close the file after reading
#     print("Content of output.txt:")
#     print(content)  # Print the content
# except FileNotFoundError:
#     print("File 'output.txt' not found.")


# '''
# 85.	**Class** Car **and Inheritance**
# •	Create a base class Car with attributes: make, model, year. 
#     Create a derived class ElectricCar with an additional battery_size attribute.
# '''
# class car:                        # Created a normal class car with variables brand, model and year
#     def __init__(self):            
#         self.brand = "McLaren"
#         self.model = "W1"
#         self.year = 2024

# class electricCar(car):           # Created derived class electricCar with additional attribute battery size
#     def __init__(self):
#         self.brand = "Tesla"
#         self.model = "Model Y"
#         self.year = 2019
#         self.battery_size = "75 kWh"

# GasCar = car()                    # Object of car class
# print(GasCar.brand)               # printing the values
# print(GasCar.model)
# print(GasCar.year)

# print()

# E_Car = electricCar()            # Object of electricCar class
# print(E_Car.brand)               # printing the values
# print(E_Car.model)
# print(E_Car.year)
# print(E_Car.battery_size)


# '''
# 86.	**Class** ComplexNumber
# •	Implement a class that represents a complex number with real and imaginary parts. 
#     Overload addition and subtraction operators (if you want to practice operator overloading in Python).
# '''
# class complex:
#     def __init__(self,real,imag):
#         self.realPart= real
#         self.imaginaryPart = imag
#     def __add__(self,number2):                  # Operator Overloading to add two objects
#         addition =f"{self.realPart + number2.realPart} + {self.imaginaryPart + number2.imaginaryPart}i"     #Adding real and imaginary parts of number1 and number2
#         return addition
#     def __sub__(self,number2):                  # Operator Overloading to subtract two objects
#         subtraction =f"{self.realPart - number2.realPart} + {self.imaginaryPart - number2.imaginaryPart}i"  #Subtracting real and imaginary parts of number1 and number2
#         return subtraction

# number1 = complex(5,3)          # Defined object--> number1
# number2 = complex(3,2)          # Defined object--> number2

# print(number1 + number2)        # call the add function--> overloaded operator to add two objects
# print(number1 - number2)        # call the sub function--> overloaded operator to subtract two objects

        

# '''
# 87.	**Class** Point
# •	Represent a point in 2D space. 
#     Add methods to set coordinates and calculate distance from another Point object.
# '''
# class co_ordinates:
#     def __init__(self,x,y):                 # Take input for x and y coordinate
#         self.x_coordinate = x
#         self.y_coordinate = y
#     def distance(self,obj2):                # Apply the distance formula
#         dist = (((self.x_coordinate) - (point2.x_coordinate))**2 + ((self.y_coordinate)- (point2.y_coordinate))**2)**0.5
#         return dist

# point1 = co_ordinates(4,3)                  # point1 object created
# point2 = co_ordinates(0,0)                  # point2 object created

# print(point1.distance(point2))      # Calling the distance function with point2 as the parameter


# '''
# 88.	**Classmethod and Staticmethod**
# •	Create a class with a regular instance method, 
#     a class method, and a static method. Demonstrate their differences.
# '''
# class ClassMethods:
#     count = 0                       # Class-level attribute

#     def __init__(self, value):
#         self.value = value          # Instance attribute
#         ClassMethods.count += 1     # Increment when an object is created

#     # Instance method: Works with instance data
#     def show_value(self):
#         return self.value           # Returns number given when object is defined

#     # Class method: Works with class-level data
#     @classmethod
#     def show_count(cls):
#         return cls.count            # Shows the count i.e. number of objects created

#     # Static method: Independent of both class and instance
#     @staticmethod
#     def greet():                    # Object independent method- doesnt do automatic work when obejct is created
#         return "Hello, this is a static method!"


# # Creating instances
# example1 = ClassMethods(10)
# example2 = ClassMethods(20)

# # Calling the instance method
# print(example1.show_value())  # Output: 10
# print(example2.show_value())  # Output: 20

# # Calling the class method
# print(ClassMethods.show_count())  # Output: 2

# # Calling the static method
# print(ClassMethods.greet())  # Output: Hello, this is a static method!


# '''
# 89.	**Property Decorators**
# •	Create a class that uses @property to control getting and setting of a private attribute.
# '''
# class Person:
#     def __init__(self, name):
#         self._name = name  # Private attribute

#     # Getter for 'name'
#     @property                           # The @property decorator is used for the getter method - when you want to access a certain method like an attribute
#     def name(self):
#         return self._name

#     # Setter for 'name'
#     @name.setter                        # @name.setter is the decorator for the setter method which is used when you want to assign value to a var
#     def name(self, value):
#         if not value:
#             print("Name cannot be empty!")
#         else:
#             self._name = value

# # Usage:
# person = Person("Alice")                # Object i.e. person created with name Alice

# # Accessing and setting name
# print(person.name)  # Output: Alice

# person.name = "Bob"    # Changing name to Bob
# print(person.name)     # Printing : Bob

# person.name=""         # Chaging name to null
# print(person.name)     # Printing : Name cannot be empty! - since we gave the if-else condition


# '''
# 90.	**Class** Employee **with Inheritance**
# •	Base class Employee (name, ID, salary) and 
#     child class Manager (with additional attributes). Override a method in the subclass.
# '''
# class Employee:
#     def __init__(self, name, emp_id, salary):
#         self.name = name        # Employee's name
#         self.emp_id = emp_id    # Employee's ID
#         self.salary = salary    # Employee's salary

#     def show_details(self):     # Show details function 
#         return f"Name: {self.name}, ID: {self.emp_id}, Salary: ${self.salary}"

# class Manager(Employee):
#     def __init__(self, name, emp_id, salary, department, team_size):
#         # Call the parent class's constructor to initialize name, ID, salary
#         super().__init__(name, emp_id, salary)
#         self.department = department    # Manager's department
#         self.team_size = team_size      # Number of people in the manager's team

#     # Override the show_details method to include department and team size
#     def show_details(self):
#         base_details = super().show_details()  # Call the base class method
#         return f"{base_details}, Department: {self.department}, Team Size: {self.team_size}"


# employee = Employee("Soham", 101, 50000)                 # Base class object
# manager = Manager("Yash", 102, 80000, "IT", 10)        # Derived class object

# print(employee.show_details())              # Shows details of employee using method from base class

# print(manager.show_details())               # Shows details of manager using the overrriden method from derived class



# '''
# 91.	**Bubble Sort**
# •	Implement bubble sort to sort a list of integers.
# '''
# myList = [3, 7, 4, 1, 9, 2, 8, 6, 0, 5]     
# for j in range(len(myList) - 1):                # Outer loop to control how many times we pass through the list
#     for i in range(0, len(myList) - 1 - j):     # Inner loop to go through the list and compare adjacent elements
#         if myList[i] > myList[i + 1]:  
#             myList[i], myList[i + 1] = myList[i + 1], myList[i]  
# print(myList)

        
        
# '''
# 92.	**Insertion Sort**
# •	Implement insertion sort to sort a list of integers.
# '''
# arr = [12, 11, 13, 5, 6]            # Define the array
# for i in range(1, len(arr)):        # Traverse through 1 to len(arr)
#     key = arr[i]                    # Define the key
#     j = i-1                         # Define the index       
#     while j >= 0 and key < arr[j]:  # Traverse through the array
#         arr[j+1] = arr[j]           # Swap the elements
#         j -= 1                      # Decrement the index     
#     arr[j+1] = key                  # Swap the elements   
# print(arr)    


# '''
# 93.	**Selection Sort**
# •	Implement selection sort to sort a list of integers.
# ''' 
# arr = [64, 25, 12, 22, 11]              # Define the array
# for i in range(len(arr)):               # Traverse through all array elements
#     min_index = i                       # Find the minimum element in remaining unsorted array
#     for j in range(i+1, len(arr)):      # Swap the found minimum element with the first element
#         if arr[min_index] > arr[j]:     
#             min_index = j               
#     arr[i], arr[min_index] = arr[min_index], arr[i]     
# print(arr)


# '''
# 94.	**Merge Sort**
# •	Implement merge sort to sort a list of integers.
# '''
# def merge_sort(arr):
#     if len(arr) > 1:                # If the length of the array is greater than 1
#         mid = len(arr) // 2         # Find the middle of the array
#         L = arr[:mid]               # Divide the array elements into 2 halves - Left Half
#         R = arr[mid:]               # Divide the array elements into 2 halves - Right Half
#         merge_sort(L)               # Recursively sort the Left Half
#         merge_sort(R)               # Recursively sort the Right Half
#         i = j = k = 0               # Initialize the index variables
#         while i < len(L) and j < len(R):        # Copy data to temp arrays L[] and R[]
#             if L[i] < R[j]:                     # Compare the elements of L[] and R[]
#                 arr[k] = L[i]                   # If L[i] is smaller, copy L[i] to arr[k]
#                 i += 1                          # Increment the index of L[]
#             else:                               
#                 arr[k] = R[j]                   # If R[j] is smaller, copy R[j] to arr[k]
#                 j += 1                          # Increment the index of R[]
#             k += 1                          # Increment the index of arr[]            
#         while i < len(L):           # Check if any element was left
#             arr[k] = L[i]           # Copy the remaining elements of L[] to arr[]
#             i += 1                  
#             k += 1
#         while j < len(R):           # Check if any element was left
#             arr[k] = R[j]           # Copy the remaining elements of R[] to arr[]
#             j += 1
#             k += 1
#     return arr

# arr = [4,8,1,3,5,9,2,6,7]           # Define the array
# print(merge_sort(arr))              # Print the sorted array


# '''
# 95.	**Quick Sort**
# •	Implement quick sort to sort a list of integers.
# '''
# def quick_sort(arr):
#     if len(arr) <= 1:                       # If the length of the array is less than or equal to 1
#         return arr                          # Return the array
#     else:                                   # Otherwise
#         pivot = arr[-1]                     # Define the pivot element
#         less = [i for i in arr[:-1] if i < pivot]     # Define the elements less than the pivot
#         print(less)
#         greater = [i for i in arr[:-1] if i >= pivot] # Define the elements greater than or equal to the pivot
#         print(greater)
#         return quick_sort(less) + [pivot] + quick_sort(greater)   # Return the sorted array
# arr = [4,8,1,3,5,9,2,6,7]           # Define the array
# print(quick_sort(arr))              # Print the sorted array


# '''
# 96.	**Binary Search**
# •	Implement binary search on a sorted list to find a given element.
# '''
# #without function
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]      # Define the array
# x = int(input("Enter the number to be searched : "))    # Define the element to be searched
# beg = 0                                 # Define the lower bound
# end = len(arr) - 1                     # Define the upper bound
# while beg <= end:                      # While the lower bound is less than or equal to the upper bound
#     mid = (beg + end) // 2             # Define the middle element
#     if arr[mid] < x:                    # If the middle element is less than the element to be searched
#         beg = mid + 1                   # Update the lower bound
#     elif arr[mid] > x:                  # If the middle element is greater than the element to be searched
#         end = mid - 1                  # Update the upper bound
#     else:                               # Otherwise
#         print(f"At Position {mid+1}")                      # Print the position of the element
#         break                           # Break the loop
# else:
#     print(-1)                           # Print -1 if the element is not found



# # 97.	**Linear Search**

# # •	Implement linear search to find an element in a list.

# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1   

# # Test the function
# arr = [1, 2, 3, 4, 5]
# target = 3
# print(linear_search(arr, target))  # Output: 2


# # 98.	**Knuth Shuffle (Fisher–Yates Shuffle)**
# # •	Given a list, shuffle its elements in place uniformly.

# import random

# def knuth_shuffle(arr):
#     n = len(arr)
#     for i in range(n):
#         j = random.randint(i, n - 1)
#         arr[i], arr[j] = arr[j], arr[i]

# # Test the function
# arr = [1, 2, 3, 4, 5]
# knuth_shuffle(arr)
# print(arr)  # Output: Random shuffle of the input list


# # 99.	**Matrix Addition**

# # •	Prompt the user for two matrices (2D lists) of the same dimensions and compute their sum.

# def input_matrix(rows, cols):
#     print(f"Enter the elements of a {rows}x{cols} matrix row by row:")
#     matrix = []
#     for i in range(rows):
#         row = list(map(int, input(f"Row {i + 1}: ").split()))
#         while len(row) != cols:
#             print(f"Row {i + 1} must have {cols} elements. Try again.")
#             row = list(map(int, input(f"Row {i + 1}: ").split()))
#         matrix.append(row)
#     return matrix

# def add_matrices(A, B):
#     # Dimensions of matrices
#     m = len(A)
#     n = len(A[0])
    
#     # Resultant matrix of size m x n
#     result = [[0] * n for _ in range(m)]
    
#     # Add matrices
#     for i in range(m):
#         for j in range(n):
#             result[i][j] = A[i][j] + B[i][j]
#     return result

# # Input dimensions for matrix A
# rows_A = int(input("Enter the number of rows in Matrix A: "))
# cols_A = int(input("Enter the number of columns in Matrix A: "))

# # Input dimensions for matrix B
# rows_B = int(input("Enter the number of rows in Matrix B: "))
# cols_B = int(input("Enter the number of columns in Matrix B: "))
# if rows_A != rows_B or cols_A != cols_B:
#     print("Matrix addition not possible. Matrices must have the same dimensions.")

# else:
#     # Input matrices
#     A = input_matrix(rows_A, cols_A)
#     B = input_matrix(rows_B, cols_B)
    
#     # Add matrices
#     result = add_matrices(A, B)
    
#     # Display result
#     print("\nResultant Matrix:")
#     for row in result:
#         print(row)


# # 100.	**Matrix Multiplication**


# def input_matrix(rows, cols):
#     print(f"Enter the elements of a {rows}x{cols} matrix row by row:")
#     matrix = []
#     for i in range(rows):
#         row = list(map(int, input(f"Row {i + 1}: ").split()))
#         while len(row) != cols:
#             print(f"Row {i + 1} must have {cols} elements. Try again.")
#             row = list(map(int, input(f"Row {i + 1}: ").split()))
#         matrix.append(row)
#     return matrix

# def multiply_matrices(A, B):
#     # Dimensions of matrices
#     m = len(A)
#     n = len(A[0])
#     p = len(B[0])
    
#     # Resultant matrix of size m x p
#     result = [[0] * p for _ in range(m)]
    
#     # Multiply matrices
#     for i in range(m):
#         for j in range(p):
#             for k in range(n):
#                 result[i][j] += A[i][k] * B[k][j]
#     return result

# # Input dimensions for matrix A
# rows_A = int(input("Enter the number of rows in Matrix A: "))
# cols_A = int(input("Enter the number of columns in Matrix A: "))

# # Input dimensions for matrix B
# rows_B = int(input("Enter the number of rows in Matrix B: "))
# cols_B = int(input("Enter the number of columns in Matrix B: "))

# # Check compatibility for multiplication
# if cols_A != rows_B:
#     print("Matrix multiplication not possible. Number of columns in Matrix A must equal the number of rows in Matrix B.")
# else:
#     # Input matrices
#     A = input_matrix(rows_A, cols_A)
#     B = input_matrix(rows_B, cols_B)
    
#     # Multiply matrices
#     result = multiply_matrices(A, B)
    
#     # Display result
#     print("\nResultant Matrix:")
#     for row in result:
#         print(row)


# # 101.	**Transposition of a Matrix**

# # •	Compute the transpose of a user-provided matrix.


# def transpose_matrix(matrix):
#     # Transpose using list comprehension
#     transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
#     return transpose

# # Test the function
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# transposed = transpose_matrix(matrix)
# print("Original Matrix:")
# for row in matrix:
#     print(row)

# print("\nTransposed Matrix:")
# for row in transposed:
#     print(row)


# # 102.	**Check if a Matrix is Symmetric**

# # •	Determine if a given square matrix is symmetric (equal to its transpose).

# def is_symmetric(matrix):
#     # Check if the matrix is square
#     rows = len(matrix)
#     cols = len(matrix[0])
#     if rows != cols:
#         return False

#     # Check symmetry
#     for i in range(rows):
#         for j in range(cols):
#             if matrix[i][j] != matrix[j][i]:
#                 return False
#     return True

# # Test the function
# matrix = [
#     [1, 2, 3],
#     [2, 5, 6],
#     [3, 6, 9]
# ]

# print("The matrix is symmetric:", is_symmetric(matrix))


# # 103.	**Longest Common Substring**

# # •	Find the longest common substring between two given strings.

# def lcs(s1, s2):
#     m, n = len(s1), len(s2)
#     dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
#     max_len = 0
#     end_index = 0
    
#     for i in range(1, m+1):
#         for j in range(1, n+1):
#             if s1[i-1] == s2[j-1]:
#                 dp[i][j] = 1 + dp[i-1][j-1]
#                 if dp[i][j] > max_len:
#                     max_len = dp[i][j]
#                     end_index = i
#             else:
#                 dp[i][j] = 0
    
#     return s1[end_index-max_len:end_index]

# s1 = "abcde"
# s2 = "abfce"
# print(lcs(s1, s2))  # Output: ab
# # The longest common substring is "ab"


# # 104.	**Longest Common Subsequence (LCS)**

# # •	Implement the LCS algorithm for two sequences.

# def lcs(s1, s2):
#     m, n = len(s1), len(s2)
#     dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
#     for i in range(1, m+1):
#         for j in range(1, n+1):
#             if s1[i-1] == s2[j-1]:
#                 dp[i][j] = 1 + dp[i-1][j-1]
#             else:
#                 dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
#     return dp[m][n]

# s1 = "abcde"
# s2 = "ace"
# print(lcs(s1, s2))  # Output: 3
# # The longest common subsequence is "ace"


# # 105.	**Coin Change (Greedy)**

# # •	Given a list of coin denominations and a target amount, find the minimum number of coins needed using a greedy approach.

# def coin_change(coins, amount):
#     coins.sort(reverse=True)
#     count = 0
    
#     for coin in coins:
#         count += amount // coin
#         amount %= coin
    
#     return count if amount == 0 else -1

# coins = [1, 2, 5]
# amount = 11

# print(coin_change(coins, amount))  # Output: 3
# # The minimum number of coins needed is 3 (5, 5, 1) to make 11.


# # 106.	**Coin Change (DP)**

# # •	Solve the coin change problem using dynamic programming for an exact solution.

# def coin_change(coins, amount):
#     dp = [float('inf')] * (amount+1)
#     dp[0] = 0
    
#     for coin in coins:
#         for i in range(coin, amount+1):
#             dp[i] = min(dp[i], dp[i-coin]+1)
    
#     return dp[amount] if dp[amount] != float('inf') else -1

# coins = [1, 2, 5]
# amount = 11

# print(coin_change(coins, amount))  # Output: 3


# # 107.	**Knapsack Problem (0/1 DP)**

# # •	Implement the 0/1 Knapsack using dynamic programming.

# def knapsack(values, weights, capacity):
#     n = len(values)
#     dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    
#     for i in range(1, n+1):
#         for w in range(1, capacity+1):
#             if weights[i-1] > w:
#                 dp[i][w] = dp[i-1][w]
#             else:
#                 dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
    
#     return dp[n][capacity]

# values = [60, 100, 120]
# weights = [10, 20, 30]
# capacity = 50
# print(knapsack(values, weights, capacity))  # Output: 220


# # 108.	**Permutations of a List**

# # •	Generate all permutations of a given list of distinct elements.


# import itertools

# def main():
#     lst = [1, 2, 3]
#     permutations = list(itertools.permutations(lst))
#     print(permutations)

# main()  


# # 109.	**Backtracking: N-Queens**

# # •	Implement the N-Queens puzzle using backtracking.

# def solve_nqueens(n):
#     def is_safe(board, row, col):
#         # Check row
#         for i in range(col):
#             if board[row][i] == 1:
#                 return False
        
#         # Check upper diagonal
#         for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
#             if board[i][j] == 1:
#                 return False
        
#         # Check lower diagonal
#         for i, j in zip(range(row, n, 1), range(col, -1, -1)):
#             if board[i][j] == 1:
#                 return False
        
#         return True
    
#     def solve(board, col):
#         if col >= n:
#             return True
        
#         for i in range(n):
#             if is_safe(board, i, col):
#                 board[i][col] = 1
                
#                 if solve(board, col+1):
#                     return True
                
#                 board[i][col] = 0
        
#         return False
    
#     board = [[0 for _ in range(n)] for _ in range(n)]
    
#     if not solve(board, 0):
#         return "No solution"
    
#     return board

# def print_board(board):
#     for row in board:
#         print(row)

# n = 4
# board = solve_nqueens(n)
# print_board(board)


# # 110.	**Shortest Path in a Grid**

# # •	Given a 2D grid, find the shortest path from top-left to bottom-right, moving only down or right (use BFS or DFS).


# def shortest_path(grid):
#     rows, cols = len(grid), len(grid[0])
#     visited = [[False for _ in range(cols)] for _ in range(rows)]
#     queue = [(0, 0, 0)]
    
#     while queue:
#         row, col, steps = queue.pop(0)
        
#         if row == rows-1 and col == cols-1:
#             return steps
        
#         visited[row][col] = True
        
#         # Move down
#         if row+1 < rows and not visited[row+1][col]:
#             queue.append((row+1, col, steps+1))
        
#         # Move right
#         if col+1 < cols and not visited[row][col+1]:
#             queue.append((row, col+1, steps+1))
    
#     return -1

# grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(shortest_path(grid))  # Output: 6
# # The shortest path is 1 -> 2 -> 3 -> 6 -> 9
# # Total steps = 4


# # 111 Password Generator - Creates a random password of specified length
# import random

# def generate_password(length=12):
#     characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
#     password = ""
#     for i in range(length):
#         random_index = random.randint(0, len(characters) - 1)
#         password += characters[random_index]
#     return password

# print(generate_password())


# # 112. Contact Book - Stores and manages contact information
# class ContactBook:
#     def __init__(self):
#         self.contacts = {}  # Store contacts in dictionary
        
#     def add_contact(self, name, phone, email):
#         # Save contact details
#         self.contacts[name] = {
#             "phone": phone,
#             "email": email
#         }
        
#     def find_contact(self, name):
#         # Return contact if found, else return None
#         return self.contacts.get(name)


# # 113 Quiz Game - Simple multiple choice quiz
# quiz_questions = [
#     {
#         "question": "What is the capital of France?",
#         "answer": "Paris",
#         "choices": ["London", "Paris", "Berlin", "Madrid"]
#     },
#     {
#         "question": "What is the largest planet in our solar system?",
#         "answer": "Jupiter",
#         "choices": ["Mars", "Venus", "Jupiter", "Saturn"]
#     },
#     # More questions can be added here
# ]

# score = 0

# # Ask the questions and display the choices
# for question_data in quiz_questions:
#     question = question_data["question"]
#     choices = question_data["choices"]

#     print("\n" + question)
#     for i in range(len(choices)):
#         print(str(i+1) + ". " + choices[i])

#     user_answer = input("Enter your answer: ")

#     if user_answer == question_data["answer"]: # score
#         score += 1
#         print("Correct!")
#     else:
#         print("Wrong!")

# print("Final score: " + str(score) + "/" + str(len(quiz_questions)))


# # 114 Hangman
# import random
# def play_hangman():
#     words = ["python", "code", "program", "computer"]
#     secret_word = random.choice(words)
#     guessed_letters = set()
#     tries = 6
    
#     while tries > 0:
#         display = ''
#         for letter in secret_word:
#             if letter in guessed_letters:
#                 display += letter
#             else:
#                 display += '_'
        
#         print(f"\nWord: {display}")
#         print(f"Tries left: {tries}")
        
#         guess = input("Guess a letter: ").lower()
#         guessed_letters.add(guess)
        
#         if all(letter in guessed_letters for letter in secret_word):
#             return "You won!"
#         elif guess not in secret_word:
#             tries -= 1
    
#     return f"Game Over! The word was {secret_word}"


# # 115 tick tack toe
# def play_tictactoe():
#     # Create an empty board
#     board = [" " for _ in range(9)]
    
#     def show_board():
#         # Display the 3x3 grid
#         for row in range(0, 9, 3):
#             print(f"{board[row]} | {board[row+1]} | {board[row+2]}")
    
#     for turn in range(9):
#         show_board()
#         player = "X" if turn % 2 == 0 else "O"
#         position = int(input(f"\nPlayer {player}, choose position (1-9): ")) - 1
        
#         if board[position] == " ":
#             board[position] = player
#         else:
#             print("Position already taken!")
#             continue
            
#         # Check for win
#         winning_combinations = [
#             [0,1,2], [3,4,5], [6,7,8],  # rows
#             [0,3,6], [1,4,7], [2,5,8],  # columns
#             [0,4,8], [2,4,6]  # diagonals
#         ]
        
#         for combo in winning_combinations:
#             if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
#                 show_board()
#                 return f"Player {player} wins!"
    
#     return "It's a tie!"

# print(play_tictactoe())


# # 116. Adventure Game - Simple text adventure
# def play_adventure():
#     print("You're in a dark room with two doors.")
#     choice = input("Choose 'left' or 'right' door: ").lower()
    
#     if choice == "left":
#         print("You found a treasure chest!")
#         if input("Open it? (yes/no): ").lower() == "yes":
#             return "You found gold! You win!"
#         return "You leave the treasure. Game Over!"
#     return "You fell into a pit! Game Over!"
# print(play_adventure())


# # 117. Rock Paper Scissors - Classic game
# def play_rps():
#     import random
    
#     # Game rules: key beats value
#     rules = {
#         "rock": "scissors",
#         "paper": "rock",
#         "scissors": "paper"
#     }
    
#     # Get choices
#     player = input("Choose rock, paper, or scissors: ").lower()
#     computer = random.choice(list(rules.keys()))
#     print(f"Computer chose: {computer}")
    
#     # Determine winner
#     if player == computer:
#         return "Tie!"
#     elif rules[player] == computer:
#         return "You win!"
#     return "Computer wins!"


# # 118. Email Slicer - Splits email into username and domain
# def slice_email(email):
#     try:
#         # Split email at @ symbol
#         username, domain = email.split('@')
#         return {
#             "username": username,
#             "domain": domain
#         }
#     except:
#         return "Invalid email format"


# # 119. Dictionary - Looks up word definitions
# def lookup_word(word):
#     import requests
    
#     try:
#         # Get definition from dictionary API
#         url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
#         response = requests.get(url)
#         data = response.json()
        
#         # Return first definition found
#         return data[0]['meanings'][0]['definitions'][0]['definition']
#     except:
#         return "Word not found"


# # 120. Todo List - Task manager
# class TodoList:
#     def __init__(self):
#         self.tasks = []  # List to store tasks
    
#     def add_task(self, task):
#         # Add new task as not completed
#         self.tasks.append({"task": task, "completed": False})
        
#     def complete_task(self, task_number):
#         # Mark task as completed
#         if 0 <= task_number < len(self.tasks):
#             self.tasks[task_number]["completed"] = True
            
#     def view_tasks(self):
#         # Show all tasks and their status
#         for i, task in enumerate(self.tasks):
#             status = "✓" if task["completed"] else " "
#             print(f"{i+1}. [{status}] {task['task']}")

