const people = [
  { name: "Ala", age: 30 },
  { name: "Beki", age: 25 },
  { name: "Ola", age: 35 },
];

// Sort by age ascending
people.sort((a, b) => a.age - b.age);

console.log(people);
/*
  [
    { name: 'Beki', age: 25 },
    { name: 'Ala', age: 30 },
    { name: 'Ola', age: 35 }
  ]
  */
