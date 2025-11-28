import { z } from "zod";

const productSchema = z.object({
    prdName : z.string().min(3 , "Product name atleast 3 character long "),
    description : z.string().min(3,"description must be al least 3 characters long").max(200 , "must be  no more 200 character "),
    price : z.number().min(0 , "price must be greater than 0"),
    tags: z.array(z.string()).optional(),
    status: z.enum(['active', 'pending', 'cancelled']).optional(),
})

export default productSchema;