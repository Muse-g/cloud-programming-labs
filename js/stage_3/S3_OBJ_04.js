function omit(obj, keys) {
  const result = {};
  for (const key in obj) {
    if (!keys.includes(key)) {
      result[key] = obj[key];
    }
  }
  return result;
}

// Test
const user = { id: 1, name: "Ala", age: 30 };
console.log(omit(user, ["age"])); // { id: 1, name: "Ala" }
console.log(omit(user, ["id", "name"])); // { age: 30 }
console.log(omit(user, ["email"])); // { id: 1, name: "Ala", age: 30 }
