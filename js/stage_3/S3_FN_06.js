function mapValues(obj, fn) {
  const result = {};
  for (const [key, value] of Object.entries(obj)) {
    result[key] = fn(value);
  }
  return result;
}

// Test
const data = { a: 1, b: 2, c: 3 };
const squared = mapValues(data, (x) => x * x);

console.log(squared); // { a: 1, b: 4, c: 9 }
console.log(data); // original object remains unchanged
