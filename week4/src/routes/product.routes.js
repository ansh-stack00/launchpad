import { Router } from "express";
import productController from "../controllers/product.controller.js";



const router = Router()

router.route("/add-product").post(productController.create)
router.route("/get-all").get(productController.getAllProducts)
router.route("/:id/get-one").get(productController.getProduct)
router.route("/:id/update-product").put(productController.updateProduct)
router.route("/:id/delete-product").delete(productController.delete);

export default router;