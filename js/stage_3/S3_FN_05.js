// Higher-order function
const atLeast = (min) => (n) => n >= min;

// Test array
const nums = [1, 3, 5, 7, 9];

// Filter using the predicate
const filtered = nums.filter(atLeast(5));

console.log(filtered); // [5, 7, 9]
