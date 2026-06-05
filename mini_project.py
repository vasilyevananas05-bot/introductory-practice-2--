# Запрашиваем количество операций
count = int(input("Сколько будет статей (N)? "))
# мы приравниваем к 0 для того чтобы у нас программа должна создать переменную и положить в неё стартовое значение. Ноль здесь — это чистый лист
# 
total_income = 0
total_expenses = 0

# Собираем доходы в одном цикле
print("--- Ввод доходов ---")
for i in range(count):
    name = input("Название дохода: ")
    amount = float(input(f"Сумма для {name}: "))
    total_income = total_income + amount # Прибавляем к общей сумме

# Собираем расходы во втором цикле
print("--- Ввод расходов ---")
for i in range(count):
    name = input("Название расхода: ")
    amount = float(input(f"Сумма для {name}: "))
    total_expenses = total_expenses + amount

# Считаем остаток
balance = total_income - total_expenses

# Выводим результаты
print("--- Результат ---")
print("Доходы:", total_income)
print("Расходы:", total_expenses)
print("Остаток:", balance)

# Проверяем состояние бюджета
if balance >= 0:
    print("Вывод: профицит")
else:
    print("Вывод: дефицит")
