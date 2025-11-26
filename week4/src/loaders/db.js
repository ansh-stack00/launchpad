import mongoose from "mongoose";
import logger from "../utils/loggers";

const connectDb = async (dbURI) => {

     if (!dbURI) {
        logger.error(" No DATABASE_URI provided in config");
        throw new Error("DATABASE_URI not provided");
    }

    try {

        const connectionInstance = await mongoose.connect(dbURI);
        console.log("Database connected succesfully 🥳🥳",connectionInstance.connection.host) ;
        logger.info("Database connected succesfully 🥳🥳")
    }
    catch(error ) {
        
        logger.error("database connection error 😕")
        process.exit(1);
    }
}

export default connectDb;