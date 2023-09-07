cost = 1000
discount = 20
quantity = 3


total_cost = cost * quantity
discount_total = total_cost - (total_cost * discount / 100)

print('Стоимость вашего заказа:', discount_total, 'рублей')
