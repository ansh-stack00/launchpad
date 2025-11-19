
const productGrid = document.getElementById("productGrid");
const searchInput = document.getElementById("searchInput");
const sortSelect = document.getElementById("sortSelect");
const loading = document.getElementById("loading");
const noResults = document.getElementById("noResults");
const resultsInfo = document.getElementById("resultsInfo");

let products = [];
let filteredProducts = [];


async function fetchProducts() {
  try {
    loading.style.display = "block";

    const { data } = await axios.get("https://dummyjson.com/products");
    products = data.products;
    filteredProducts = products;

    renderProducts(filteredProducts);
  } catch (error) {
    console.error("Error fetching products:", error);
    productGrid.innerHTML = `<p style="color:white;">Failed to load products 😢</p>`;
  } finally {
    loading.style.display = "none";
  }
}


function renderProducts(productList) {
  productGrid.innerHTML = "";

  if (productList.length === 0) {
    noResults.style.display = "block";
    resultsInfo.textContent = "";
    return;
  } else {
    noResults.style.display = "none";
  }

  productList.forEach((product) => {
    const card = document.createElement("div");
    card.classList.add("product-card");

    card.innerHTML = `
      <img src="${product.thumbnail}" alt="${product.title}" class="product-image">
      <div class="product-info">
        <div class="product-brand">${product.brand || "Brand"}</div>
        <div class="product-title">${product.title}</div>
        <div class="product-description">${product.description}</div>
        <div class="product-footer">
          <div class="product-price">$${product.price}</div>
          <div class="product-rating">⭐ ${product.rating}</div>
        </div>
        <button class="add-to-cart">Add to Cart</button>
      </div>
    `;

    productGrid.appendChild(card);
  });

  resultsInfo.textContent = `Showing ${productList.length} of ${products.length} products`;
}


searchInput.addEventListener("input", (e) => {
  const query = e.target.value.toLowerCase();
  filteredProducts = products.filter((p) =>
    p.title.toLowerCase().includes(query)
  );
  applySort(); 
});

// Sorting
sortSelect.addEventListener("change", applySort);

function applySort() {
  const sortValue = sortSelect.value;
  let sorted = [...filteredProducts];

  switch (sortValue) {
    case "price-high":
      sorted.sort((a, b) => b.price - a.price);
      break;
    case "price-low":
      sorted.sort((a, b) => a.price - b.price);
      break;
    case "name":
      sorted.sort((a, b) => a.title.localeCompare(b.title));
      break;
    case "rating":
      sorted.sort((a, b) => b.rating - a.rating);
      break;
  }

  renderProducts(sorted);
}


fetchProducts();
