# for i in range(100):
#     print("Love You Jyoti")
# 1>:-----------

# a = {1, 2, 3}
# b = {4, 5, 6}

# print(a | b)

# a |= b

# print(a)
# 2>:-----------

# def func(x):
#     return x[::-1].title()

# x = 'Oediv eht ekil esaelp'
# print(func(x))
# 3>:----------

# user = 'Jyoti' 

# if user is not None:
#     print(user)

# if None is not user:
#     print(user)

# if not user is None:
#     print(user)

# def max_value_3(a,b,c):
#     if a > b:
#         return a
#     elif b > c :
#         return b
#     else :
#         return c
# c = max_value_3(50,70,30)
# print(c)

# a = "Jyoti"
# last_char = a[-1]
# print('last charecter:',last_char)

# x = lambda a : a +10
# print(x(5))

# add = lambda x , y: x+y
# mul = lambda x,y: x*y
# print(mul(10,20))

# N = int(input(""))
# for i in range(N):
    # reversed = input()
    # print(int(reversed[::-1]))

# side = int(input())
# area = side * side
# print('Area of the sqaure ='+str(area))

# side = int(input())
# print("Square star pattern")
# for i in range(side):
#     for i in range(side):
#         print("*", end = ' ')
#     print()

a=[23,78,[12,98]]
sum=0
for i in a[2]:
    sum=sum+i
    print(sum)