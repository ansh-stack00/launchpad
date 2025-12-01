
import logger from "../utils/loggers.js";
import { uuid } from "zod";

const  tracingMiddleware  = (req, res, next) => {

    const requestId = req.headers["x-request-id"] || uuid();

    req.requestId = requestId;

    // seding back in response 
    res.setHeader("X-Request-ID", requestId);

    req.log = {
        info : (msg) => logger.info(`[${requestId}] ${msg}`),
        error : (msg) => logger.error(`[${requestId}] ${msg}`),
        warn : (msg) => logger.warn(`[${requestId}] ${msg}`)
    }

    next();
}


export default tracingMiddleware;