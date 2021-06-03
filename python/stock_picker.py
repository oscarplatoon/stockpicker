# reverse the order of PRICES
# input is a list of PRICES, newest day's
# prices are lower indices
# The best day to buy must be before the
# best day to sell
# Starting at the end of the array, store that BUY_INDICE
# store the SELL_INDICE and DIFF between the first newer element that is less than the first elem
# loop through the array comparing PRICES[INDICE] to each
# newer day. if that comparison is > DIFF, store that SELL_INDICE and DIFF
# repeat until you reach index 1


def picker(prices):
    buy_indice = len(prices) - 1
    sell_indice = None
    diff = -1
    i = buy_indice - 1
    j = buy_indice
 
    while j > 0:
        while i >= 0:
            temp_diff = prices[j] - prices[i]
            #print(temp_diff)
            if (temp_diff > 0 and temp_diff > diff):
                diff = temp_diff
                sell_indice = i
                buy_indice = j
            i -= 1
        j -= 1
        i = j - 1

    return [sell_indice, buy_indice]

