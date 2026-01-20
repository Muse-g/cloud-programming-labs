function shippingCost(weightKg, isMember) {
  let cost;

  if (weightKg < 1) cost = 10;
  else if (weightKg <= 5) cost = 20;
  else cost = 30;

  if (isMember) cost *= 0.8; // 20% discount for members

  return cost;
}

// Test cases
console.log(shippingCost(0.5, false)); // 10
console.log(shippingCost(2, false)); // 20
console.log(shippingCost(6, false)); // 30
console.log(shippingCost(2, true)); // 16 (20% off)
console.log(shippingCost(6, true)); // 24
