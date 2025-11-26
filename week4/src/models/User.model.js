import mongoose, { Schema } from "mongoose";
import bcrypt from "bcrypt";

const userSchema = new Schema( 
    {

        firstName: {
        type: String,
        required: [true, "First name is required"],
        trim: true,
        },

        lastName: {
        type: String,
        required: [true, "Last name is required"],
        trim: true,
        },

        email: {
        type: String,
        required: [true, "Email is required"],
        unique: true,
        lowercase: true,
        },

        password: {
        type: String,
        required: [true, "Password is required"],
        minlength: 6,
        },

        status: {
        type: String,
        enum: ["active", "inactive"],
        default: "active",
        },
    },
    {
        timestamps:true
    }
)

// hash the password before saving it to db 

userSchema.pre("save" , async function(next) {
    if( !this.isModified("password")) return next();
    this.password = await bcrypt.hash(this.password , 10);
    next();

})

// custom method to check password is correct 

userSchema.methods.isPasswordCorrect = async function(password) {
    return await bcrypt.compare(password , this.password);
}

// creating a model 
const User = new mongoose.model("User" , userSchema);

export default User;