# class MyClass(object):
#     def __init__(self, name, gender, age, bank_cost = ""):
#         self.name = name
#         self.gender = gender
#         self.age = age
#         self.bank_cost = bank_cost
#
#     @property
#     def bank_cost(self):
#         return self.__bank_cost
#
#     @bank_cost.setter
#     def bank_cost(self, value):
#         self.__bank_cost = value
#
# shon = MyClass("Shon", "male", 32)
# shon.bank_cost = 99999
# mary = MyClass("Mary", "female", 33)
#
# print(shon.age)
# print(shon.bank_cost)