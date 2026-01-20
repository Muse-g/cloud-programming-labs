// S1_VAR_02 — Block scope checking if it is bounded and canot escape out of its block

try {
  {
    let x = 10;
  }
  console.log(x);
} catch (e) {
  console.log("let variable is not accessible outside block");
}

{
  var y = 20;
}
console.log("var variable outside block:", y);

// the following are scoped properly
// let is block-scoped; var is function-scoped.
