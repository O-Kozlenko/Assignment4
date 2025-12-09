
def process_prices(prices, discount_percent):
    if prices>0:
        total=prices*(1-(discount_percent/100))
        round(total)
        return total
    else:
        return("Error")
old_prices=[1000, -50, 300, 0, 500]
for i in range(len(old_prices)):
    print(process_prices(old_prices[i],20),end=' ')
