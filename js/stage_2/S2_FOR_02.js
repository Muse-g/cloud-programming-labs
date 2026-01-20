function findFirstEven(nums) {
  for (const n of nums) {
    if (n % 2 === 0) return n;
  }
  return null;
}

// Test
console.log(findFirstEven([1, 3, 5, 4, 6])); // 4
console.log(findFirstEven([1, 3, 5])); // null
