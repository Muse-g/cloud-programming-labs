//this code works only in modern js, node20+ ,be cautius if you got eror while running in lower node versions.
function get(obj, path, fallback) {
  const keys = path.split(".");
  let current = obj;

  for (const key of keys) {
    if (current == null || typeof current !== "object") return fallback;
    current = current[key];
    if (current === undefined) return fallback;
  }

  return current;
}

// Test
const data = { a: { b: { c: 42 } } };

console.log(get(data, "a.b.c", null)); // 42
console.log(get(data, "a.b.x", "N/A")); // "N/A"
console.log(get(data, "a.b.c.d", 0)); // 0
console.log(get(data, "a", "missing")); // { b: { c: 42 } }
