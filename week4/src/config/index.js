import dotenv from "dotenv";
import path from "path";



export default function loadConfig() {

    const env = process.env.NODE_ENV || "local"

    const envFile = {
        local : ".env.local",
        dev : ".env.dev",
        prod : ".env.prod"
    }[env] || ".env.local"

    // resolving path for dotenv
    const resolvedPath = path.resolve(process.cwd() , envFile); 

    dotenv.config({
        path:resolvedPath
    })

    return {
        env ,
        port : process.env.PORT ? Number(process.env.PORT) : 8080,
        dbURI: process.env.DATABASE_URI || ""
    }
}

