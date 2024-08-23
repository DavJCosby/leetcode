/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumAverage = function (nums) {
    const n = nums.length;
    nums.sort(function (a, b) {
      return a - b;
    });
  
    //var averages = [];
    var smallestSoFar = 51; // 50 is the max
    for (i = 0; i < n / 2; i++) {
      const minElement = nums[i];
      const maxElement = nums[n - i - 1];
      const avg = (minElement + maxElement) / 2;
      //averages.push(avg);
      smallestSoFar = Math.min(smallestSoFar, avg)
    }
  };
  
  minimumAverage([1, 2, 3, 4, 5]);  