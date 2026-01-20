function safeAdd(a, b) {
  const isSafeInt = Number.isSafeInteger(a) && Number.isSafeInteger(b);

  if (!isSafeInt) {
    const result = BigInt(a) + BigInt(b);
    console.log("BigInt");
    return result;
  } else {
    const result = a + b;
    console.log("Number");
    return result;
  }
}

// Test cases
console.log(safeAdd(10, 20)); // Number, 30
console.log(safeAdd(Number.MAX_SAFE_INTEGER, 1)); // BigInt, 9007199254740992n
console.log(safeAdd(123, 456)); // Number, 579
console.log(safeAdd(9007199254740991, 9007199254740991)); // BigInt
