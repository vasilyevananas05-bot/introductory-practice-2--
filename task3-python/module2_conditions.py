#Теория: Условные конструкции и циклы
Условный оператор (if, elif, else)
Используется, когда программе нужно сделать выбор.
if (если): Проверяет условие. Если оно истинно (True), выполняется блок кода под ним.
elif (иначе если): Проверяется, если предыдущее условие if оказалось ложным. Таких блоков может быть много.
else (иначе): Выполняется, если ни одно из условий выше не подошло.
Цикл for
Используется для повторения действий определенное количество раз.
Чаще всего применяется с функцией range(n), которая создает последовательность чисел от 0 до n−1n - 1n−1.
Например, for i in range(5): выполнит код внутри 5 раз.

Критерий	if	for
Основная функция	Условное ветвление — выбор блока кода в зависимости от условия	Повторение блока кода определённое количество раз или перебор элементов
Синтаксис	if условие:, блок кода с отступом	for элемент in последовательность:, блок кода
Применение	Выбор действий при выполнении или невыполнении условия	Перебор элементов, выполнение действий определённое количество раз 

# все коды выполнялись в компиляторе питон

# код 1
profit = float(input("Введите прибыль или убыток: "))

if profit > 0:
    print("Результат: Прибыль")
elif profit < 0:
    print("Результат: Убыток")
else:
    print("Результат: Безубыточность")
# код 2
revenue = float(input("КАкая ваша выручка за год?: "))

if revenue <= 1000000:
    print("Категория: Микробизнес")
elif revenue <= 10000000:
    print("Категория: Малый бизнес")
elif revenue <= 100000000:
    print("Категория: Средний бизнес")
else:
    print("Категория: Крупный бизнес")
# код 3
salary = float(input("Введите сумму ЗП: "))

if salary <= 50000:
    tax_rate = 0.13
else:
    tax_rate = 0.15

tax = salary * tax_rate
take_home = salary - tax

print(f"Налог: {tax} руб.")
print(f"На руки: {take_home} руб.")
# код 4
rate = float(input("Введите процентную ставку: "))

for i in range(1, 13):
    result = rate * i
    print(f"Ставка × {i} = {result}")
# код 5
prices = [150.0, 450.5, 299.9, 1000.0, 50.0]

for price in prices:
    if price > 300:
        print(f"Цена {price} — ДОРОГО")
    else:
        print(f"Цена {price} — Приемлемо")
# код 6
capital = float(input("Начальный капитал: "))
rate = float(input("Процентная ставка (%): "))

for year in range(1, 6):
    capital = capital * (1 + rate / 100)
    print(f"Год {year}: на счету {round(capital, 2)}")
# код 7
monthly_payment = float(input("Ежемесячный взнос: "))
months = int(input("Количество месяцев: "))
total = 0

for m in range(1, months + 1):
    total += monthly_payment
    print(f"Месяц {m}: накоплено {total}")
# код 8
budget = float(input("Ваш бюджет: "))
# Список из 5 товаров (название и цена)
catalog = {"Товар А": 500, "Товар Б": 2000, "Товар В": 100, "Товар Г": 1500, "Товар Д": 300}

for item, price in catalog.items():
    if budget >= price:
        print(f"{item} (цена {price}): доступен")
    else:
        diff = price - budget
        print(f"{item} (цена {price}): не хватает {diff} руб.")
# код 9
revenues = []
for i in range(1, 7):
    rev = float(input(f"Введите выручку за месяц {i}: "))
    revenues.append(rev)

print(f"Максимум: {max(revenues)}")
print(f"Минимум: {min(revenues)}")
print(f"Среднее: {sum(revenues) / len(revenues)}")
# код 10
threshold = float(input("Введите пороговую рентабельность (%): "))
count_above = 0

for i in range(1, 7):
    val = float(input(f"Рентабельность за месяц {i} (%): "))
    if val > threshold:
        count_above += 1

print(f"Месяцев выше порога: {count_above}")
