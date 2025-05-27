import psutil

# Получение информации о виртуальной памяти
virtual_memory = psutil.virtual_memory()

# Конвертация байтов в гигабайты (1024 * 3)
total_gb = virtual_memory.total / (1024 * 1024 * 3)
available_gb = virtual_memory.available / (1024 * 1024 * 3)
used_gb = virtual_memory.used / (1024 * 1024 * 3)
free_gb = virtual_memory.free / (1024 * 1024 * 3)

# Вывод информации о виртуальной памяти в гигабайтах
print(f"Всего памяти: {total_gb:.2f} ГБ")
print(f"Использовано памяти: {used_gb:.2f} ГБ")
print(f"Доступно памяти: {available_gb:.2f} ГБ")
print(f"Свободно памяти: {free_gb:.2f} ГБ")
