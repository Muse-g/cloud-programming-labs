function sumNested(matrix) {
  let total = 0;

  for (const row of matrix) {
    for (const n of row) {
      total += n;
    }
  }

  return total;
}

// Test
const matrix = [[1, 2, 3], [4, 5], [6]];

console.log(sumNested(matrix)); // 21
