function calc(a, op, b) {
  switch (op) {
    case "+":
      return a + b;
    case "-":
      return a - b;
    case "*":
      return a * b;
    case "/":
      return b !== 0 ? a / b : null;
    default:
      return null;
  }
}

// Test cases
console.log(calc(5, "+", 3)); // 8
console.log(calc(5, "-", 3)); // 2
console.log(calc(5, "*", 3)); // 15
console.log(calc(6, "/", 3)); // 2
console.log(calc(6, "/", 0)); // null
console.log(calc(6, "%", 2)); // null (unsupported op)
