import mongoose, { Schema } from "mongoose";

const productSchema = new Schema(
  {
    name: {
      type: String,
      required: [true, "Product name is required"],
      trim: true,
    },

    price: {
      type: Number,
      required: true,
      min: 1,
    },

    category: {
      type: String,
      enum: ["electronics", "fashion", "grocery", "other"],
      default: "other",
    },

    rating: {
      type: Number,
      min: 0,
      max: 5,
      default: 0,
    },

    status: {
      type: String,
      enum: ["active", "archived"],
      default: "active",
    },
  },
    { 
        timestamps: true 
    }

);


productSchema.virtual("priceWithTax").get(function () {
  return this.price * 1.18;
});

// adding indexing on status 
productSchema.index({ status: 1, createdAt: -1 });

// creating product models
const Product = mongoose.model("Product", productSchema);
export default Product;
