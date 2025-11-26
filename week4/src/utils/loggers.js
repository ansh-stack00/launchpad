import winston from "winston";
import fs from "fs";
import path from "path";

// check if logs dir exist or not 
//  resolved to src/logs
const logDir = path.join(process.cwd() , "src","logs")

if(!fs.existsSync(logDir)) {
    fs.mkdirSync(logDir , { recursive:true })
}


const logger = winston.createLogger({
  level: "info",
  format: winston.format.combine(
    winston.format.timestamp({ format: "YYYY-MM-DD HH:mm:ss" }),
    winston.format.printf(({ timestamp, level, message }) => {
      return `${timestamp} [${level.toUpperCase()}] ${message}`;
    })
  ),
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: path.join(logDir, "app.log") })
  ],
});


export default logger ;