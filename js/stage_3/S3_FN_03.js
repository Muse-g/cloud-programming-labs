function makeAdder(x) {
  return (y) => x + y;
}

// Test
const add5 = makeAdder(5);
console.log(add5(10)); // 15

const add20 = makeAdder(20);
console.log(add20(7)); // 27
