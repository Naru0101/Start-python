x = 5
y = "Hello, World!" # контейнер для хранения 

a = 10 #int целое 
b = 3.14 #float дроби
c = "python" #str текст
d =True #bool правда или ложь 

list = [1,2,3,4,5, "Python"] # list списки изи )
tuple = (1,2,3,4,5, "Python") # tuples кортежи 
set = {1,2,3,4,5} # множества
dict = {"name": "Ihor", "age": 16} # Словари изи бро

x = 10
if x > 5:
    print("x is greater than 5") # Условия оператора 

# циклы )    
for i in range(5):
    print(i)    
    
#цикл while    
i = 0
while i < 5:
    print(i)
    i += 1

#Функции
def greet(name):
    print("Hello,"+ name +"!")
    
#Обработка исключения
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")

#Ввод и вывод даных
name = input("Enter your name: ")
print("Hello,"+ name +"!")

#Форматирование строк 
age = 25
print("My age is {}".format(age))
#ил так 
print(f"My age is{age}")

#Обасть видимости переменных
global_vriable = 10

def my_function():
    local_variable = 5
    print(local_variable)
my_function()    
    
# coments
# this is comments
"Это многострочный коментарий "

#WORK OF FILE 
with open("example.txt", "r") as files:
    content = files.read()
    
#Лямда-функции
square = lambda x: x** 2
print(square(5))

#Генераторы и списковые выражения 
squares = [x **2 for x in range(5)]

#Обработка сктрок множество методов для работы со строками, таких как split(), join(), replace().
sentance = "this is a samle sentence"
words = sentance.slit()
 
#Работа с временем и датами: Модуль datetime позволяет работать с датами и временем.
from datetime import datetime
current_time = datetime.now()

#Итераторы и Генераторы/Генераторы - это специальный вид итераторов, создаваемых с использованием ключевого слова yield
def square_generator(n):
    for i in range(n):
        yield i ** 2
squares = square_generator(5)
for square in squares:
    print(square)
    
#Классы позволяют создавать свои собственные типы данных. Объекты - это экземпляры классов.
class Car:
    def __init__(self, brand, models):
        self.brand = brand
        self.model = models
my_car = Car("Toyota", "BMV", "camry")

#Декораторы используются для изменения поведения функций. Они позволяют обернуть функцию в другую функцию.
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening afterthe function is called.")
    return wrapper   