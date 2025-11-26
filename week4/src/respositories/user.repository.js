import User from "../models/User.model.js";

class UserRepository {
  
  async create(data) {
    return await User.create(data);
  }

  async findById(id) {
    return await User.findById(id);
  }

  async findPaginated({ page = 1, limit = 10 }) {
    const skip = (page - 1) * limit;

    const users = await User.find()
      .sort({ createdAt: -1 })
      .skip(skip)
      .limit(limit);

    const count = await User.countDocuments();

    return {
      page,
      totalPages: Math.ceil(count / limit),
      totalItems: count,
      data: users,
    };
  }

  async update(id, data) {
    return await User.findByIdAndUpdate(id, data, {
      new: true,
      runValidators: true,
    });
  }

  async delete(id) {
    return await User.findByIdAndDelete(id);
  }
}

export default new UserRepository();
