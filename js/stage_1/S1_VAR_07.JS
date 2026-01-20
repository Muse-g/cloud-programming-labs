function toNumberOrNull(x) {
  const n = +x; // Unary plus converts to number
  return typeof x === "string" && !Number.isNaN(n) ? n : null;
}

// Test cases
console.log(toNumberOrNull("12")); // 12
console.log(toNumberOrNull("12.5")); // 12.5
console.log(toNumberOrNull(" 12 ")); // 12
console.log(toNumberOrNull("12x")); // null
console.log(toNumberOrNull("")); // 0
