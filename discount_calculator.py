def apply_discount(price, discount):
    

    type_price = type(price)
    type_discount = type(discount)
    if type(price) not in [int, float]:
        return'The price should be a number'
    
    if type(discount) not in [int, float]:
        return 'The discount should be a number'

    if price <= 0:
        return'The price should be greater than 0'
    
    if discount < 0 or discount > 100:
        return'The discount should be between 0 and 100'
    
    new_discount = (discount/100) * price
    final_price = price - new_discount
    return final_price
    

print(apply_discount(100, 20))
apply_discount(200, 50)
apply_discount(50, 0)
apply_discount(50, 100)
apply_discount(74.5, 20.0)