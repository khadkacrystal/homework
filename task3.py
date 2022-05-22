# '''
# 1. Write a program to accept percentage and display the Category according to the  following criteria :

# Percentage	Category
# < 40	                     Failed
# >=40 & <55	Fair
# >=55 & <65	Good
# >=65	                     Excellent
# '''
# percentage = int(input("Enter your percentage :"))


# if percentage<0 or percentage>100 :
#     print("Enter more than 0 or less than hundred") 
# else :
#     print(f"marks in math is {percentage}")
#     if percentage >= 65 :
#         print("Excellent")
#     elif 55<=percentage<65 :
#         print("Good")
#     elif 40<=percentage<55 :
#         print("Fair")
#     elif percentage<40:
#         print("Failed")

# '''
# 2. Write a Python Program to Swap Two Variables.
# '''
# a = 10
# b = 20
# print(f"The value of a and b is {a} and {b}")
# temp = a
# a = b
# b = temp
# print(f"The swaped value of a and b is {a} and {b}")

# '''
# 3. Write a program to print multiplication table of a  number 10 using for loop.
# '''

# a = 10
# for i in range (1,11)  :
#     print(f"{a}*{i} = {a*i} ")

# '''
# 4. Print list in reverse order using a loop. Hint: list1=[1,2,3,4]
# '''

# list1 = [1,2,3,4]
# reverse_list = []
# for i in reversed(list1) :
#     reverse_list.append(i)
# print(reverse_list)

# '''
# 5. Display numbers from -10 to -1 using for loop.
# '''
# a = -10
# for i in range(0,10) :
#     print(a)
#     a+=1    

# a = 100
# for i in range(0,100,10) :
#     print(a)
#     a = a+i
# else :
#     print("done")

# '''
# 7. Find the factorial of a number 5.
# '''

# a = 5
# for i in range(1,a) :
#     a = a*i
# print(a)  

# '''
# 8. Use a loop to display elements from a given list present at odd index positions. Given: my_list=[10,20, 30, 40, 50, 60, 70, 80, 90, 100]
# '''
# my_list=[10,20,30,40,50,60,70,80,90,100]
# my_list = reversed(my_list)
# for i in range(0,10,2) :
    
#     print(my_list[i])

# '''
# 9. Calculate the cube of all numbers from 1 to a given number. (1-6)
# example:
# Expected output:
# 1-1
# 2-8
# 3-27
# 4-64
# 5-125
# 6-216
# '''
# for i in range(1,7) :
#     print(f"{i} - {i**3}")

# '''
# 10.  Print First 10 natural numbers using for loop.
# '''
# a = 1
# for i in range(0,10) :
#     print(a)
#     a+=1