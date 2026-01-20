function stats(nums) {
  if (nums.length === 0) return null;

  let min = nums[0];
  let max = nums[0];
  let sum = 0;

  for (const n of nums) {
    if (n < min) min = n;
    if (n > max) max = n;
    sum += n;
  }

  return {
    min,
    max,
    avg: sum / nums.length,
  };
}

// Test
console.log(stats([1, 2, 3, 4, 5]));
// { min: 1, max: 5, avg: 3 }

console.log(stats([])); // null
