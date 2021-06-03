def picker(prices):
    prices2 = prices [:]
    highest_profit = 0
    days = []
    for i, num1 in enumerate(prices):
        prices2.remove(num1)
        for j, num2 in enumerate(prices2):
            if num2 - num1 > highest_profit:
                highest_profit = num2 - num1
                days = (i,(j+i+1))
    
    return(days)



        
picker([10,5,5,3,2,0])