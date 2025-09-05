# # Q1
# def diff17(x):
#     if x <= 17:
#         return 17 - x
#     else:
#         return (x - 17) * 2
# print(diff17(22))
# print(diff17(14))

#  Q2
# def test_range(x):
#     return (x in range(100,1001)) or (x == 2000)
# print(test_range(150))
# print(test_range(2500))

# # Q3
# def reverse_string(text):
#     return text[::-1]
# print(reverse_string("robot"))

# # Q4
# def count_case(text):
#     result = {"UPPER":0, "LOWER":0}
#     for c in text:
#         if c.isupper():
#             result["UPPER"] += 1
#         elif c.islower():
#             result["LOWER"] += 1
#     return result
# print(count_case("RoBotics"))

# # Q5
# def unique_list(data):
#     output = []
#     for x in data:
#         if x not in output:
#             output.append(x)
#     return output
# print(unique_list([1,2,2,3,4,4,5]))

# # Q6
# def even_numbers(data):
#     output = []
#     for x in data:
#         if x % 2 == 0:
#             output.append(x)
#     return output
# print(even_numbers([1,2,3,4,5,6,7,8,9]))

# # Q7
# def robot():
#     def move():
#         print("Robot is moving")
#     move()
# robot()

# # Q8
# def student(name, age, course):
#     return name, age, course
# print(student.__code__.co_varnames)

# # Q9
# def move_robot(a, b, direction):
#     if direction == "up":
#         b += 1
#     elif direction == "down":
#         b -= 1
#     elif direction == "left":
#         a -= 1
#     elif direction == "right":
#         a += 1
#     return (a,b)
# print(move_robot(0,0,"up"))
# print(move_robot(2,3,"left"))

# # Q10
# def classify_temperature(t):
#     if t < 15:
#         return "Cold"
#     elif 15 <= t <= 30:
#         return "Moderate"
#     else:
#         return "Hot"
# print(classify_temperature(10))
# print(classify_temperature(20))
# print(classify_temperature(35))

# # Q11
# def is_goal_reached(moves):
#     a = 0
#     b = 0
#     for move in moves:
#         if move == "up":
#             b += 1
#         elif move == "down":
#             b -= 1
#         elif move == "left":
#             a -= 1
#         elif move == "right":
#             a += 1
#     return (a,b) == (2,0)
# print(is_goal_reached(["up","right","right","down"]))
# print(is_goal_reached(["up","right"]))

# # Q12
# class Student:
#     def __init__(self, id, name, cls):
#         self.id = id
#         self.name = name
#         self.cls = cls
#     def display(self):
#         print("ID:", self.id, "Name:", self.name, "Class:", self.cls)
# s = Student(1,"Tanmay","RAI")
# s.display()

# # Q13
# class Student:
#     def __init__(self, id, name, cls):
#         self.id = id
#         self.name = name
#         self.cls = cls
# s1 = Student(1,"Tanmay","RAI")
# s2 = Student(2,"Alice","AI")
# print("ID:", s1.id, "Name:", s1.name, "Class:", s1.cls)
# print("ID:", s2.id, "Name:", s2.name, "Class:", s2.cls)

# # Q14
# import math
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return math.pi * self.radius * self.radius
#     def perimeter(self):
#         return 2 * math.pi * self.radius
# c = Circle(5)
# print(c.area())
# print(c.perimeter())

# # Q15
# class StringClass:
#     def get_String(self):
#         self.text = input("Enter a string: ")
#     def print_String(self):
#         print(self.text.upper())
# obj = StringClass()


# # Q16
# class Robot:
#     def __init__(self, name, task):
#         self.name = name
#         self.task = task
#         self.battery = 100
#     def perform_task(self):
#         print(self.name, "is performing:", self.task)
#         self.battery -= 10
#     def recharge(self):
#         self.battery = 100
#     def status(self):
#         print("Name:", self.name, "Task:", self.task, "Battery:", self.battery)
# r = Robot("Robo1","Cleaning")
# r.perform_task()
# r.status()
# r.recharge()
# r.status()