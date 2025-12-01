import { Route, Router } from "express";
import connectController from "../controllers/connect.controller.js";

const router = Router();

router.route("/").get(connectController.userConnect)

export default router;