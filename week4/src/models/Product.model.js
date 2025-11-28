import mongoose, { Schema } from "mongoose";

const productSchema = new Schema( {

  prdName : {
    type : String,
    required : [true , "product name is required"],
    trim : true
  },
  description : {
    type : String ,
    required : [true , "description is required"],
    trim : true, 
  },
  price : {
    type : Number ,
    required : true
  },
  tags: [ String ],
  status : {
    type : String ,
    enum : ['active' , 'pending' , 'cancelled'],
    default : 'pending',

  },
  createdAt : {
    type : Date,
    default : Date.now
  },
  updatedAt : {
    type : Date,
    default : Date.now
  },
  deletedAt : {
    type : Date,
    default : null
  }

})


// pre-save hook for updating the product 
productSchema.pre("save" , function(next) {
  this.updatedAt = Date.now();
  next();
})

// virtual field 
productSchema.virtual("priceWithTax").get(function () {
  return this.price * 1.18;
});

// adding indexing on status 
productSchema.index({ status: 1, createdAt: -1 });

// creating product models
const Product = mongoose.model("Product", productSchema);
export default Product;
