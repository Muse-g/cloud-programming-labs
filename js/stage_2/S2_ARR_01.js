function cleanNumbers(arr) {
  return arr.map((s) => +s.trim()).filter((n) => !Number.isNaN(n));
}

// Test
console.log(cleanNumbers([" 1 ", "x", "2"])); // [1, 2]
