# Q1

# (i)
# a=[11,12,13,14]
# a.append(50)
# a.append(60)
# print(a)

#(ii)
# a=[11,12,13,14]
# a.remove(11)
# a.remove(13)
# print(a)

#(iii)
# a=[11,12,13,14]
# a.sort
# print(a)

#(iv)
# a=[11,12,13,14]
# a.sort(reverse=True)
# print(a)

#(v)
# a=[11,12,13,14]
# if 13 in a:
#     print("13 is in the list")

#(vi)
# a=[11,12,13,14]
# print(len(a))

# (vii)
# a=[11,12,13,14]
# print(sum(a))

# (viii)
# a=[11,12,13,14]
# print(sum(x for x in a if x % 2 == 1))

# (ix)
# a=[11,12,13,14]
# print(sum(x for x in a if x % 2 == 0))

# (x)
# a=[11,12,13,14]
# total = 0
# for x in a:
#     if x > 1:
#         check = True
#         for i in range(2, int(x**0.5)+1):
#             if x % i == 0:
#                 check = False
#                 break
#         if check:
#            total += x
# print(total)

# (xi)
# a=[11,12,13,14]
# a.clear()
# print(a)

# (x)
# a=[11,12,13,14]
# del a



#Q2
# x = int(input("How many numbers? "))
# data = []
# for _ in range(x):
#     value = int(input("Enter a number: "))
#     data.append(value)
# total=0
# for i in data:   
#     total+=i
    
# print(total)

# Q3
# nums = [1,2,3,4]
# result = 1
# for x in nums:
#     result *= x
# print(result)

#Q4
# matrix=[]
# for i in range(3):
#     block=[]
#     for j in range(4):
#         line=[]
#         for k in range(6):
#             line.append('*')
#         block.append(line)
#     matrix.append(block)

# for block in matrix:
#     for line in block:
#         print(line)
#     print()


#Q5
# (i)
# d = {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
# d[8] = 8.8
# print(d)

# (ii)
# d = {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
# if 2 in d: del d[2]
# print(d)

#  (iii)
# d = {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
# print(6 in d)

# (iv)
# d = {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
# print(len(d))



# v)
# d= {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
# total=0
# for i in d.values():
#     total+=i
# print(total)

# (vi)
# d = {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
# if 3 in d: d[3] = 7.1
# print(d)


# (vii)
# d = {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
# d.clear()
# print(d)



# Q6
# (i)
# a = {10,20,30,40,50,60}
# b = {40,50,60,70,80,90}
# a.add(55)
# a.add(66)
# print(a)

# (ii)
# a = {10,20,30,40,50,60}
# b = {40,50,60,70,80,90}
# a.discard(10)
# a.discard(30)
# print(a)

# (iii)
# a = {10,20,30,40,50,60}
# b = {40,50,60,70,80,90}
# print(40 in a)

# (iv)
# a = {10,20,30,40,50,60}
# b = {40,50,60,70,80,90}
# print(a.union(b))

# (v)
# a = {10,20,30,40,50,60}
# b = {40,50,60,70,80,90}
# print(a.intersection(b))

# (vi)
# a = {10,20,30,40,50,60}
# b = {40,50,60,70,80,90}
# print(a.difference(b))


#q7 i)
# import string
# import random
# for i in range(100):
#     length=random.randint(6,8)
#     text=''
#     for j in range(length):
#         c=random.choice(string.ascii_letters)
#         text=text+c
#     print(text)

# Q7(ii)
# result = []
# for x in range(600, 801):
#     if x > 1:
#         check = True
#         for i in range(2, int(x**0.5)+1):
#             if x % i == 0:
#                 check = False
#                 break
#         if check:
#             result.append(x)
# print(result)
        
# Q7(iii)
# ans = []
# for x in range(100, 1001):
#     if x % 7 == 0 and x % 9 == 0:
#         ans.append(x)
# print(ans)        
  
        
# Q8
# date = (11, 12, 2025)
# print("The examination will start from:", date[0], "/", date[1], "/", date[2])
       

# Q9
# data = [10,11,15,23,25,30,42]
# for x in data:
#     if x % 5 == 0:
#         print(x)
        
# Q10
# x = 42
# even = (x % 2 == 0)
# odd = not even
# print(x, "is even?", even, "is odd?", odd)        
        

# Q11
# s = "Emma is my friend. Emma likes reading. EmmaEmma"
# print(s.count("Emma"))


# Q12
# x = [1,2,3,4,5]
# y = [6,7,8,9,10]
# result = []
# for i in x:
#     if i % 2 == 1:
#         result.append(i)
# for i in y:
#     if i % 2 == 0:
#         result.append(i)
# print(result)


#Q13
# coords = [(2,3), (4,5), (6,7), (7,8)]

# for p in coords:
#     a=p[0]
#     if(a%2==0):
#         print(p)


# Q14
# data = {1: 2.3, 2: 4.5, 3: 1.8, 4: 3.6}
# for key, value in data.items():
#     if(value>3):
#         print(key,value)


# Q15
# received = {"MOVE", "TURN_LEFT", "TURN_RIGHT", "STOP"}
# executed = {"MOVE", "TURN_LEFT", "STOP"}
# pending = received - executed
# print(pending)