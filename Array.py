# list = [6,5,4,3,2,1]
# print(list[::-1])

# a = [1, 3, 4, 2, 7, 5, 8, 6]
# n = len(a)
# # Function call
# print("Mean =", (a, n))
# print("Median =", (a, n))


# def mode(arr) :
#     m = max([arr.count(a) for a in arr])
#     return [x for x in arr if arr.count(x) == m][0] if m>1 else None

# def mode(list):
#     x = {}
#     for i in list:
#         if not i in x:
#             x[i] = 1
#         else:
#             x[i] +=1
#     return [ y for y,l in x.items() if 1==max(x.values())]


# list = [4 ,5, 6, 7,4,2,5]
# for i in list:
#     if list.count(i)>1:
#         for x in range(list.count(i)):
#             list.remove(i)
# print(list)  

# list= [4 ,5, 6,6, 7,4,2,5]
# a = []
# for i in list:
#     if i not in a:
#         a. append(i)
#     else:
#         print(i,end=' ')


# # Mode:
# from collections import Counter
# numb = [2, 3,3, 4, 5, 7, 2]
# no = len(numb)
# val = Counter(numb)
# findMode = dict(val)
# mode = [i for i, v in findMode.items() if v == max(list(val.values()))]  
# if len(mode) == no:
#     findMode = "The group of number do not have any mode"
# else:
#     findMode = "The mode of a number is / are: " + ', '.join(map(str, mode))
# print(findMode)
      
numb = [2, 4, 5, 8, 9]
no = len(numb)
numb.sort()
if no % 2 == 0:
    median1 = numb[no//2]
    median2 = numb[no//2 - 1]
    median = (median1 + median2)/2
else:
    median = numb[no//2]
print("The median of the given numbers  (", numb, ") is", str(median))