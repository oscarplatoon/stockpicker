def picker(prices):
    
    #empty list return empty list
    if prices == []:
        return []
    else:
        #initialize variables
        potential_buy = prices[0]
        profit = 0
        buy_idx = 0
        sell_idx = 1

        for i in range(1,len(prices)-1):
            #compare for lower price
            if prices[i] < potential_buy:
                #set new potential buy value and set buy_idx to i for output later
                potential_buy = prices[i]
                buy_idx = i
                #enter inner range loop to look for sell idx
            for j in range(i + 1,len(prices)):
                #calc temp profit to compare saved profit to
                temp = prices[j] - potential_buy
                #if temp profit greater reassign and save sell_idx
                if temp > profit:
                    profit = temp
                    sell_idx = j
                #idx comparison to make sure we buy before we sell
            if buy_idx < sell_idx:
                output = [buy_idx, sell_idx]

    return output