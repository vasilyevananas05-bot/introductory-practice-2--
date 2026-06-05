#Типы данных:
Команда def (от англ. define) сообщает интерпретатору, что мы создаем новую именованную функцию. 
Параметры внутри скобок — это переменные, в которые попадают данные при вызове функции.
Оператор return завершает выполнение функции и отправляет результат обратно в то место, где функция была вызвана. Без return функция вернет None.

# Все коды были выполнены на компиляторе питон 

# код 1
calculate_profit(). Функция принимает выручку и затраты, возвращает прибыль. Вызвать с тремя разными парами значений.

  
def calculate_profit(revenue, costs):
    return revenue - costs

print(calculate_profit(1000, 700))
print(calculate_profit(5000, 4800))
print(calculate_profit(250, 300))
# код 2
calculate_vat(). Функция принимает цену и ставку НДС (по умолчанию 20%), возвращает сумму налога. Вызвать с явной и стандартной ставкой.


def calculate_vat(price, vat_rate=0.20):
    return price * vat_rate

print(calculate_vat(1000))
print(calculate_vat(1000, 0.10))

# код 3

get_category(). Функция возвращает категорию бизнеса по выручке (микро / малый / средний / крупный). Протестировать на 4 значениях.
  
def get_category(revenue):
    if revenue < 120: return "микро"
    elif revenue < 800: return "малый"
    elif revenue < 2000: return "средний"
    else: return "крупный"

test_values = [50, 500, 1500, 3000]
for v in test_values:
    print(v, "-", get_category(v))
# код 4

compound_interest(). Функция принимает капитал, ставку и срок, возвращает итоговую сумму. Вывести для 3, 5 и 10 лет.



# код 5

apply_discount(). Функция принимает цену и процент скидки, возвращает новую цену. Применить к списку из 5 товаров в цикле.

def apply_discount(price, discount_percent):
    return price * (1 - discount_percent / 100)

prices = [100, 250, 500, 1000, 1500]
for p in prices:
    print(f"Цена со скидкой 15%: {apply_discount(p, 15)}")
# код 6

currency_convert(). Функция принимает сумму, курс и направление ('to_usd' / 'to_rub'), возвращает конвертированную сумму.

def currency_convert(amount, rate, direction):
    if direction == 'to_usd':
        return amount / rate
    elif direction == 'to_rub':
        return amount * rate

print(currency_convert(7000, 70, 'to_usd'))
# код 7

payback_period(). Функция принимает объём инвестиций и годовую прибыль, возвращает срок окупаемости. Обработать случай прибыли ≤ 0

def payback_period(investments, annual_profit):
    if annual_profit <= 0:
        return "Никогда (прибыль нулевая или отрицательная)"
    return investments / annual_profit

print(payback_period(1000000, 250000))
print(payback_period(500000, -100))def format_invoice_line(name, quantity, price):
    total = quantity * price
    return f"{name} x {quantity} = {total} руб."

print(format_invoice_line("Кофе", 2, 250))
print(format_invoice_line("Чай", 1, 150))
print(format_invoice_line("Печенье", 3, 80))
# код 8

format_invoice_line(). Функция принимает название, количество и цену, возвращает строку: «[название] × [кол-во] = [сумма] руб.» Вызвать для 3 позиций


# код 9

get_revenues() + analyze(). Первая функция принимает n и возвращает список из n введённых значений. 
Вторая принимает список и возвращает минимум, максимум и среднее

# код 10

generate_report(). Функция принимает название компании, выручку и затраты, выводит многострочный отчёт: прибыль, рентабельность, вывод (прибыльна / убыточна).
