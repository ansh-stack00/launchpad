const { execSync } = require("child_process");
const fs = require("fs");

const CONCURRENCY_LEVELS = [1, 4, 8]; // adjust if needed
const REPEATS = 5;                    // number of runs per level
const LOG_DIR = "logs";
const OUTPUT_FILE = `${LOG_DIR}/perf-summary.json`;

// helper to take median of an array
function median(arr) {
  const sorted = [...arr].sort((a, b) => a - b);
  return sorted[Math.floor(sorted.length / 2)];
}

// run one benchmark for a given worker count
function runOnce(workers) {
  const start = Date.now();
  execSync(`node wordstat.js ${workers}`, { stdio: "ignore" }); // no console spam
  return Date.now() - start;
}

function runBenchmark(workers) {
  console.log(`\n🚀 Benchmarking with ${workers} worker(s) (${REPEATS} runs)`);

  // warm up (JIT + cache)
  runOnce(workers);

  const times = [];
  for (let i = 0; i < REPEATS; i++) {
    const ms = runOnce(workers);
    console.log(`  Run ${i + 1}: ${ms} ms`);
    times.push(ms);
  }

  const med = median(times);
  console.log(`→ Median: ${med} ms`);
  return { workers, runs: times, median: med };
}

function main() {
  if (!fs.existsSync(LOG_DIR)) fs.mkdirSync(LOG_DIR);
  const results = CONCURRENCY_LEVELS.map(runBenchmark);
  fs.writeFileSync(OUTPUT_FILE, JSON.stringify(results, null, 2));
  console.log(`\n✅ Saved benchmark results → ${OUTPUT_FILE}`);
}

main();
