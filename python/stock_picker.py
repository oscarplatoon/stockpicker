def picker(prices):
    #Create Output array with best profit
    best_profit_prices = [0,0]
    best_profit = 0
    # for loop to increment between
    for i, buy_price in enumerate(prices):
        for j in range(i+1,len(prices)):
            if (prices[j]-buy_price>best_profit):
                best_profit = prices[j]-buy_price  
                best_profit_prices = [i,j]

    return best_profit_prices
picker([3,17,6,9,18,15,6,1,10])