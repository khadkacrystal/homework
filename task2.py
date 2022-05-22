# # What is the output of ‘banana’ > ‘BANANA’?

# a = "banana"
# b = "BANANA"
# print(a.upper())
# print(b.lower())

# # 2. Check whether 5 is in list of first 5 natural numbers or not

# a = [1,2,3,4,5]
# b= 5

# if b in a :
#     print("5 is in list of first 5 natural numbers")
# else :
#     print("5 is not in list of first 5 natural numbers")

# #3. Given three integers, print the smallest one. (Three integers should be user input)

# a = int(input("Enter a number one :"))
# b = int(input("Enter a number two :"))
# c = int(input("Enter a number three :"))

# if a<b :
#     if a<c :
#         print("a is the smallest ")
#     else :
#         print("c is the smallest")
# elif b<a :
#     if b<c:
#         print("b is the smallest.")
#     else :
#         print("c is the smallest")

# #4 Given a three-digit number. Find the sum of its digits.
# number= 123
# a = number//100
# b = number//10 % 10
# c = number % 10
# sum = a+b+c

# #Write a program that asks the user for a number in the range of 1 to 12. The program should display the corresponding month, where 1=january, 2=february,3=march,4=april,5=may,6=june,7=july, 8=august,9=september,10=october,11=november,12=december. The program should display an error message if the user enters a number that is outside the range of 1 to 12.


# a = int(input("Enter a number from 1 to 12 :"))
# if a == 1 :
#     print("january")
# elif a==2 :
#     print("february")
# elif a== 3 :
#     print("March")
# elif a==4 :
#     print("april")
# elif a== 5 :
#     print("May")
# elif a==6 : 
#     print("june")
# elif a==7 :
#     print("july")
# elif a==8:
#     print("august")
# elif a==9 :
#     print("september")
# elif a==10 :
#     print("october")
# elif a==11:
#     print("november")
# elif a==12:
#     print("december")
# else :
#     print("Enter from 1 to 12")

# # Given x = 5, what will be the value of x after we run x+=3?
# x = 5
# x+=3
# print(x) 
# #after we run it 3 will be added in x

# # Write a Python Program to Check Prime Number.
# flag = False
# a = int(input("Enter a number :"))
# if a>1 :
#     for i in range(2,a) :
#         if a%i==0 :
#             flag = True
#             break
# if flag :
#     print("a is not a prime number")
# else :
#     print("a is a prime number")

# # 8. A school has following rules for grading system: a. Below 25 - F b. 25 to 45 - E c. 45 to 50 - D d. 50 to 60 -  e. 60 to 80 - B f. Above 80 - A Ask user to enter marks and print the corresponding grade.
# math = int(input("Enter the marks in maths :"))


# if 0>(math) >100 :
#     print("Enter more than 0 or less than hundred") 
# else :
#     print(f"marks in math is {math}")
#     if math >= 80 :
#         print("You got grade A")
#     elif 60<=math<80 :
#         print("you got grade B")
#     elif 50<=math<60 :
#         print("You got grade C")
#     elif 45<=math<50 :
#         print("You got grade D")
#     elif 25<=math<45 :
#         print("You got grade E")
#     elif math<25 :
#         print("You got grade F")

# # 9. Take input of age of 3 people by user and determine oldest and youngest among them

# a = int(input("Enter the age of Ram :"))
# b = int(input("Enter the age of Shyam :"))
# c = int(input("Enter the age of Hari :"))

# if a>b and a>c :
#     print("Ram is the oldest")
# elif b>c and b>a :
#     print("Shyam is the oldest")
# elif c>b and c>a :
#     print("Hari is the oldest")
# if a<b and a<c :
#     print("Ram is the youngest")
# elif b<a and b<c :
#     print("Shyam is the youngest")
# elif c<a and c<b :
#     print("Hari is the youngest")       


# # 10.  Write a program to check whether a person is eligible for voting or not. (accept age from user)
# a= int(input("Enter your age :"))
# if a>18 :
#     print("you are allowed to vote")
# else :
#     print("you are not allowed to vote")

# # 11.  Write a program to check whether a number entered by user is even or odd.
# a = int(input('Enter a number :'))
# if a%2==0 :
#     print(" is a even number")
# else :
#     print("{} is a odd number".format(a))  
# # 12. Write a program to check whether a number is divisible by 7 or not.
# a = int(input("Enter a number :"))
# if a%7 == 0 :
#     print(f"{a} is divisble by seven")
#     print(a/7)
# else :
#     print(f"{a} is not divisble by seven")

# # Write a program to display "Hello" if a number entered by user is a multiple of five , otherwise print "Bye".
# a = int(input("Enter a number :"))
# if a%5 == 0 :
#     print("Hello")
# else :
#     print("Bye")

# # 14. Write a program to accept percentage from the user and display the grade according to the following criteria          Marks                                    Grade          > 90                                         A          > 80 and <= 90                    B          >= 60 and <= 80                  C          below 60                                 D
# a = int(input("Enter the percentage :"))
# if a>100 or a<0 :
#     print("Please enter percentage from 0 to 100")
# elif a>90:
#     print("A")
# elif 80<a<=90 :
#     print("B")
# elif 60<=a<=80:
#     print("C")
# elif a<60 :
#     print("D")

# '''
# 15. Accept any city from the user and display monument of that city.
#                   City                                 Monument
#                   Delhi                               Red Fort
#                   Agra                                Taj Mahal
#                   Jaipur                              Jal Mahal
# '''
# b = ['delhi','agra','Jaipur']
# a = input(f"Enter a city name in list {b}")
# if a=="delhi" :
#     print("Red Fort")
# elif a=="agra" :
#     print("Taj Mahal")
# elif a=="Jaipur" :
#     print("Jal Mahal")

# # 16. Write the output of the following if a = 9
# a = 9
# if (a > 5 and a <=10):    
#     print("Hello")    
# else:    
#     print("Bye")

# # Write a program to whether a number (accepted from user) is divisible by 2 and 3 both
# a = int(input("Enter a number :"))
# if a%2==0 and a%3==0 :
#     print(f"{a} is divisble by 2 and 3 both")
# else :
#     print(f"{a} is not divisible by 2 and 3 both")

# # 18. Write a program to check a character is vowel or not.
# a = ['a','e','i','o','u']
# b = input("Enter a letter :")
# if b in a :
#     print(f"{b} is a vowel")
# if b not in a :
#     print(f"{b} isnot a vowel")  

# # 19. Write a program to accept two numbers and mathematical operators and perform operation accordingly.
# a = int(input("Enter the first number:"))
# b  = int(input("Enter the second number:"))
# c =input('Enter a mathematical operator(+,-,/,*):')
# if c =='+' :
#     print(f"the sum of {a} and {b} is",a+b)
# elif c=='*' :
#     print(f"the multiplication of {a} and {b} is", a*b)
# elif c=='-' :
#     print(f"the difference of {a}and {b} is",a-b)
# elif c=='/' :
#     print(f"the divison of {a }and {b} is",a/b)
# else :
#     print("Enter a valid operator") 