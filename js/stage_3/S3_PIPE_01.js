function pipe(...fns) {
  return (x) => fns.reduce((acc, fn) => fn(acc), x);
}

// Test functions
const add2 = (x) => x + 2;
const square = (x) => x * x;
const half = (x) => x / 2;

// Create a pipeline
const pipeline = pipe(add2, square, half);

console.log(pipeline(4)); // ((4 + 2) ^ 2) / 2 = 18
console.log(pipeline(2)); // ((2 + 2) ^ 2) / 2 = 8
