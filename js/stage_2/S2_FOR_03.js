function sumUntil(nums, threshold) {
  let sum = 0;

  for (const n of nums) {
    if (sum + n > threshold) break;
    sum += n;
  }

  return sum;
}

// Test
console.log(sumUntil([1, 2, 3, 4, 5], 7)); // 6 (1 + 2 + 3)
console.log(sumUntil([5, 5, 5], 9)); // 5
