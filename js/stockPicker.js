const picker = (prices) => {
  // set buy and sell variables
  let buy = 0
  let sell = 0
  // set a result varriable as an array of [buyIndex, sellIndex]
  let buyIndex = undefined,
     sellIndex = undefined,
     result = [buyIndex,sellIndex]
  // loop through prices
  prices.array.forEach((element, index) => {
    // compare low's and highs
    if (buy < element) {
      buy = element
      buyIndex = index
    }
    if(element > sell) {
      sell = element
      sellIndex = index
    }
  });
  return result
}


console.log(picker([17,3,6,9,15,8,6,1,10]))