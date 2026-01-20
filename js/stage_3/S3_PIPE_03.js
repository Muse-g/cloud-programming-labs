// Simple pipe implementation
const pipe =
  (...fns) =>
  (x) =>
    fns.reduce((acc, fn) => fn(acc), x);

// Individual steps
const trim = (str) => str.trim();
const toLower = (str) => str.toLowerCase();
const normalizeSpaces = (str) => str.replace(/\s+/g, " ");

// Create normalization pipeline
const normalize = pipe(trim, toLower, normalizeSpaces);

// Test
const text = "   Hello   WORLD   JS  ";
console.log(normalize(text)); // "hello world js"

console.log(normalize("  Multiple   SPACES HERE ")); // "multiple spaces here"
