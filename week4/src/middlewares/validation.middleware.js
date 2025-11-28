import ApiError from "../utils/apiError.js";

const validate = (schema) => (req, _, next) => {
  try {
    schema.parse(req.body);
    next();
  } catch (err) {
    throw new ApiError(400, err.errors.map(e => e.message).join(", "));
  }
}

export default validate