const nums = [1, 2, 3, 4, 5];

// Sum of squares of even numbers
const sumOfSquares = nums
  .filter((n) => n % 2 === 0) // to keep even numbers
  .map((n) => n * n) // then tosquare each
  .reduce((acc, n) => acc + n, 0); // calculating suum

console.log(sumOfSquares); // 20 (2² + 4²)
