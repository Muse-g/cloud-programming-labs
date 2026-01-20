function grade(score) {
  if (score < 0 || score > 100) return null;
  if (score >= 90) return "A";
  if (score >= 80) return "B";
  if (score >= 70) return "C";
  if (score >= 60) return "D";
  return "F";
}

// Test cases
console.log(grade(95)); // "A"
console.log(grade(85)); // "B"
console.log(grade(72)); // "C"
console.log(grade(60)); // "D"
console.log(grade(50)); // "F"
console.log(grade(-5)); // null
console.log(grade(105)); // null
