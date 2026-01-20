function typeLabel(value) {
  return value === null ? "null" : typeof value;
}

// Test cases
console.log(typeLabel(null)); // "null"
console.log(typeLabel(undefined)); // "undefined"
console.log(typeLabel(42)); // "number"
console.log(typeLabel("42")); // "string"
console.log(typeLabel(true)); // "boolean"
console.log(typeLabel({})); // "object"
console.log(typeLabel([])); // "object"
console.log(typeLabel(() => {})); // "function"
