import Product from "../models/Product.model.js";

class ProductRepository {
  
  async create(data) {
    return await Product.create(data);
  }

  async findById(id) {
    return await Product.findById(id);
  }

  async findPaginated({ page = 1, limit = 10 }) {
    const skip = (page - 1) * limit;

    const products = await Product.find()
      .sort({ createdAt: -1 })
      .skip(skip)
      .limit(limit);

    const count = await Product.countDocuments();

    return {
      page,
      totalPages: Math.ceil(count / limit),
      totalItems: count,
      data: products,
    };
  }

  async update(id, data) {
    return await Product.findByIdAndUpdate(id, data, {
      new: true,
      runValidators: true,
    });
  }

  async delete(id) {
    return await Product.findByIdAndDelete(id);
  }
}

export default new ProductRepository();
