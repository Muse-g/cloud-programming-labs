// Pipe utility
const pipe =
  (...fns) =>
  (x) =>
    fns.reduce((acc, fn) => fn(acc), x);

// Step 1: Parse lines into objects { level, user }
const parseLines = (lines) =>
  lines.map((line) => {
    const [level, rest] = line.split(": ");
    const userMatch = rest.match(/user=(\d+)/);
    return { level, user: userMatch ? Number(userMatch[1]) : null };
  });

// Step 2: Filter only INFO lines
const filterInfo = (lines) => lines.filter((l) => l.level === "INFO");

// Step 3: Extract user IDs
const extractUserIds = (lines) =>
  lines.map((l) => l.user).filter((u) => u !== null);

// Build the pipeline
const getInfoUserIds = pipe(parseLines, filterInfo, extractUserIds);

// Test
const logLines = [
  "INFO: user=42",
  "ERROR: user=7",
  "INFO: user=15",
  "WARN: user=3",
  "INFO: user=99",
];

console.log(getInfoUserIds(logLines)); // [42, 15, 99]
