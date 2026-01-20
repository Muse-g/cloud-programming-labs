// Pipe implementation
const pipe =
  (...fns) =>
  (x) =>
    fns.reduce((acc, fn) => fn(acc), x);

// Pipeline steps
const filterValidNumbers = (arr) => arr.filter((x) => !Number.isNaN(+x));
const toNumbers = (arr) => arr.map((x) => +x);
const doubleValues = (arr) => arr.map((x) => x * 2);
const sumArray = (arr) => arr.reduce((acc, x) => acc + x, 0);

// Build the pipeline
const processNumbers = pipe(
  filterValidNumbers,
  toNumbers,
  doubleValues,
  sumArray
);

// Test
const input = ["1", "2", "x", "3", "4.5", "abc"];
console.log(processNumbers(input)); // (1+2+3+4.5) *2 = 20

const input2 = ["10", "5", "foo"];
console.log(processNumbers(input2)); // (10+5)*2 = 30
