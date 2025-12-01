import helmet from "helmet";
import rateLimit from "express-rate-limit";
import cors from "cors";
import hpp from "hpp";

const applySecurity = (app) => {
  
  app.use(helmet());

  app.use(hpp());
  
  app.use(
    cors({
      origin: "*", 
      credentials: true,
    })
  );

  
  const limiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 1, 
    message: "Too many requests from this IP, please try again later",
  });

  app.use(limiter);

};

export default applySecurity
