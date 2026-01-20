// Original functions (example)function, square(n) { return n * n; }
// function isOdd(n) { return n % 2 !== 0; }, function greet(name) { return "Hello " + name; }

// Arrow function versions
const square = (n) => n * n;
const isOdd = (n) => n % 2 !== 0;
const greet = (name) => `Hello ${name}`;

// Tests we done to make sure it works
console.log(square(5)); // 25
console.log(isOdd(5)); // true
console.log(isOdd(4)); // false
console.log(greet("Ala")); // "Hello Ala"
// added this comment to re order the sequence on the commit history
