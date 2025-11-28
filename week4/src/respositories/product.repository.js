import Product from "../models/Product.model.js"

class ProductRepository {

  async create(data) {
    const product = new Product(data);
    return await product.save();
  }

  // exclude soft deleted products 
  async findById (id) {
    return await Product.findById(id).where('deletedAt').equals(null);
  }


  async findPaginated(filters , page=1 , limit = 10) {
    const query = this.buildQuery(filters);

    const product = await Product.find(query)
                    .skip((page-1) * limit)
                    .limit(limit)
                    .sort({createdAt : -1})

    return product;
  }

  async update (id , data ) {

    return await Product.findByIdAndUpdate(
      id , 
      data , 
      {
        new : true
      }
    )
  }

  buildQuery(filters) {
    let query = {};

    if (filters.search) {
      // Case-insensitive search
      query.name = { $regex: filters.search, $options: 'i' }; 
    }

    if (filters.minPrice) {
      query.price = { $gte: filters.minPrice };
    }

    if (filters.maxPrice) {
      query.price = query.price || {}; 
      query.price.$lte = filters.maxPrice;
    }

    if (filters.status) {
      query.status = filters.status;
    }

    if (filters.includeDeleted) {
      // Including soft-deleted products
      query.deletedAt = { $ne: null }; 
    } else {
      // Excluding soft-deleted products
      query.deletedAt = null; 
    }

    return query;
  }
}

export default new ProductRepository();