def picker(prices):
    high = 0
    for i,price in enumerate(prices):
        for x in range(i+1,len(prices)):
            if(prices[x]-price) > high:
                high = prices[x]-price
                answer = [i,x]
    return(answer)

