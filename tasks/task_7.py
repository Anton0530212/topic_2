"""Программа для расчета стоимости заказа
в интернет-магазине, которая выводит
сообщение о стоимости заказа с учетом скидки"""
cost: int = 1000
discount: int = 20
quantity: int = 3

total_cost = cost * quantity
discount_total = total_cost - (total_cost * discount / 100)

print('Стоимость вашего заказа:', discount_total, 'рублей')
