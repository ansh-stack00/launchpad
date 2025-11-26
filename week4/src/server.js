import loadConfig from "./config/index.js";
import initApp from "./loaders/app.js";
import logger from "./utils/loggers.js";

const startServer = async() => {
    try {
        const config = loadConfig();

        // initialize app 
        const app = await initApp()

        // start server 
        app.listen(config.port, () => {
            logger.info(`Server started on port ${config.port}`);
            console.log(`🚀 Server running on http://localhost:${config.port}`);
        });
    } catch(error) {
        logger.error("❌ Failed to start server: " + error.message);
        process.exit(1);
    }
}

startServer();