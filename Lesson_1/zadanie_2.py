"""
[ Первая программа ]
"""
# name = "Alice" #str
# age = 30 #int
# is_student = False #bool

# print(f"Name: {name}, Age: {age}, Student: {is_student}")

"""
[ Вторая программа ]
"""
# x = 10
# y = 3

# print(x + y)   # 13
# print(x - y)   # 7
# print(x * y)   # 30
# print(x / y)   # 3.333...
# print(x // y)  # 3
# print(x % y)   # 1
# print(x ** y)  # 1000

"""
[ Третья программа ]
"""
# peremennay_1 = 1
# peremennay_2 = 2.5

# print(type(peremennay_1))
# print(type(peremennay_2))

# peremennay_3 = int(peremennay_2)
# print(type(peremennay_3))
# print(peremennay_3)

"""
[ Чётвёртая программа ]
"""

peremennay_4 = """
Мороз и солнце; день чудесный!\n
Еще ты дремлешь, друг прелестный —\n
Пора, красавица, проснись:\n
Открой сомкнуты негой взоры\n
Навстречу северной Авроры,\n
Звездою севера явись!
"""
print(len(peremennay_4))

'''
[ Пятая программа ]
Обратное преобразование из строки в число работать не будет!
'''
# peremennay_5 = int("2+2")
# print(type(peremennay_5))

'''
[ Шестая программа ]
Преобразование из числа в строку выполнится успешно.
Но при работе он почитает арифметическое действие.
'''
peremennay_6 = str(2+2)
print(type(peremennay_6))
print(peremennay_6)
