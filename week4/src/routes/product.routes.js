import { Router } from "express";
import productController from "../controllers/product.controller.js";
import validate from "../middlewares/validation.middleware.js";
import productSchema from "../Schemas/Product.schema.js";



const router = Router()

router.route("/add-product").post(validate(productSchema) ,  productController.create)
router.route("/get-all").get(productController.getAllProducts)
router.route("/:id/get-one").get(productController.getProduct)
router.route("/:id/update-product").put(validate(productSchema) ,productController.updateProduct)
router.route("/:id/delete-product").delete(productController.delete);

export default router;