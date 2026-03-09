# # class Parent:
# #     name= 'Python'
# #     @classmethod
# #     def result(cls, a,b):
# #         print('Parent class')
# #         return a+b, cls.name
# class Base:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
    
#     @property
#     def add(self):
#         return self.num2
    
#     @add.setter
#     def add(self,m):
#         self.num2 = m**2
    
#     @property
#     def add1(self):
#         return self.num1
#     @add1.setter
#     def add1(self,n):
#         self.num1 = n**3
# res = Base(9,9)
# res.add1 = 3
# res.add = 4
# print(res.add1)



# class Addition:
#     def __init__(self,a):
#         self.a = a 
#         # self.b = b
    
#     def __list__(self, k):
#         return self.a+k.a
#     def __add__(self, k):
#         return self.a+k.a

# obj1 = Addition([2,3,4,5])
# obj2 = Addition([3,4,5,1])

# print(obj1.__add__(obj2))


# class Multiplication:
#     def add(self, num1,num2):
#         return num1+num2

# class Addition(Multiplication):
#     def add(self, num1,num2):
#         return num1-num2

# m = Multiplication()
# print(m.add(7,5))
# a = Addition()
# print(a.add(4,5))
