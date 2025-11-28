import express from "express";
import cors from "cors";
import morgan from "morgan";
import cookieParser from "cookie-parser";
import connectDb from "./db.js";
import logger from "../utils/loggers.js";
import loadConfig from "../config/index.js";
    
// import routes here 
    
import productRoutes from "../routes/product.routes.js"


const initApp = async() => {

    const app = express();

    // load environment variable

    const config = loadConfig();

    logger.info("loading middlewares...");

    app.use(cors({
        origin:"*",
        credentials: true
    }));

    app.use(express.json({limit: "10mb"}));
    app.use(express.urlencoded({
        limit:"10mb",
        extended:true
    }))

    app.use(morgan("dev"));
    app.use(express.static("public"));
    app.use(cookieParser());

    logger.info("middlewares loaded !!")


    logger.info("connecting to database!");
    await connectDb(config.dbURI);
    
    
     // routes declaration
     app.use("/product" , productRoutes)

    // logger.info(`✔ Routes mounted: ${routes.stack.length} endpoints`);


    return app;


}


export default initApp ;