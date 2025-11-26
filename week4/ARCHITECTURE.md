# PROJECT ARCHITECTURE — DAY 1

## Purpose
Layered Node.js + Express architecture with environment-based config, bootstrapping loaders, logging, and clean folder separation.

## Folder structure
src/
  config/        → environment loader (index.js)
  loaders/       → app.js (Express bootstrap) and db.js (DB init)
  models/        → Mongoose models
  routes/        → route definitions
  controllers/   → request handlers (not yet used in minimal example)
  services/      → business logic
  repositories/  → DB access logic
  middlewares/   → express middlewares
  utils/         → utilities (logger.js)
  jobs/          → cron/jobs
  logs/          → application log files

## Boot process
1. Load configuration from `.env.local` / `.env.dev` / `.env.prod` based on NODE_ENV.
2. Initialize Express (load core middlewares).
3. Initialize database connection.
4. Mount routes under `/api`.
5. Start HTTP server.
6. Log key startup events.

## Key logs (using Winston)
- ✔ Server started on port X
- ✔ Database connected
- ✔ Middlewares loaded
- ✔ Routes mounted: N endpoints

## Files to submit
- src/loaders/app.js
- src/loaders/db.js
- src/utils/logger.js
- src/config/index.js
- ARCHITECTURE.md
