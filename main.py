# def custom_eval(str_input):
#     count = 0
#     len = len(str_input)
#     for i in range (0,len):
#         if str_input[i]=='(':
#             n = 0
#             j = i
#             while str_input[j] != ')':
#                 j += 1
#                 n += 1
#            for a in range (i,n) :
#             if str_input[a] == '*':
#              int(str_input[a - 1]) * int(str_input[a + 1])
#             elif str_input[i] == '/':
#              int(str_input[a - 1]) / int(str_input[a + 1])
#             elif str_input[i] == '+':
#              int(str_input[a - 1]) + int(str_input[a + 1])
#             elif str_input[i] == '-':
#              int(str_input[a - 1]) - int(str_input[a + 1])

from data import number_count
numlist =[]
n = int(input("enter the number of elements :"))
print("enter your list numbers :")
for i in range (0 , n):
    lst = int(input())
    numlist.append(lst)
print(f"your list is {numlist}")
print(number_count(numlist))




# num = int(input('Enter a number :'))
# if (num%2 == 0) :
#     print('your number is even')
#
# elif (num%2 != 0) :
#     print('you number is odd')
# for i in range(10):
#     print(i)
# for i in "ali zanjanian":
#     print(i)

# scores = [10, 15, 20, 20, 12, 16]
# for i in scores:
#     if i == 10:
#         print(i,'is equall to 10')
#     elif i > 10:
#         print(i,'is upper than 10')
#     else:
#         print(i,'is lower than 10')
# even_list=[]
# odd_list=[]
# for i in range(100):
#     if i%2 == 0:
#         even_list.append(i)
#     else :
#         odd_list.append(i)
# even_list = [i for i in range(100) if i%2 == 0]
# odd_list = [i for i in range(100) if i%2 ==1 ]
# print(even_list)
# print(odd_list)
#
# n = 10
# while n <= 100 :
#     print(n)
#     n += 1
# x2list = [j*2 for j in range(10) if j%2 == 0]
# print(x2list)
