#q1 
# print("Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are")

#q2
# a=input("Enter you first name")
# b=input("Enter you last name")
# print(b,a)

#q3
# r=input("Enter the radius of the circle")
# area=3.14*int(r)*int(r)
# print("The area of the cricle of radius",r,"is",area)

#q4
# colors=["Red","Green","White","Black"]
# print("First:",colors[0],"\nLast:",colors[3])

#q5
# x=int(input("Enter a number:"))
# print(x+x*x+x*x*x)

#q6
# data=input("Enter the values:")
# a=data.split(',')
# b=tuple(a)
# print(a)
# print(b)

#q7
# c=float(input("Enter the temperature in celcius:"))
# f=(9/5*c)+32
# print(f)

#q8
# a=int(input("Enter First Number:"))
# b=int(input("Enter Second Number:"))
# a,b=b,a
# a+=1
# print("First Number:",a)
# print("Second Number:",b)

#q9
# x=int(input("Enter a number:"))
# if(x%2==0):
#     print(x,"is even")
# else:
#     print(x,"is odd")

#q10
# y=int(input("Enter a year to check if its leap or not"))
# if(y%4==0 and y%100!=0) or (y%400==0):
#     print(y,"is a leap year")
# else:
#     print(y,"is not a leap year")

#q11
# import math
# a=int(input("Enter the x coordinate of first point:"))
# b=int(input("Enter the y coordinate of first point:"))
# c=int(input("Enter the x coordinate of second point:"))
# d=int(input("Enter the y coordinate of second point:"))

# distance= math.sqrt((c-a)**2-(d-b)**2)
# print("The Euclidean distance between the two coordinates is:",distance)

#q12
# x=int(input("Enter the first angle:"))
# y=int(input("Enter the second angle:"))
# z=int(input("Enter the third angle:"))

# if(x+y+z==180):
#     print("These angles form a Triangle")
# else:
#     print("These three angles do not form a triangle")

#q13
# principal=int(input("Enter the principal amount:"))
# rate=float(input("Enter the rate of interest in %:"))
# times=int(input("Enter the number of times interest applied per time period:"))
# period=int(input("Enter the number of time period ellapsed:"))
# result=principal*((1+rate/times)**(times*period))
# print("Amount after compound interest:",result)

#q14
# x=int(input("Enter a number:"))
# counter=0
# for i in range(2,x//2+ 1):
#     if(x%i==0):
#         counter+=1
# if(counter>0):
#     print(x,"is not prime")
# else:
#     print(x,"is a prime number")

#q15
# x=int(input("Enter a number:"))
# total=0
# for i in range(x+1):
#     total+=i*i
# print("Sum:",total)