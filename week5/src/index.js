import express from "express"
import axios from "axios";

const app = express();


const fetchProd = async () => {
    try {
        const prod = await axios.get("https://dummyjson.com/products")

        console.log("fetched product succesfully ");
        console.log(prod.data.products)
        return prod.data.products
        
    } catch (error) {
        console.log("some error occured while fetching" , error);
        throw error
    }
}

app.get("/" , (req , res) => {

    res.send("hello from docker ")

})

app.get("/products", async (req, res) => {
  try {
    const products = await fetchProd(); 
    res.json(products); 
  } catch (error) {
    res.status(500).send("Error fetching products"); 
  }
});

app.listen(8080 , () => {
    console.log("server is listening at port 8080 🥳")
})



