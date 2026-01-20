function countOccurrences(values) {
  const counts = {};

  for (const v of values) {
    counts[v] = (counts[v] || 0) + 1;
  }

  return counts;
}

// Test
console.log(countOccurrences(["a", "b", "a", "c", "b", "a"]));
// { a: 3, b: 2, c: 1 }

console.log(countOccurrences([1, 2, 1, 1]));
// { '1': 3, '2': 1 }
