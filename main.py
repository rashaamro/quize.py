# Q1 ------
def discount(price, is_member):
    if is_member == True:
        discount = price * 0.10
        discounted_price = price - discount
        return discounted_price
    else:
        return 0


print("Discounted Amount is :", discount(100, True))

# Q2----------
def difference(list):

    max_number = max(list)
    min_number = min(list)

    difference = max_number - min_number
    return difference



print("Difference is :", difference([4,10,5,2,8]))

