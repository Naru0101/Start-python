#Нужно знать для )+
import random
import string

length = int(input("Введите длину пароля: "))

password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
print("Сгенерированный пароль:", password)