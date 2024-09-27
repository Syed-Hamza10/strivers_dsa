def sol(prices, money):
    mini = float('inf')
    sec_mini = float('inf')

    for price in prices:
        if price < mini:
            sec_mini = mini
            mini = price
        else:
            sec_mini = min(sec_mini, price)

    price_sum = mini + sec_mini
    return (money - price_sum) if money >= price_sum else money
