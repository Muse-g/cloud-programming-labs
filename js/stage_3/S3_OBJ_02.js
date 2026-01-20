function mergeDefaults(defaults, overrides) {
  return { ...defaults, ...overrides };
}

// Test
const defaults = { host: "localhost", port: 80, debug: false };
const overrides = { port: 8080, debug: true };

const result = mergeDefaults(defaults, overrides);
console.log(result);
// { host: 'localhost', port: 8080, debug: true }

// Ensure inputs are not mutated
console.log(defaults); // { host: 'localhost', port: 80, debug: false }
console.log(overrides); // { port: 8080, debug: true }
