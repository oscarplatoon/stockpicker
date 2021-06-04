# unfinished challenge.  

def picker(prices):

    buy = 0
    sell = 0
    buy_day = 0
    sell_day = 0
    buy_sell = []
    status = "sold"


    for day, price in enumerate(prices):
        if prices[day] < prices[day + 1] and status == "sold":
            buy = prices[day]
            buy_day = day
            status = "bought"
            buy_sell.append(buy_day)
            print(f"Stock {status} on day {buy_day} at ${prices[day]}")
        elif prices[day] > prices[day + 1] and status == "bought":
            sold = prices[day]
            sell_day = day
            status = "sold"
            buy_sell.append(sell_day)
            print(f"Stock {status} on day {sell_day} at ${prices[day]}")
            print(buy_sell)
            break
        
   
print(picker([17,3,6,9,15,8,6,1,10, 7])) 
