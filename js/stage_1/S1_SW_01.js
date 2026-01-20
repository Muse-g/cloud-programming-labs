function dayName(n) {
  switch (n) {
    case 1:
      return "Monday";
    case 2:
      return "Tuesday";
    case 3:
      return "Wednesday";
    case 4:
      return "Thursday";
    case 5:
      return "Friday";
    case 6:
      return "Saturday";
    case 7:
      return "Sunday";
    default:
      return null;
  }
}

// Test cases
console.log(dayName(1)); // "Monday"
console.log(dayName(5)); // "Friday"
console.log(dayName(7)); // "Sunday"
console.log(dayName(8)); // null
