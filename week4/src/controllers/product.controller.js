import productService from "../services/product.service.js";
import logger from "../utils/loggers.js";
import asyncHandler from "../utils/asyncHandler.js";
import ApiError from "../utils/apiError.js";
import ApiResponse from "../utils/apiResponse.js";

class ProductController {

    constructor () {
        this.productService = productService
    }

    // endpoint for creating a new product 

    create = asyncHandler( async(req , res) => {
        
        const {prdName , price , description , tags , status } = req.body;

        if(
            [ prdName , price , description ].some((field) => field?.trim === "")
        ){
            throw new ApiError(400 , "all field are required");
        }

        const productData = {
            prdName,
            price,
            description,
            tags: tags || [], 
            status: status || 'pending', 
        }
        const product = await this.productService.create(productData);

        if(!product) {
            throw new ApiError(500 , "something went wrong while creating a product ");
        }

        logger.info(`Product created successfully with ID: ${product._id}`);

        return res
        .status(200)
        .json(
            new ApiResponse(200 , "product created succesfully" , product )
        )
    })

    // endpoint for getting all products 

    getAllProducts = asyncHandler(async(req,res) => {

        const filters = req.query;
        logger.info(`Received request to fetch products with filters: ${JSON.stringify(filters)}`);

        const allProducts = await this.productService.getAll(filters);

        if(!allProducts || allProducts.length == 0) {
            return new ApiError(404, "No products found")
        }

        logger.info(`Fetched ${allProducts.length} products`);

        return res
        .status(200)
        .json(
            new ApiResponse(200 ,  "product fetched succesfully" , allProducts)
        )
    })

    // get a product by id 

    getProduct = asyncHandler(async(req , res) => {
        const productId = req.params.id;

        if(!productId) {
            throw new ApiError(400 , "id is required");
        }

        logger.info(`Received request to fetch product with ID: ${productId}`)

        const product = await this.productService.getOne(productId)

        if (!product) {
            throw new ApiError(404, "Product not found");
        }
        logger.info(`Fetched product with ID: ${productId}`);

        return res
        .status(200)
        .json(
            new ApiResponse(200 , "product fetched succesfully" , product)
        )
    })

    // endpoint to update product details 

    updateProduct = asyncHandler( async( req , res ) => {
    
        const productId = req.params.id;
        if (!productId) {
            throw new ApiError(400 , "product id is required")
        }

        const updatedData = req.body;
        if(!updatedData) {
            throw new ApiError(400 , "details are required");
        }

        logger.info(`Received request to update product with ID: ${productId} and data: ${JSON.stringify(updatedData)}`);


        const updatedProduct = await this.productService.update(productId , updatedData);

        if (!updatedProduct) {
            throw new ApiError(404, "Product not found");
        }

        logger.info(`Product updated successfully with ID: ${productId}`);

        return res
        .status(200)
        .json(
            new ApiResponse(200 , "product updated succesfully " , updatedProduct)
        )   
    })


    // endpoint to delete a product(soft)

    delete = asyncHandler(async (req, res) => {

        // Get product ID from URL params
        const productId = req.params.id; 
        if (!productId) {
            throw new ApiError(400 , "product id is required")
        }

        logger.info(`Received request to soft delete product with ID: ${productId}`);

        const deletedProduct = await this.productService.delete(productId);

        if (!deletedProduct) {
            throw new ApiError(404, "Product not found");
        }

        logger.info(`Product soft-deleted successfully with ID: ${productId}`);
        
        return res
        .status(200)
        .json(
            new ApiResponse(200 , "product deleted succesfull" , "")
        )
  });
}

export default new ProductController();