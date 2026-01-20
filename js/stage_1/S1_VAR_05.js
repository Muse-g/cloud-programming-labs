function isArray(value) {
  return Array.isArray(value);
}

// Test cases
console.log(isArray([])); // true
console.log(isArray([1, 2, 3])); // true
console.log(isArray({})); // false
console.log(isArray({ a: 1 })); // false
console.log(isArray("string")); // false
console.log(isArray(null)); // false
