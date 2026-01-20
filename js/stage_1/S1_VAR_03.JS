const user = { name: "Ala", tags: [] };

// Push two tags
user.tags.push("developer", "blogger");

// Print final object
console.log(user);
//LETS TRY TO ASSIGN IT TO {}
try {
  // Attempt to reassign const
  user = {};
} catch (err) {
  console.log("Error:", err.message);
}
