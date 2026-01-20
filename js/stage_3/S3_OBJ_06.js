function groupBy(items, key) {
  const result = {};

  for (const item of items) {
    const groupKey = item[key];
    if (!(groupKey in result)) {
      result[groupKey] = [];
    }
    result[groupKey].push(item);
  }

  return result;
}

// Test
const users = [
  { name: "Ala", role: "admin" },
  { name: "Beki", role: "user" },
  { name: "Ola", role: "admin" },
];

console.log(groupBy(users, "role"));
/*
  {
    admin: [
      { name: "Ala", role: "admin" },
      { name: "Ola", role: "admin" }
    ],
    user: [
      { name: "Beki", role: "user" }
    ]
  }this in order to create the task naming right.
  */
