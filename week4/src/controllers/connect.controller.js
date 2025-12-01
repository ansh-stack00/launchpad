import asyncHandler from "../utils/asyncHandler.js";
import ApiResponse from "../utils/apiResponse.js";
import addEmailJob from "../jobs/email.jobs.js";
import logger from "../utils/loggers.js";

class ConnectUser {

    userConnect = asyncHandler(async (req, res) => {

        logger.info("Adding email job for new connected user...");

        await addEmailJob({
            to: "anshagrawal181@gmail.com",     
            subject: "New User Connected",
            text: "A user just connected to your application.",
            html: "<p>A new user connected 🔥</p>",
        });

        logger.info("Email job added successfully.");

        return res
            .status(201)
            .json(new ApiResponse(201, "Email job queued successfully"));
    });
}

export default new ConnectUser();
