# #1  Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".

# num_0 = int(input("Input a number for a:  "))
# num_1 = int(input("Input a number for b: "))

# if num_0==num_1 : 
#     print("1")
# elif num_0>num_1 :
#     print("2")
# else :
#     print("3")

# # 2. Print "Hello" if a is equal to b, and c is equal to d.

# a = int(input("Input a number for a:  "))
# b = int(input("Input a number for b: "))
# c = int(input("Input a number for c: "))
# d = int(input("Input a number for d: "))

# if a==b and c==d :
#     print("HELLO")

# # 3. Print "Hello" if a is equal to b or c is equal to d.

# a = int(input("Input a number for a:  "))
# b = int(input("Input a number for b: "))
# c = int(input("Input a number for c: "))
# d = int(input("Input a number for d: "))

# if a==b or c==d :
#     print("HELLO")

# #4.  For given integer x, print ‘True’ if it is positive, print ‘False’ if it is negative and print ‘zero’ if it is 0.

# a = int(input("Input a number:  "))
# if a>0 :
#     print("True")
# elif a<0 :
#     print("False")
# elif a==0 :
#     print("zero")

# # 5. Check whether the user input number is even or odd and display it to user.
# num_3 = int(input("Input a number"))
# if num_3%2 ==0 :
#     print(f"{num_3} is a even number")
# elif num_3%2 !=0 :
#     print(f"{num_3} is a odd number")

# # 6.  WAP which accepts marks of four subjects and display total marks, percentage and grade
# math = int(input("Enter the marks in maths :"))
# science = int(input("Enter the marks in science :"))
# english = int(input("Enter the marks in english :"))
# nepali = int(input("Enter the marks in nepali :"))

# total_marks = math + science + english +nepali
# percentage = total_marks/400 * 100
# if 0<(math or science or english or nepali) <100 :
#     print("Enter more than 0 or less than hundred") 
# else :
#     print(f"marks in math is {math}")
#     print(f"marks in science is {science}")
#     print(f"marks in english is {english}")
#     print(f"marks in nepali is {nepali}")
#     print(f"your total marks is {total_marks}")    
# print(f"your percentage is {percentage}%")
# if percentage >= 80 :
#     print("You gotDistinction")
# elif percentage >= 60 :
#     print("you got first divison")
# elif percentage >= 40 :
#     print("You pass")
# elif percentage < 40 :
#     print("You fail")

# a = "APPLE"
# b = "apple"
# print(a.lower())
# print(b.upper())

# name = input("Enter your name :")
# address = input("Enter your address :")
# age = input("Enter your age :")

# print(f"Hello {name}, \nYour address is {address}. \nYour age is {age}.")

# # Write a python program which accepts the radius of circle from user and compute the area.
# import math


# import math
# radius = float(input("Enter the radius of circle :"))
# pi = math.pi
# area = pi * (radius**2)
# print(area)

# #  A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of students in each class, print the smallest possible number of desks that can be purchased.
# a = int(input("number of student in classroom A :"))
# b = int(input("number of student in classroom B :"))
# c = int(input("number of student in classroom C :")) 

# total_desk = (a+b+c)/2
# z = round(total_desk)
# print(f"the smallest possible number of desks that can be purchased is {z} ")


# #11. Given three integers, print the smallest one. (Three integers should be user input)

# num1=int(input("Enter the first number: "))
# num2=int(input("Enter the second number: "))
# num3=int(input("Enter the third number: "))

# if(num1<=num2):
#       if(num1<=num3):
#             d=num1
#       else:
#           d=num3
# else:
#       if (num2<=num3):
#         d=num2
#       else:
#         d=num3

       
# print(f"Smallest number is {d}")

# #12. Write a program that takes three numbers and prints their sum. Every number is given on a separate line.
# a = int(input("Enter number one :"))
# b = int(input("Enter number two :"))
# c = int(input("Enter number third :"))
# print(f"the sum of {a},{b},{c} is {a + b + c}")

# # 13. Write a program that reads the length of the base and the height of a right-angled triangle  and prints the area. Every number is given on a separate line.
# base = int(input("Input the base of the triangle :"))
# height = int(input("Input the height of the triangle :"))
# area = 1/2 * base * height
# print(f"For {base} cm base and {height} cm height " , end = ":" )
# print(f"\nthe area of the triangle is {area}")

# # 14. N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket. How many apples will each single student get? How many apples will remain in the basket? The program reads the numbers N and K. It should print the two answers for the questions above.

# n = int(input("Enter the number of students"))
# k = int(input("Enter the number of apples"))

# print(f"each single student would get {k//n} apples.")
# print(f"{k%n} apples will remain in the basket. ")