function unique(values) {
  const result = [];
  for (const v of values) {
    if (!result.includes(v)) result.push(v);
  }
  return result;
}
//
// Test
console.log(unique([1, 2, 1, 3, 2, 4])); // [1, 2, 3, 4]
console.log(unique(["a", "b", "a", "c"])); // ["a", "b", "c"]
