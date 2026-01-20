function flatten1(arr) {
  const result = [];
  for (const item of arr) {
    if (Array.isArray(item)) {
      result.push(...item);
    } else {
      result.push(item);
    }
  }
  return result;
}

// Test
console.log(flatten1([1, [2, 3], [4], 5])); // [1, 2, 3, 4, 5]
