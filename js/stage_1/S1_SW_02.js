function runCommand(cmd) {
  switch (cmd) {
    case "start":
      return "System starting...";
    case "stop":
      return "System stopping...";
    case "status":
      return "System status: OK";
    default:
      return "Unknown command";
  }
}

// Test cases
console.log(runCommand("start")); // "System starting..."
console.log(runCommand("stop")); // "System stopping..."
console.log(runCommand("status")); // "System status: OK"
console.log(runCommand("restart")); // "Unknown command"
