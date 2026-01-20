function normalizeName(input) {
  return input ? input.trim() : "Anonymous";
}

// Test cases
console.log(normalizeName("")); // "Anonymous"
console.log(normalizeName(" ")); // "" (trimmed space becomes empty string)
console.log(normalizeName(null)); // "Anonymous"
console.log(normalizeName(" Ola ")); // "Ola"
