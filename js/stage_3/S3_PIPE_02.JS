function compose(...fns) {
  return (x) => fns.reduceRight((acc, fn) => fn(acc), x);
}

// Test functions
const add2 = (x) => x + 2;
const square = (x) => x * x;
const half = (x) => x / 2;

// Create a composition (right-to-left)
const composed = compose(half, square, add2);

console.log(composed(4)); // half(square(add2(4))) = half(square(6)) = half(36) = 18
console.log(composed(2)); // half(square(add2(2))) = half(square(4)) = half(16) = 8
