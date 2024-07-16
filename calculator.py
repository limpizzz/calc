
# Функция сложения
def add(a, b):
    return a + b

# Функция вычитания
def subtract(a, b):
    return a - b

# Функция умножения
def multiply(a, b):
    return a * b

# Функция деления
def divide(a, b):
    return a / b

# Пользовательский ввод чисел и операции
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
operation = input("Выберите операцию (+, -, *, /): ")

# Выполнение выбранной операции
if operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = subtract(num1, num2)
elif operation == "*":
    result = multiply(num1, num2)
elif operation == "/":
    result = divide(num1, num2)
else:
    print("Некорректная операция.")

# Вывод результата
print(result)



