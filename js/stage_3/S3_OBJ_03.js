function pick(obj, keys) {
  const result = {};
  for (const key of keys) {
    if (key in obj) {
      result[key] = obj[key];
    }
  }
  return result;
}

// Test
const user = { id: 1, name: "Ala", age: 30 };
console.log(pick(user, ["id", "name"])); // { id: 1, name: "Ala" }
console.log(pick(user, ["age", "email"])); // { age: 30 }
console.log(pick(user, ["email"])); // {}
