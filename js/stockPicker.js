exports.picker = function (prices) {
  /**
   * Define a function which receives an array, evaluates it for greatest difference from left
   * to right, and returns the paired indices which give the greatest difference.
   * 
   * There are two null cases, one if the argument array is in reverse order, the other if
   * there is only one element in the array.
   */

  // First edge case, only one or less items in argument array:
  resultArr = [];
  if (prices.length <= 1) {
    return resultArr
  }
  let maxDiff = -1;

  for (let i = 0; i < prices.length; i++) {
    for (let j = i + 1; j < prices.length; j++) {
      if(prices[i] < prices[j] && maxDiff < (prices[j] - prices[i])) {
        maxDiff = prices[j] - prices[i]
        //set our output of best indices to new max difference indices.
        resultArr[0] = i
        resultArr[1] = j
      } 
    } 
  }
  if (maxDiff == -1) {
  return ("No profitable pick in range.")
  } else 
  return resultArr 
}