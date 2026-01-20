function inspect(value) {
  return {
    type: value === null ? "null" : typeof value,
    isArray: Array.isArray(value),
    isNull: value === null,
    isNaN: typeof value === "number" && Number.isNaN(value),
  };
}

// Test cases
const values = [null, [], {}, 42, NaN, "hello", true, () => {}];

values.forEach((v) => console.log(inspect(v)));
