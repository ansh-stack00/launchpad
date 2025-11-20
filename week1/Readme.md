# 🚀 5-Day Backend Engineering Bootcamp — Progress Log

This repository contains my daily logs from a 5-day learning sprint focused on backend fundamentals, Node.js, Git, APIs, and automation. Each day documents **what I learned** and **what challenges I faced**, along with the core concepts I practiced.

---

## 📅 DAY 1 — System Reverse Engineering + Node & Terminal Fundamentals

### ✅ What I Learned
- **Buffer vs Stream**  
  - *Buffer*: Loads all data at once — suitable for small files (e.g., downloading an entire video).  
  - *Stream*: Processes data in chunks — better for large files (like YouTube video streaming).
- **Node.js File System Basics**  
  - `fs.readFile()` → async, uses buffer  
  - `fs.readFileSync()` → sync, blocking, uses buffer  
  - `fs.createReadStream()` → async, uses streams for chunked reading

### ❗ What Went Wrong
- Had issues reading data using streams at first because the output was incorrect — fixed after debugging.

---

## 📅 DAY 2 — Node CLI App, Concurrency & Large Data Processing

### ✅ What I Learned
- **Asynchronous Programming**  
  Enables multiple tasks to run without blocking one another.
- **Building a Custom CLI Tool**  
  Created `wordstat.js` and learned how CLI commands interact with the system.
- **Concurrency in JavaScript**  
  Non-blocking operations allow efficient task switching.  
  Used `Promise.all()` for parallel execution.
- **Performance Measurement**  
  Used `Date.now()` for benchmarking.
- **Worker Threads**  
  Helpful for CPU-heavy tasks (like Fibonacci calculations) without slowing down the main event loop.

### ❗ What Went Wrong
- Faced challenges in writing concurrent code and splitting data into chunks.

---

## 📅 DAY 3 — Git Essentials: Reset, Revert, Cherry-pick, Bisect, Stash

### ✅ What I Learned
- **git bisect** → Helps identify which commit introduced a bug.  
- **git reset**  
  - Used when you want to adjust commits before finalizing.  
  - `--soft` keeps changes; `--hard` discards commit + changes.
- **git revert** → Safely undoes changes by creating a new commit.  
- **git stash** → Temporarily stores changes when switching tasks.  
- **git pull** → Gets updated changes from the remote repository.  
- **Merge Conflicts** → Practiced merging and resolving conflicts.

### ❗ What Went Wrong
- Initially struggled with `git bisect`, but fixed it after some trial.

---

## 📅 DAY 4 — HTTP / API Forensics (Curl, Postman, Headers)

### ✅ What I Learned
- **Traceroute** → Shows the path your data takes to reach a server.
- **Verbose Mode (-v)** → Gives detailed request/response information.
- **User-Agent** → Identifies the client making the request.
- **ETag & Caching**  
  - ETag helps determine if the cached version is still valid.  
  - If data isn't changed, server returns **304 Not Modified**.
- **Pagination** → Used `limit` and `skip` to fetch large datasets in smaller chunks.
- **HTTP Headers** → Includes metadata such as content type, caching rules, and authentication.

### ❗ What Went Wrong
- Nothing major — mostly theoretical and tool-based tasks.

---

## 📅 DAY 5 — Automation & Mini CI Pipeline

### ✅ What I Learned
- **ESLint** → Detects syntax and logical issues.
- **Prettier** → Ensures consistent code formatting.
- **Checksum** → Used to verify data integrity.
- **Cron Jobs** → Help automate tasks on a schedule.
- **Husky**  
  - Added Git hooks to run ESLint & Prettier before commit.  
  - Prevents poorly formatted or error-prone code from being committed.

### ❗ What Went Wrong
- Faced issues while setting up Husky for the first time.

---

## 🏁 Final Thoughts
This 5-day sprint strengthened my backend fundamentals—ranging from Node.js internals and concurrency to Git workflows, HTTP forensics, and automation tools. It was a solid foundation-building journey that will help me in upcoming projects.

