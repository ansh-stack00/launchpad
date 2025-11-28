import productRepository from "../respositories/product.repository.js";
import logger from "../utils/loggers.js";

class ProductService {

    constructor(){
        this.productRepository = productRepository
    }

    async create(data) {
        logger.info('creating product ...')

        try {
            const product = await this.productRepository.create(data);
            logger.info(`product is creates with id : ${product._id}`)
            return product;

        } catch (error) {

            logger.error(`Error creating product: ${error.message}`);
            throw new Error(`Error creating product: ${error.message}`);
        }
    }




    async getAll(filters) {

        logger.info('Fetching all products with filters:', filters);

        try {

            const products = await this.productRepository.findPaginated(filters);
            logger.info(`Fetched ${products.length} products`);
            return products;

        } catch (error) {
            logger.error(`Error fetching products: ${error.message}`);
            throw new Error(`Error fetching products: ${error.message}`);
        }
    }

    async getOne(id) {
        logger.info(`Fetching product with ID: ${id}`);
        try {
            const product = await this.productRepository.findById(id);
            if (!product) {
                logger.warn(`Product with ID: ${id} not found`);
            }
            return product;

        } catch (error) {
            logger.error(`Error fetching product: ${error.message}`);
            throw new Error(`Error fetching product: ${error.message}`);
        }
    }

    async update(id, data) {
        logger.info(`Updating product with ID: ${id}`);
        try {
            const updatedProduct = await this.productRepository.update(id, data);
            logger.info(`Product with ID: ${id} updated successfully`);
            return updatedProduct;
        } catch (error) {

            logger.error(`Error updating product: ${error.message}`);
            throw new Error(`Error updating product: ${error.message}`);

        }
    }

    async delete(id) {
        logger.info(`Soft deleting product with ID: ${id}`);
        try {
            const deletedProduct = await this.productRepository.delete(id);
            logger.info(`Product with ID: ${id} soft-deleted successfully`);
            return deletedProduct;
        } catch (error) {
            logger.error(`Error deleting product: ${error.message}`);
            throw new Error(`Error deleting product: ${error.message}`);
        }
    }
}

export default new ProductService();

