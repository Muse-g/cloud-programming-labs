function invert(obj) {
  const result = {};

  for (const [key, value] of Object.entries(obj)) {
    if (result[value] === undefined) {
      result[value] = key;
    } else if (Array.isArray(result[value])) {
      result[value].push(key);
    } else {
      result[value] = [result[value], key];
    }
  }

  return result;
}

// Test
const data1 = { a: 1, b: 2, c: 1 };
console.log(invert(data1));
// { '1': ['a', 'c'], '2': 'b' }

const data2 = { x: "foo", y: "bar", z: "foo" };
console.log(invert(data2));
// { foo: ['x', 'z'], bar: 'y' }
