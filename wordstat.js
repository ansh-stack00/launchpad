const fs = require("fs");
const path = require("path");
const { Worker } = require("worker_threads");

const FILE = "corpus.txt";   // input file
const WORKERS = 4;           // number of workers to use
const TOP_N = 10;            // top N frequent words
const OUT = "output/stats.json"; // where to save final stats

// splitting text into equal chunks 
function splitText(text, numParts) {
  const size = Math.ceil(text.length / numParts);
  const parts = [];
  for (let i = 0; i < text.length; i += size) {
    parts.push(text.slice(i, i + size));
  }
  return parts;
}

// Running  one worker and return its result
function runWorker(chunk, topN) {
  return new Promise((resolve, reject) => {
    const worker = new Worker(path.join(__dirname, "worker.js"), {
      workerData: { text: chunk, topN },
    });
    worker.on("message", resolve);
    worker.on("error", reject);
  });
}

// Combine results from all workers
function mergeResults(results) {
  const totalCounts = {};
  let totalWords = 0;
  let longestWord = "";
  let shortestWord = null;

  for (const res of results) {
    totalWords += res.totalWords;
    for (const [word, count] of Object.entries(res.topWords.reduce((acc, w) => {
      acc[w.word] = (acc[w.word] || 0) + w.count;
      return acc;
    }, {}))) {
      totalCounts[word] = (totalCounts[word] || 0) + count;
    }

    if (res.longestWord.length > longestWord.length) longestWord = res.longestWord;
    if (!shortestWord || res.shortestWord.length < shortestWord.length)
      shortestWord = res.shortestWord;
  }

  const topWords = Object.entries(totalCounts)
    .sort((a, b) => b[1] - a[1])
    .slice(0, TOP_N)
    .map(([word, count]) => ({ word, count }));

  return {
    totalWords,
    uniqueWords: Object.keys(totalCounts).length,
    longestWord,
    shortestWord,
    topWords,
  };
}

// Main function
async function main() {
  console.log("Reading file...");
  const text = fs.readFileSync(FILE, "utf8");

  console.log(` Splitting into ${WORKERS} chunks...`);
  const chunks = splitText(text, WORKERS);

  console.log(` Starting ${WORKERS} workers...`);
  const start = Date.now();
  const results = await Promise.all(chunks.map((chunk) => runWorker(chunk, TOP_N)));

  const finalStats = mergeResults(results);
  const timeTaken = Date.now() - start;

  fs.mkdirSync("output", { recursive: true });
  fs.writeFileSync(OUT, JSON.stringify({ ...finalStats, timeTaken }, null, 2));

  console.log(`Done in ${timeTaken} ms`);
  console.log("Results saved to:", OUT);
  console.log(finalStats);
}

// Run main
main().catch(console.error);
