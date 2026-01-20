function activeUserNames(users) {
  return users
    .filter((u) => u.active)
    .map((u) => u.name.toUpperCase())
    .sort();
}

// Test
const users = [
  { id: 1, name: "Ala", active: true },
  { id: 2, name: "Beki", active: false },
  { id: 3, name: "Ola", active: true },
];

console.log(activeUserNames(users)); // ["ALA", "OLA"]
