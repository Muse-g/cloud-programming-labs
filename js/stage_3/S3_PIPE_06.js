function pipeSafe(...fns) {
  return (x) => {
    let value = x;
    try {
      for (const fn of fns) {
        value = fn(value);
      }
      return { ok: true, value };
    } catch (error) {
      return { ok: false, error };
    }
  };
}

// Test functions
const add2 = (x) => x + 2;
const square = (x) => x * x;
const failIfOdd = (x) => {
  if (x % 2 !== 0) throw new Error("Odd number");
  return x;
};

// Build safe pipeline
const safePipeline = pipeSafe(add2, square, failIfOdd);

console.log(safePipeline(2)); // { ok: true, value: 16 } -> (2+2)^2=16, even
console.log(safePipeline(3)); // { ok: false, error: Error: Odd number } -> (3+2)^2=25, odd
