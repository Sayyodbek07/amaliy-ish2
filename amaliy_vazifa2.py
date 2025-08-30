#  Vazifa 1: Book (Kitob) obyekti
# 📌 Talab: Book nomli class yozing. Unda quyidagilar bo‘lsin:
# atributlar: title (nomi), author (muallif), year (chiqarilgan yil)
#
#
# metod: get_info() → kitob haqida ma’lumotni chiqaradi.
#
# Vazifa 2: Student (Talaba) obyekti
# 📌 Talab: Student class yozing. Unda quyidagilar bo‘lsin:
# atributlar: name, age, grade (kursi)

# metod: introduce() → talabani tanishtirib beradi.

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Kitob: {self.title}, Muallif: {self.author}, Yil: {self.year}"


book1 = Book("Sariq devni minib", "Xudoyberdi Toxtaboyev", 2011)
book2 = Book("Sariq devni minib", "Xudoyberdi Toxtaboyev", 2011)
print(book1.get_info())





# 2-misol
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        print(f"Mening ismim {self.name}, yoshim {self.age} da, {self.grade}-kurs talabasiman.")



talaba1 = Student("Sayyodbek", 20, 2)
talaba1.introduce()
