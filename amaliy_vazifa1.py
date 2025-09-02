# 1-misol
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance


    def deposit(self):
        self.total_balance = self.__balance + 100_000
        return f"Siz balansingizga 100 000 ming qoshdingiz"

    def withdraw(self):
        return f"Sizning jami balancingiz {self.total_balance}"

obj = BankAccount(1_000_000)
print(obj.deposit())
print(obj.withdraw())


#
# # 2-misol
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.__grade = 0
#
#     def set_grade(self, grade):
#         if 0 == self.__grade <= 100:
#             self.__grade = grade
#
#     def get_grade(self):
#         return self.__grade
#
# student1 = Student("Sayyodbek")
# student2 = Student("Ziyobek")
# student1.set_grade(95)
# print(student1.name, "bahosi:", student1.get_grade())
#
# student2.set_grade(120)
# print(student2.name, "bahosi:", student1.get_grade())
#
#
#
#
# # 3-misol
#
# class Animal:
#     def sound(self):
#         return "Bazi hayvonlar tovushi"
#
# class Dog(Animal):
#     def sound(self):
#         return "vov vov"
#
# class Cat(Animal):
#     def sound(self):
#         return "myav myav"
#
# dog = Dog()
# cat = Cat()
#
# print("Itning ovozi:", dog.sound())
# print("Mushukning ovozi:", cat.sound())
#

# 4 - misol
class Vehicle:
    def move(self):
        return "harakatlanuvchi..."

class Car(Vehicle):
    def move(self):
        return "mashina harakatlanmoqda 🚘"

class Bike(Vehicle):
    def move(self):
        return "velosiped sporti 🚲"

car = Car()
bike = Bike()
print(car.move())
print(bike.move())


# 5-misol
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

shapes = [Circle(5), Rectangle(4, 6)]

for s in shapes:
    print(s.area())

# 5-misolni chuntirish: area() metodi barcha klasslarda bir xil nomda. Lekin hisoblash usuli har xil (Circle uchun radius, Rectangle uchun eni va bo‘yi).
# Bu — Polymorphism.


# 6-misol
class Employee:
    def work(self):
        return "ish qilish..."

class Developer(Employee):
    def work(self):
        return "Kodli dastur 👨‍💻"

class Manager(Employee):
    def work(self):
        return "boshqaruv jamoasi👨‍💼"

dev = Developer()
mgr = Manager()
print(dev.work())
print(mgr.work())


# 7-misol
class Payment:
    def pay(self, amount):
        return f"Paid {amount} so‘m"

class CreditCardPayment(Payment):
    def pay(self, amount):
        return f"Kredit kartaga {amount} so‘m  tolangan"

class PayPalPaynet(Payment):
    def pay(self, amount):
        return f"Payment  orqali {amount} so‘m toladim "

cc = CreditCardPayment()
pp = PayPalPaynet()

print(cc.pay(2000))
print(pp.pay(3500))


# 8-misol
class Transport:
    def go(self):
        return "Transport is moving..."

class Bus(Transport):
    def go(self):
        return "avtobus shaxobchaga toxtadi "

class Train(Transport):
    def go(self):
        return "poyezd yuryapti"

bus = Bus()
train = Train()

print(bus.go())
print(train.go())
