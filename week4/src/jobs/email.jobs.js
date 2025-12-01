import { Queue , Worker } from "bullmq";
import sendEmail from "../utils/emailSender.js";
import  { Redis } from "ioredis";
import logger from "../utils/loggers.js";


const connection = new Redis({
    host: process.env.REDIS_HOST,
    port: process.env.REDIS_PORT,
    maxRetriesPerRequest: null,   
    enableReadyCheck: false       
});

// creating an email queue 
const emailQueue = new Queue('emailQueue' , { connection });


// adding a job in queue

async function addEmailJob(data) {
  await emailQueue.add("sendEmail", data, {
    attempts: 5,  
    backoff: {
      type: "exponential",
      delay: 5000, 
    },
    removeOnComplete: true,
    removeOnFail: false,
  });
}


// worker to process jobs 

const emailWorker = new Worker(
  "emailQueue",
  async (job) => {
    console.log(`Processing job ${job.id} - sending email to ${job.data.to}`);
    await sendEmail(job.data);
  },
  { connection }
);

emailWorker.on("completed", (job) => {
  console.log(`Job ${job.id} completed`);
  logger.info(`Job ${job.id} completed`);
});

emailWorker.on("failed", (job, err) => {
  console.error(`Job ${job.id} failed: ${err.message}`) ; 
  logger.warn(`Job ${job.id} failed: ${err.message}`) ;
});

export default addEmailJob